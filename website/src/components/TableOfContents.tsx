import { useEffect, useState } from "react";
import { useLocation } from "react-router-dom";

interface Heading {
    id: string;
    text: string;
    level: number;
}

const TableOfContents = () => {
    const [headings, setHeadings] = useState<Heading[]>([]);
    const [activeId, setActiveId] = useState<string>("");
    const { pathname } = useLocation();

    useEffect(() => {
        const nodes = document.querySelectorAll<HTMLElement>(
            "main h2[id], main h3[id]",
        );
        const found: Heading[] = Array.from(nodes).map((el) => ({
            id: el.id,
            text: el.textContent ?? "",
            level: Number(el.tagName[1]),
        }));
        setHeadings(found);

        if (found.length === 0) return;

        const observer = new IntersectionObserver(
            (entries) => {
                const visible = entries
                    .filter((e) => e.isIntersecting)
                    .sort(
                        (a, b) =>
                            a.boundingClientRect.top - b.boundingClientRect.top,
                    );
                if (visible[0]) setActiveId(visible[0].target.id);
            },
            { rootMargin: "-100px 0px -80% 0px", threshold: 0 },
        );

        nodes.forEach((n) => observer.observe(n));
        return () => observer.disconnect();
    }, [pathname]);

    if (headings.length === 0) return null;

    return (
        <nav className="text-sm">
            <p className="font-semibold text-slate-900 mb-2">On this page!</p>
            <ul className="space-y-1 border-l-2 border-slate-200">
                {headings.map((h) => (
                    <li key={h.id} className={h.level === 3 ? "ml-4" : ""}>
                        <a
                            href={`#${h.id}`}
                            className={`block -ml-0.5 pl-3 py-1 border-none transition-none font-medium ${
                                activeId === h.id
                                    ? "border-cyan-700 text-cyan-800 font-semibold"
                                    : "border-transparent text-slate-600 hover:text-cyan-800 font-medium"
                            }`}
                        >
                            {h.text}
                        </a>
                    </li>
                ))}
            </ul>
        </nav>
    );
};

export default TableOfContents;
