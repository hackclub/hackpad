const SideBarKeyboard = () => {
  return (
    <aside className= "bg-slate-100 space-y-2 max-w-prose p-4 h-screen border-r-4 border-slate-500 border-dashed">
      <nav>
        <ul>
          <li>
            <a href="/keyboard" className="block py-2 px-4 rounded hover:bg-slate-200 transition-all text-slate-900 hover:text-cyan-800">
              Keyboard Overview
            </a>
          </li>
          <li>
            <a href="/keyboard/faq" className="block py-2 px-4 rounded hover:bg-slate-200 transition-all text-slate-900 hover:text-cyan-800">
              FAQ v2
            </a>
          </li>
          <li>
            <a href="/guide" className="block py-2 px-4 rounded hover:bg-slate-200 transition-all text-red-400 hover:text-red-500">
              Back to macropads
            </a>
          </li>
        </ul>
      </nav>
    </aside>
  );
};

export default SideBarKeyboard;