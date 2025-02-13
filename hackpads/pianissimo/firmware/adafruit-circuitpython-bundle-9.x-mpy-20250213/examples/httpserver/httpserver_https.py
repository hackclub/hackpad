# SPDX-FileCopyrightText: 2024 Michał Pokusa
#
# SPDX-License-Identifier: Unlicense

import socketpool
import wifi

from adafruit_httpserver import Server, Request, Response


pool = socketpool.SocketPool(wifi.radio)
server = Server(
    pool,
    root_path="/static",
    https=True,
    certfile="cert.pem",
    keyfile="key.pem",
    debug=True,
)


@server.route("/")
def base(request: Request):
    """
    Serve a default static plain text message.
    """
    return Response(request, "Hello from the CircuitPython HTTPS Server!")


server.serve_forever(str(wifi.radio.ipv4_address), 443)
