# Development Setup for Open STEAM Education Resources (MkDocs)

This document outlines the steps required to set up a development environment for the Open STEAM Education Resources project, which uses MkDocs with the Material for MkDocs theme.

## Prerequisites

Before you begin, ensure you have the following installed:

*   **Python 3:**  MkDocs is a Python-based tool. You'll need Python 3 installed on your system. You can check if you have Python installed by opening a terminal and typing `python3 --version`.
*   **pip:** This is the package installer for Python and usually comes bundled with Python 3. You can check if you have pip by opening a terminal and typing `pip --version`.

## Setup Steps

Follow these steps to set up your development environment:

1.  **Create a Virtual Environment:**

    Virtual environments are essential for isolating project dependencies. This prevents conflicts with other Python projects on your system.

    ```bash
    python3 -m venv .venv
    ```

    This command creates a new virtual environment named `.venv` in your project directory. You can choose a different name if you prefer.

2.  **Activate the Virtual Environment:**

    Before working on the project, you need to activate the virtual environment. This ensures that you're using the correct Python interpreter and libraries.

    *   **Linux/macOS:**

        ```bash
        source .venv/bin/activate
        ```

    *   **Windows:**

        ```bash
        .venv\Scripts\activate
        ```

    After activation, you'll see the name of the virtual environment (e.g., `(.venv)`) at the beginning of your terminal prompt.

3.  **Install `mkdocs-material`:**

    With the virtual environment activated, install the `mkdocs-material` package using `pip`:

    ```bash
    pip install mkdocs-material
    ```

    This command downloads and installs MkDocs, the Material for MkDocs theme, and its required dependencies within your virtual environment.

4.  **Build the Site:**

    Build the static HTML site from your Markdown files:

    ```bash
    mkdocs build
    ```

    This command will generate the static site in the `site` directory.

5.  **Serve the Site (Live Preview):**

    To preview your site locally with live reloading, use the `serve` command:

    ```bash
    mkdocs serve
    ```

    This will start a local web server, typically at `http://127.0.0.1:8000`. Any changes you make to your Markdown files will automatically be reflected in the browser.

## Development Workflow

Now that you've set up your environment, here's a typical workflow:

1.  **Activate the virtual environment:** (If you've closed your terminal)
    ```bash
    source .venv/bin/activate # Linux/macOS
    .venv\Scripts\activate # Windows
    ```
2. **Edit Content:** Modify the Markdown files (e.g., those in the `docs` folder or specified in your `mkdocs.yml` file).
3.  **Preview:** Run `mkdocs serve` to see your changes live in your web browser.
4.  **Build:** Before deploying, run `mkdocs build` to generate the final static website.
5. **Deactivate** when you are done : `deactivate`

## Deactivating the Virtual Environment

When you're finished working on the project, you can deactivate the virtual environment:

```bash
deactivate
