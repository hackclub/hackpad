// import NavBar from "./components/NavBar";

export default function App() {
  return (
    <div>
      <div className="sm:fixed right-0 sm:right-5">{/* <NavBar /> */}</div>
      <div className="flex justify-center text-center">
        <div className="mt-16 text-slate-950 mx-20 md:max-w-6xl font-mono">
          <div className="flex justify-center items-center align-middle">
            <div className="bg-green-400 inline-block p-2 mb-8">
              <h1 className="text-6xl font-bold">HACKPAD</h1>
            </div>
          </div>
          <div>
            {/* <h2 className="text-3xl">How does it work?</h2> */}
            <div className="flex flex-col md:flex-row items-center justify-center md:space-x-24 space-y-6 md:space-y-0 py-6 text-2xl font-bold">
              <div>
                <h3>Design a PCB</h3>
                <img
                  src="pcb_design_2.png"
                  className="max-h-56 sm:max-h-96 rounded-sm my-6 border-slate-600 border-4 p-2 border-dashed"
                ></img>
              </div>
              <div>
                <h3>Build a case</h3>
                <img
                  src="cad_design_2.png"
                  className="max-h-56 sm:max-h-96 rounded-sm my-6 border-slate-600 border-4 p-2 border-dashed"
                ></img>
              </div>
              <div>
                <h3>Code firmware</h3>
                <img
                  src="firmware_2.png"
                  className="max-h-56 sm:max-h-96 rounded-sm my-6 border-slate-600 border-4 p-2 border-dashed"
                ></img>
              </div>
            </div>
            <div>
              <h2 className="text-2xl text-center">
                Get <i>your</i> macropad sent to you!!
              </h2>
            </div>
          </div>

          <div>
            <h2 className="text-xl py-3">What exactly is this?</h2>
            <p>
              Hackpad is a limited-time You Ship, We Ship (YSWS) where you can
              get your own custom macropad!
            </p>
            <br></br>
            <p>
              A macropad is a small, minified keyboard that you can program to
              do <i>anything</i> you want it to!. People mainly use them for
              shortcuts, custom keybinds, typing whole sentences, and even a
              MIDI controller! Some amazing examples:
              <div className="flex justify-center py-6">
                <div className="text-left ml-10">
                  <ul className="list-disc inline-block mr-12 underline">
                    <li>
                      <a
                        href="https://github.com/The-Royal/The_Royal_Open-Source-Projects/tree/schwann/01%20-%20Complete%20Kits"
                        target="_blank"
                      >
                        The RoMac
                      </a>
                    </li>
                    <li>
                      <a
                        href="https://github.com/palmacas/MacroBoard"
                        target="_blank"
                      >
                        The MacroBoard
                      </a>
                    </li>
                  </ul>
                  <ul className="list-disc inline-block underline">
                    <li>
                      <a
                        href="https://learn.adafruit.com/qtpy-lemon-mechanical-keypad-macropad/overview"
                        target="_blank"
                      >
                        This Lemon Keypad!
                      </a>
                    </li>
                    <li>
                      <a href="https://wooting.io/uwu" target="_blank">
                        The Wooting UwU
                      </a>
                    </li>
                  </ul>
                </div>
              </div>
            </p>
          </div>
          <div>
            <h2 className="text-2xl py-3 font-semibold">FAQ</h2>
            <p>{/* Some common questions you may have, answered here! */}</p>
            <div className="flex justify-center text-left">
              <div>
                <ul className="list-disc max-w-2xl">
                  <p className="font-bold text-lg">
                    Will my PCB come assembled?
                  </p>
                  <li>
                    {" "}
                    If you use only through-hole parts, It'll be assembled here
                    at HQ! If there are any SMD parts though, you'll have to
                    solder them yourself!
                  </li>
                  <p className="font-bold text-lg pt-4">Can I use X part??</p>
                  <li>
                    Probably! You can check the list of approved parts{" "}
                    <a
                      href="https://github.com/hackclub/hackpad/blob/main/APPROVED_PARTS.md"
                      target="_blank"
                    >
                      here
                    </a>
                    . If it's not there, run it by me @alexren on slack! Chances
                    are it's probably good to go
                  </li>
                </ul>
              </div>
            </div>
          </div>
          <div>
            <h2 className="text-2xl py-3 font-semibold">Requirements</h2>
            <p>
              Here are some rules your design should follow! It's not a
              comprehensive list, so if you have any questions please ask in
              #hackpad in the slack!
            </p>
            <div className="md:flex justify-center inline-block sm:gap-40 pt-4 text-left border-">
              <div>
                <ul className="list-disc max-w-96 space-y-2 pb-2">
                  <li>
                    The overall design uses 20 or less inputs/switches. This
                    includes rotary encoders!
                  </li>

                  <li>
                    The PCB is under 100mm in either direction, and only uses 2
                    layers
                  </li>
                </ul>
              </div>
              <div>
                <ul className="list-disc max-w-96 space-y-2">
                  <li>Your design is fully original </li>
                  <li>
                    The macropad uses a through-hole Seeed XIAO RP2040 as its
                    main MCU. No exceptions
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
