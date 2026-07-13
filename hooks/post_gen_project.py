import os

use_type_checking = "{{ cookiecutter.use_type_checking }}"

if use_type_checking == "n":
    file_path = "ty.toml"
    if os.path.exists(file_path):
        os.remove(file_path)
