#!/usr/bin/env python3

import google.generativeai as genai
import os
import argparse

# Configure your API key (replace with your actual API key)
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def translate_markdown_file(input_file, output_file, target_language="Spanish"):
    """
    Translates a markdown file using the Gemini API and saves the translated content
    to a new markdown file.

    Args:
        input_file: Path to the input markdown file.
        output_file: Path to the output markdown file.
        target_language: The target language for translation.
    """

    try:
        with open(input_file, "r", encoding="utf-8") as f:
            markdown_content = f.read()

        model = genai.GenerativeModel('gemini-2.0-flash')

        prompt = f"""
        Translate the following markdown content to {target_language}, preserving the original markdown formatting.

        Markdown content:
        ```markdown
        {markdown_content}
        ```

        Translated markdown:
        ```markdown
        """

        response = model.generate_content(prompt)

        translated_content = response.text.replace("```markdown", "").replace("```", "").strip()

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(translated_content)

        print(f"Translation successful. Translated content saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def translate_all_markdown_files(input_dir, output_dir, target_language="Catalan"):
    """
    Translates all the markdown files in a directory using the Gemini API and saves the translated content
    to new markdown files in a different directory.

    Args:
        input_dir: Path to the input directory containing markdown files.
        output_dir: Path to the output directory where translated markdown files will be saved.
        target_language: The target language for translation.
    """

    try:
        os.makedirs(output_dir, exist_ok=True)

        for file_name in os.listdir(input_dir):
            if file_name.endswith(".md"):
                input_file = os.path.join(input_dir, file_name)
                output_file = os.path.join(output_dir, file_name)

                translate_markdown_file(input_file, output_file, target_language)

    except FileNotFoundError:
        print(f"Error: Input directory '{input_dir}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def translate_all_markdown_files_recursive(input_dir, output_dir, target_language="Catalan"):
    """
    Translates all the markdown files in a directory and its subdirectories recursively using the Gemini API 
    and saves the translated content to new markdown files in a corresponding directory structure.

    Args:
        input_dir: Path to the input directory containing markdown files.
        output_dir: Path to the output directory where translated markdown files will be saved.
        target_language: The target language for translation.
    """

    try:
        os.makedirs(output_dir, exist_ok=True)

        for root, _, files in os.walk(input_dir):
            relative_path = os.path.relpath(root, input_dir)
            output_subdir = os.path.join(output_dir, relative_path)
            os.makedirs(output_subdir, exist_ok=True)

            for file_name in files:
                if file_name.endswith(".md"):
                    input_file = os.path.join(root, file_name)
                    output_file = os.path.join(output_subdir, file_name)

                    translate_markdown_file(input_file, output_file, target_language)

    except FileNotFoundError:
        print(f"Error: Input directory '{input_dir}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Translate markdown files using Gemini API.")
    parser.add_argument("src", help="Path to the input markdown file or the directory.")
    parser.add_argument("dst", help="Path to the output markdown file or the directory.")
    parser.add_argument("-l", "--language", default="Catalan", help="Target language for translation (default: Catalan).")
    parser.add_argument("-r", "--recursive", action="store_true", help="Translate recursively")

    args = parser.parse_args()
    
    if os.path.isfile(args.src) and os.path.isfile(args.dst):
        translate_markdown_file(args.src, args.dst, args.language)
        exit(0)
    elif os.path.isdir(args.src) and os.path.isdir(args.dst):
        if args.recursive:
            translate_all_markdown_files_recursive(args.src, args.dst, args.language)
        else:
            translate_all_markdown_files(args.src, args.dst, args.language)
        exit(0)
    else:
        print(f"Error: Invalid input or output. Both must be either files or directories.")
        exit(1)
   