# SPDX-FileCopyrightText: 2024 Michał Pokusa
#
# SPDX-License-Identifier: Unlicense

try:
    from typing import Dict, List, Tuple, Union
except ImportError:
    pass

from asyncio import create_task, gather, run, sleep
from random import choice

import socketpool
import wifi

from adafruit_pycamera import PyCamera
from adafruit_httpserver import Server, Request, Response, Headers, Status, OK_200


pool = socketpool.SocketPool(wifi.radio)
server = Server(pool, debug=True)


camera = PyCamera()
camera.display.brightness = 0
camera.mode = 0  # JPEG, required for `capture_into_jpeg()`
camera.resolution = "1280x720"
camera.effect = 0  # No effect


class XMixedReplaceResponse(Response):
    def __init__(
        self,
        request: Request,
        frame_content_type: str,
        *,
        status: Union[Status, Tuple[int, str]] = OK_200,
        headers: Union[Headers, Dict[str, str]] = None,
        cookies: Dict[str, str] = None,
    ) -> None:
        super().__init__(
            request=request,
            headers=headers,
            cookies=cookies,
            status=status,
        )
        self._boundary = self._get_random_boundary()
        self._headers.setdefault(
            "Content-Type", f"multipart/x-mixed-replace; boundary={self._boundary}"
        )
        self._frame_content_type = frame_content_type

    @staticmethod
    def _get_random_boundary() -> str:
        symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        return "--" + "".join([choice(symbols) for _ in range(16)])

    def send_frame(self, frame: Union[str, bytes] = "") -> None:
        encoded_frame = bytes(
            frame.encode("utf-8") if isinstance(frame, str) else frame
        )

        self._send_bytes(
            self._request.connection, bytes(f"{self._boundary}\r\n", "utf-8")
        )
        self._send_bytes(
            self._request.connection,
            bytes(f"Content-Type: {self._frame_content_type}\r\n\r\n", "utf-8"),
        )
        self._send_bytes(self._request.connection, encoded_frame)
        self._send_bytes(self._request.connection, bytes("\r\n", "utf-8"))

    def _send(self) -> None:
        self._send_headers()

    def close(self) -> None:
        self._close_connection()


stream_connections: List[XMixedReplaceResponse] = []


@server.route("/frame")
def frame_handler(request: Request):
    frame = camera.capture_into_jpeg()

    return Response(request, body=frame, content_type="image/jpeg")


@server.route("/stream")
def stream_handler(request: Request):
    response = XMixedReplaceResponse(request, frame_content_type="image/jpeg")
    stream_connections.append(response)

    return response


async def send_stream_frames():
    while True:
        await sleep(0.1)

        frame = camera.capture_into_jpeg()

        for connection in iter(stream_connections):
            try:
                connection.send_frame(frame)
            except BrokenPipeError:
                connection.close()
                stream_connections.remove(connection)


async def handle_http_requests():
    server.start(str(wifi.radio.ipv4_address))

    while True:
        await sleep(0)

        server.poll()


async def main():
    await gather(
        create_task(send_stream_frames()),
        create_task(handle_http_requests()),
    )


run(main())
