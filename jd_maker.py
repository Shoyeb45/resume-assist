import sys
import subprocess
from pathlib import Path
import shutil

template = Path("template.tex")

if not template.is_file():
    print(
        "Base template for resume doesn't exist, please create template.tex in root directory"
    )
    exit(1)

print("Copying template.tsx to resume.tsx")
shutil.copy("template.tex", "resume.tex")
print("Yay!! Copy success")

company_name = input("Enter Company Name: ")
company_website = input("Enter Company Website: ")

print("Paste the Job Description.")
print("Press Enter on an empty line when you're done:")

print("Paste the Job Description.")
print("Type END_JD on a new line when you're done:")

lines = []

while True:
    line = input()

    if line == "END_JD":
        break

    lines.append(line)

jd = "\n".join(lines)

str = "Read the prompt from here \\PROMPT.md file\n\n"

if company_name:
    str += "- Company Name: " + company_name + "\n\n"
if company_website:
    str += "- Company Wesbite: " + company_website + "\n\n"

str += "# Job Description\n\n" + jd


def copy_to_clipboard(text):
    if sys.platform == "darwin":
        command = ["pbcopy"]

    elif sys.platform == "win32":
        command = ["clip"]

    elif sys.platform.startswith("linux"):
        if shutil.which("wl-copy"):
            command = ["wl-copy"]
        elif shutil.which("xclip"):
            command = ["xclip", "-selection", "clipboard"]
        elif shutil.which("xsel"):
            command = ["xsel", "--clipboard", "--input"]
        else:
            raise RuntimeError(
                "No clipboard utility found. Install wl-clipboard, xclip, or xsel."
            )

    else:
        raise RuntimeError(f"Unsupported OS: {sys.platform}")

    subprocess.run(command, input=text, text=True, check=True)


copy_to_clipboard(str)

print("Prompt Copy successfully, you can paste it into AI Agent")
