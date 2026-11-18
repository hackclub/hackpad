import { Link } from "react-router-dom";
import { navLinks } from "../config/navLinks";

const SideBar = () => {
    return (
        <aside className="bg-slate-100 space-y-2 max-w-xl p-4 h-screen border-r-2 border-slate-500/50">
            <nav>
                <ul>
                    {navLinks.map((link) => (
                        <li key={link.href}>
                            <Link
                                to={link.href}
                                className="block py-2 px-4 rounded hover:bg-slate-200 transition-all text-slate-900 hover:text-cyan-800"
                            >
                                {link.label}
                            </Link>
                        </li>
                    ))}
                </ul>
            </nav>
        </aside>
    );
};

export default SideBar;
