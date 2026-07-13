import os
import subprocess

use_type_checking = "{{ cookiecutter.use_type_checking }}"

if use_type_checking == "n":
    file_path = "ty.toml"
    if os.path.exists(file_path):
        os.remove(file_path)


def init_git_repo():
    """Initialize a fresh git repository for the generated project."""
    try:
        subprocess.run(["git", "init", "-b", "main"], check=True)
    except subprocess.CalledProcessError:
        subprocess.run(["git", "init"])
    except FileNotFoundError:
        print("git not found; skipping repository initialization.")
        return


def create_venv():
    """Create a virtual environment using the pinned Python version."""
    try:
        subprocess.run(["uv", "venv"], check=True)
    except subprocess.CalledProcessError:
        print("uv venv failed; skipping virtual environment creation.")
    except FileNotFoundError:
        print("uv not found; skipping virtual environment creation.")


init_git_repo()
create_venv()
