import os

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


init_git_repo()
