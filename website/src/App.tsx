import NavBar from "./components/NavBar";
import Footer from "./components/Footer";
import OrpheusFlag from "/OrpheusFlag.svg";

export default function App() {
  return (
    <div>
      <div>
        <img src={OrpheusFlag} className="max-w-20 sm:max-w-36 left-4 sm:left-12 absolute"></img>
      </div>
      <div className="fixed max-w-48 right-4 sm:right-5 md:right-10">
        <NavBar />
      </div>
      <div className="flex justify-center text-center">
        <div className="mt-16 text-slate-950 mx-8 md:max-w-6xl font-mono">
          <div className="flex justify-center items-center align-middle">
            <div className="bg-green-400 inline-block py-2 px-4 mb-8 rounded-sm">
              <h1 className="text-5xl sm:text-6xl font-bold">HACKPAD</h1>
            </div>
          </div>
          <img
            src="orpheuspadpic.png"
            className="w-full max-w-xl mx-auto"
          ></img>
          {/* <div className="absolute right-8 top-36 sm-rotate-12">
            <p>get your own macropad!</p>
          </div> */}
          <div>
            {/* <h2 className="text-3xl">How does it work?</h2> */}
            <div className="flex flex-row items-center justify-center space-x-4 sm:space-x-8 sm:space-y-6 md:space-y-0 py-6 text-md sm:text-2xl font-semibold">
              <div>
                <h3>Design a PCB</h3>
                <img
                  src="pcb_design_2.png"
                  className="max-h-56 sm:max-h-80 md:max-h-96 rounded-sm my-2 border-slate-600 border-4 p-1 sm:p-2 border-dashed"
                ></img>
              </div>
              <div>
                <h3>Build a case</h3>
                <img
                  src="cad_design_2.png"
                  className="max-h-56 sm:max-h-80 md:max-h-96 rounded-sm my-2 border-slate-600 border-4 p-1 sm:p-2 border-dashed"
                ></img>
              </div>
              <div>
                <h3>Code firmware</h3>
                <img
                  src="firmware_3.png"
                  className="max-h-56 sm:max-h-80 md:max-h-96 rounded-sm my-2 border-slate-600 border-4 p-1 sm:p-2 border-dashed"
                ></img>
              </div>
            </div>
            <div>
              <a href="/guide" className="flex justify-center">
                <p className="text-xl sm:text-2xl text-center bg-red-500 text-slate-50 max-w-54 sm:max-w-xl px-3 py-2 rounded-sm font-semibold border-black border-4">
                  Learn how to make a hackpad ➜
                </p>
              </a>
              <p className="text-xl font-semibold pt-2">...and join <a href="https://hackclub.slack.com/archives/C07LESGH0B0/p1727813799029559" target="_blank" className="text-2xl underline">#hackpad</a> on the <a href="https://hackclub.com/slack/" target="_blank"> Hack Club Slack</a>. Or else...</p>
            </div>
          </div>

          <div>
            <h2 className="text-xl py-3">What exactly is this?</h2>
            <p>
              Hackpad is a limited-time You Ship, We Ship (YSWS) where you can
              learn how to make your own macropad, and then we ship{" "}
              <b className="font-bold">your</b> design to you! Join{" "}
              <a>#hackpad</a> in the slack to stay up to date and see what other
              people are working on! Ends October 21st.
            </p>
            <br></br>
            <p>
              A macropad is a small, minified keyboard that you can program to
              do <i>anything</i> you want it to! People mainly use them for
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
                        This Lemon Keypad
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
      <div className="max-h-96 pt-16">
        <Footer />
      </div>
    </div>
  );
}
