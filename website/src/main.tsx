import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import App from "./App.tsx";

import SimpleTutorial from "./pages/hackpad/SimpleTutorial.mdx";
import Submission from "./pages/hackpad/Submission.mdx";
import KitContents from "./pages/hackpad/KitContents.md";
import Faq from "./pages/hackpad/Faq.mdx";
import Braindump from "./pages/hackpad/deprecated/Braindump.mdx";
import Resources from "./pages/hackpad/Resources.mdx";
import GetKeycap from "./pages/hackpad/deprecated/GetKeycap.mdx";
import CardGrant from "./pages/hackpad/CardGrant.mdx";
import Guide from "./pages/hackpad/guide_staging.md";
import OtherParts from "./pages/hackpad/OtherParts.mdx";
import Assembly from "./pages/hackpad/Assembly.md";

import Overview from "./pages/hackboard/Overview.mdx";
import Faq2 from "./pages/hackboard/Faq2.mdx";

import DocPage from "./layouts/DocPage.tsx";
import SideBarKeyboard from "./components/SideBarKeyboard.tsx";
import SideBar from "./components/SideBar.tsx";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import "./index.css";

import Gallery from "./pages/Gallery";
import NotFound from "./pages/NotFound";

// IMPORT YOUR PROJECTS HERE
import OrpheusPad from "./pages/submissions/Orpheuspad/OrpheusPad.mdx";
import CyaoPad from "./pages/submissions/Cyaopad/CyaoPad.mdx";
import Wang01 from "./pages/submissions/Wang01/Wang01.mdx";

const router = createBrowserRouter([
    {
        path: "/",
        element: <App />,
    },
    {
        path: "/gallery",
        element: <Gallery />,
    },
    {
        // Layout route for pages using the main SideBar
        element: <DocPage SideBar={SideBar} />,
        children: [
            { path: "/guide", element: <SimpleTutorial /> },
            { path: "/add-components", element: <OtherParts /> },
            { path: "/guide-staging", element: <Guide /> },
            { path: "/assembly", element: <Assembly /> },
            { path: "/submitting", element: <Submission /> },
            { path: "/parts", element: <KitContents /> },
            { path: "/faq", element: <Faq /> },
            { path: "/braindump", element: <Braindump /> },
            { path: "/resources", element: <Resources /> },
            { path: "/get-keycap", element: <GetKeycap /> },
            { path: "/cardgrant", element: <CardGrant /> },
            // Submitting? Great! Do something like this:
            { path: "/projects/orpheuspad", element: <OrpheusPad /> },
            { path: "/projects/cyaopad", element: <CyaoPad /> },
            { path: "/projects/wang01", element: <Wang01 /> },
        ],
    },
    {
        // Layout route for pages using the keyboard SideBar
        element: <DocPage SideBar={SideBarKeyboard} />,
        children: [
            { path: "/keyboard", element: <Overview /> },
            { path: "/keyboard/faq", element: <Faq2 /> },
        ],
    },
    {
        path: "*",
        element: <NotFound />,
    }
]);

createRoot(document.getElementById("root")!).render(
    <StrictMode>
        <RouterProvider router={router} />
    </StrictMode>,
);
