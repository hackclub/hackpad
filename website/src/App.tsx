import InfoCard from "./components/InfoCard.tsx";

export default function App() {
    return (
        <div className="pt-20 mt-20 text-black mx-64 font-mono">
            <div className="flex justify-center items-center align-middle">
              <div className="bg-green-400 inline-block p-2">
              <h1 className="text-6xl font-bold">HACKPAD</h1>
              </div>
            </div>
            <div>
                <h2 className="text-3xl">What's this?</h2>
                <p>Hackpad is a limited-time You Ship, We Ship (YSWS) where you can get a custom macropad!</p>
                <p>A macropad is a small, minified keyboard that you can program to do <i>anything</i> you want it to! 
                Stuff like [this] and [this]. People mainly use them for shortcuts, but they're also great typing messages,
                 as a MIDI controller, and pretty much anything you can think of!
                uch as
                different keybinds, storing secret messages, making a MIDI controller, etc there's some great examples
                </p>
                <a href="https://google.com/" target="_blank">sadf</a>
            </div>
            <div>
                <h2 className="text-3xl">What do I do?</h2>
                <div className="flex items-center justify-center">
                    <p>Design a pcb</p>
                    <p>Build a CAD model</p>
                    <p>Write firmware for it</p>

                </div>
                <p>Design a complete macropad following the three steps above!</p>
            </div>
            <div>
                <h2 className="text-3xl">What do I get?</h2>
                <div className="flex">
                    <img></img>
                    <p></p>
                </div>
            </div>
            <div>
                <h2>What do I do?</h2>

                <InfoCard
                    title={"Make a pcb"}
                    content={"SADFFASD"}
                    image={"./AS"}
                />
            </div>
            <h2 className="text-white text-3xl">HELLO</h2>
            <p className="text-white">hey what????!!!</p>
            <div></div>
        </div>
    );
}
