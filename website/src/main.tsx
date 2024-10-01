import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import App from "./App.tsx";

import Tutorial from "./pages/Tutorial.mdx";
import Submission from "./pages/Submission.mdx";
import ApprovedParts from "./pages/ApprovedParts.mdx";
import Faq from "./pages/Faq.mdx";
import Braindump from "./pages/Braindump.mdx"

import DocPage from "./layouts/DocPage.tsx";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import "./index.css";

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
  }
]);

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <RouterProvider router={router} />
  </StrictMode>
);
