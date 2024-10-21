const SideBar = () => {
  return (
    <aside className= "bg-slate-100 space-y-2 max-w-prose p-4 h-screen border-r-4 border-slate-500 border-dashed">
      <nav>
        <ul>
        {/* <li>
            <a href="/note" className="block py-2 px-4 rounded hover:bg-slate-200 transition-all text-slate-900 hover:text-cyan-800">
              Troubleshooting
            </a>
          </li> */}
          <li>
            <a href="/guide" className="block py-2 px-4 rounded hover:bg-slate-200 transition-all text-slate-900 hover:text-cyan-800">
              DIY Guide
            </a>
          </li>
          <li>
            <a href="/resources" className="block py-2 px-4 rounded hover:bg-slate-200 transition-all text-slate-900 hover:text-cyan-800">
              Resources
            </a>
          </li>
          <li>
            <a href="/parts" className="block py-2 px-4 rounded hover:bg-slate-200 transition-all text-slate-900 hover:text-cyan-800">
              Approved Parts
            </a>
          </li>
          <li>
            <a href="/submitting" className="block py-2 px-4 rounded hover:bg-slate-200 transition-all text-slate-900 hover:text-cyan-800">
              Submit your project!
            </a>
          </li>
          <li>
            <a href="/faq" className="block py-2 px-4 rounded hover:bg-slate-200 transition-all text-slate-900 hover:text-cyan-800">
              FAQ
            </a>
          </li>
        </ul>
      </nav>
    </aside>
  );
};

export default SideBar;