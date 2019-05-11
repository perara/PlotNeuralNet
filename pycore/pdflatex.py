
import subprocess
import os

def _get_pdflatex_path():
    out = subprocess.Popen(["/usr/bin/which", "pdflatex"], stdout=subprocess.PIPE)
    x = out.communicate()[0].decode("utf-8").strip()
    return x


def _is_pdflatex_installed():
    return _get_pdflatex_path() != ""



def convert_from_path(file_path, file_output=None):
    data = None
    with open(file_path, "rb") as f:
        data = f.read()

    if data is None:
        raise ValueError("Data is empty. No tex exists!")

    if file_output is None:
        head, tail = os.path.split(file_path)
        tail = os.path.splitext(tail)[0] + ".pdf"
        file_output = os.path.join(head, tail)

    convert_from_string(data, file_output)

def convert_from_string(data, file_output):
    if not _is_pdflatex_installed():
        raise ModuleNotFoundError("pdflatex is not installed/supported.")

    out = subprocess.Popen([_get_pdflatex_path()], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    out.stdin.write(data)

    x = out.communicate()[0].decode("utf-8")

