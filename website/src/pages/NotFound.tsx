import NavBar from "../components/NavBar";
import Footer from "../components/Footer";
import OrpheusFlag from "/OrpheusFlag.svg";

export default function NotFound() {
  return (
    <div className="min-h-screen flex flex-col">
      <div>
        <img
          src={OrpheusFlag}
          className="max-w-20 sm:max-w-36 left-4 sm:left-12 absolute"
        />
      </div>

      <div className="fixed max-w-48 right-4 sm:right-5 md:right-10">
        <NavBar />
      </div>

      <main className="flex-1 flex items-center justify-center px-6">
        <div className="text-center text-slate-950 font-mono max-w-2xl mt-24">
          <div className="inline-block bg-green-400 border-4 border-black border-dashed rounded-sm px-4 py-2 mb-4">
            <h1 className="text-4xl sm:text-6xl font-bold">404</h1>
          </div>
          <p className="text-xl sm:text-2xl font-semibold mb-3">
            this key does not exist
          </p>
          <p className="text-base sm:text-lg mb-8">
            Looks like this page got lost in the matrix scan.
          </p>

          <div className="flex flex-wrap justify-center gap-3">
            <a href="/" className="bg-red-500 text-slate-50 font-semibold border-4 border-black rounded-sm px-4 py-2">
              Back to home
            </a>
            <a href="/guide" className="bg-yellow-300 text-black font-semibold border-4 border-black rounded-sm px-4 py-2">
              Open guide
            </a>
            <a href="/gallery" className="bg-green-200 text-black font-semibold border-4 border-black rounded-sm px-4 py-2">
              View gallery
            </a>
          </div>
        </div>
      </main>

      <div className="max-h-96 pt-8">
        <Footer />
      </div>
    </div>
  );
}