import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import App from "./App.tsx";

import Tutorial from "./pages/Tutorial.mdx";
import Submission from "./pages/Submission.mdx";
import ApprovedParts from "./pages/ApprovedParts.mdx";
import Faq from "./pages/Faq.mdx";
import Braindump from "./pages/Braindump.mdx"
import Resources from "./pages/Resources.mdx"
import ResearchNote from "./pages/ResearchNote.mdx"
import GetKeycap from "./pages/GetKeycap.mdx"

import DocPage from "./layouts/DocPage.tsx";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import "./index.css";


// IMPORT YOUR PROJECTS HERE
import OrpheusPad from "./pages/submissions/Orpheuspad/OrpheusPad.mdx"
import CyaoPad from "./pages/submissions/Cyaopad/CyaoPad.mdx"
import Wang01 from "./pages/submissions/Wang01/Wang01.mdx"

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
  },
  {
    path: "/guide",
    element: (
      <DocPage Content={Tutorial} />
    ),
  },
  {
    path: "/submitting",
    element: <DocPage Content={Submission} />,
  },
  {
    path: "/parts",
    element: <DocPage Content={ ApprovedParts } />,
  },
  {
    path: "/faq",
    element: <DocPage Content={ Faq } />,
  },
  {
    path: "/braindump",
    element: <DocPage Content={ Braindump } />,
  },
  {
    path: "/resources",
    element: <DocPage Content={ Resources } />,
  },
  {
    path: "/note",
    element: <DocPage Content={ ResearchNote } />,
  },
  {
    path: "/get-keycap",
    element: <DocPage Content={ GetKeycap } />,
  },

  // Submitting? Great! Do something like this:
  {
    path: "/projects/orpheuspad",
    element: <DocPage Content={ OrpheusPad } />
  },
  {
    path: "/projects/cyaopad",
    element: <DocPage Content={ CyaoPad } />
  },
  {
    path: "/projects/wang01",
    element: <DocPage Content={ Wang01 } />
  }
]);

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <RouterProvider router={router} />
  </StrictMode>
);
