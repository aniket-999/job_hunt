from jinja2 import Environment, FileSystemLoader
import os

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), "templates")

env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))

def build_resume(context: dict) -> str:
    template = env.get_template("resume.tex.j2")
    return template.render(**context)