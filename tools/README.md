# Markdown Translator with Gemini API

This script, `translate.py`, is a command-line tool that translates Markdown files into other languages using the Google Gemini API. It leverages the `google.generativeai` library to interact with the API.

## Features

*   **Markdown Support:** Handles Markdown files, preserving the original structure during translation.
*   **Gemini API:** Uses the Google Gemini API (specifically, the `gemini-2.0-flash` model) to perform translations.
*   **Language Code/Name Support:** Accepts the name of the target language (e.g., "Spanish", "French", "Catalan").
*   **Batch Translation:** Can translate a single file or an entire directory of Markdown files.
*   **Command-line Interface:** Uses the command line to get the necessary arguments (input, output, and target language).
* **Environment Variable:** Uses the environment variable to get the API KEY.

## Prerequisites

1.  **Python 3:** Ensure you have Python 3 installed on your system.
2.  **Gemini API Key:** You'll need a Google Gemini API key. Set it as an environment variable:

    ```bash
    export GEMINI_API_KEY="your_api_key_here"
    ```

3.  **Required Libraries:** Install the `google-generativeai` library:

    ```bash
    pip install google-generativeai
    ```

## Usage

1.  **Run the script:**

    ```bash
    python translate.py <src> <dst> [-l <language>]
    ```

    Or if you made the script executable

    ```bash
    ./translate.py <src> <dst> [-l <language>]
    ```

2.  **Arguments:**

    *   **`<src>`:** This is the first required argument. It can be:
        *   The path to the input Markdown file you want to translate (e.g., `my_document.md`).
        * The path to the input directory containing markdown files.
    *   **`<dst>`:** This is the second required argument. It can be:
        *   The path to where you want to save the translated Markdown file (e.g., `my_document.ca.md`).
        * The path to the output directory where translated markdown files will be saved.
    *   **`-l` or `--language`:** This is an optional argument to specify the target language. If not provided, the default is "Catalan". (e.g. `-l Spanish` or `--language French`).

3.  **Translation:** The script will translate the input Markdown file or all the files in a directory and save the translated content to the specified output file or directory.

4.  **Success Message:** If the translation is successful, you'll see a message like:

    ```
    Translation successful. Translated content saved to my_document_es.md
    ```

## Examples

**Example 1: Translating a Single File**

Let's say you want to translate `my_document.en.md` (in your current working directory) into Catalan and save it as `my_document.ca.md` in the same directory:

```bash
python translate.py my_document.md my_document_es.md -l Catalan
```

**Example 2: Translating a Directory of Files**

Let's say you want to translate all the files in the docs directory into catalan and save them to the docs/ca directory.

```bash
python translate.py docs/en docs/ca -l Catalan
```
