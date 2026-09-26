import subprocess 
from pathlib import Path
import shutil

template = Path("template.tex")

if not template.is_file():
    print("Base template for resume doesn't exist, please create template.tex in root directory")
    exit(1)

print("Copying template.tsx to resume.tsx")
shutil.copy("template.tex", "resume.tex")
print("Yay!! Copy success")

company_name = input("Enter Company Name: ")
company_website = input("Enter Company Website: ")

print("Paste the Job Description.")
print("Press Enter on an empty line when you're done:")

lines = []

while True:
    line = input()
    if line == "":
        break
    lines.append(line)

jd = "\n".join(lines)

str = "Read the prompt from here \\PROMPT.md file\n\n"

if company_name is not None:
    str += "- Company Name: " + company_name + "\n\n"
if company_website is None:
    str += "- Company Wesbite: " + company_website + "\n\n"

str += "# Job Description\n\n" + jd

subprocess.run("pbcopy", text=True, input=str)

print("Prompt Copy successfully, you can paste it into AI Agent")