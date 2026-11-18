import { useState, type FormEvent } from "react";

// Attribution: ?ref=... (or ?utm_source=...) on the page URL, else "landing"
function getSource() {
    const params = new URLSearchParams(window.location.search);
    const ref = (params.get("ref") || params.get("utm_source") || "").trim();
    return ref ? ref.slice(0, 100) : "landing";
}

type Status = "idle" | "loading" | "success" | "error";

export default function EmailSignup() {
    const [email, setEmail] = useState("");
    const [status, setStatus] = useState<Status>("idle");
    const [message, setMessage] = useState("");

    async function handleSubmit(e: FormEvent) {
        e.preventDefault();
        setStatus("loading");
        setMessage("");

        try {
            // Same-origin on purpose: prod serves the site + API from one
            // Express server, and dev goes through the Vite /api proxy.
            const res = await fetch("/api/signup", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ email, source: getSource() }),
            });
            const data = await res.json().catch(() => ({}));
            if (!res.ok) throw new Error(data.error || "Something went wrong");

            setStatus("success");
            setMessage("Ty!! check your email :)");
            setEmail("");
        } catch (err) {
            setStatus("error");
            setMessage(
                err instanceof Error ? err.message : "Something went wrong",
            );
        }
    }

    return (
        <form
            onSubmit={handleSubmit}
            className="flex flex-col items-center w-0 min-w-full lg:w-auto lg:min-w-0"
        >
            <label htmlFor="signup-email" className="sr-only">
                Email address
            </label>
            <div className="flex w-full border-black border-4 rounded-sm text-xl sm:text-2xl ">
                <input
                    id="signup-email"
                    type="email"
                    required
                    placeholder="your@email.com"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    disabled={status === "loading"}
                    className="min-w-0 flex-1 lg:flex-none lg:w-72 bg-slate-50 text-slate-950 px-3 py-2 placeholder:text-slate-400 focus:outline-none disabled:opacity-60"
                />
                <button
                    type="submit"
                    disabled={status === "loading"}
                    className="bg-green-400 text-black px-3 py-2 border-l-4 border-black whitespace-nowrap hover:bg-green-500 disabled:opacity-60"
                >
                    {status === "loading" ? "..." : "get updates!"}
                </button>
            </div>
            {message && (
                <p
                    role="status"
                    className={`pt-2 font-semibold ${
                        status === "error" ? "text-red-600" : "text-green-700"
                    }`}
                >
                    {message}
                </p>
            )}
        </form>
    );
}
