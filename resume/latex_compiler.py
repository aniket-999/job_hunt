import subprocess
import os

def compile_latex(job_id: str, latex_source: str):
    folder = f"data/resumes/{job_id}"
    os.makedirs(folder, exist_ok=True)

    tex_path = os.path.join(folder, "resume.tex")

    with open(tex_path, "w", encoding="utf-8") as f:
        f.write(latex_source)

    subprocess.run(
        ["pdflatex", "-interaction=nonstopmode", "resume.tex"],
        cwd=folder,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    pdf_path = os.path.join(folder, "resume.pdf")
    return pdf_path