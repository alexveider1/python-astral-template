# Python Repo Template

An opinionated [Cookiecutter](https://cookiecutter.readthedocs.io/) template for
Python projects built on the [Astral](https://astral.sh/) toolchain:
[uv](https://docs.astral.sh/uv/) for dependency management,
[Ruff](https://docs.astral.sh/ruff/) for linting and formatting, and
[ty](https://docs.astral.sh/ty/) for optional static type checking.

## Usage

Generate a new project straight from GitHub. With `uv` (nothing to install):

```bash
uvx cookiecutter gh:alexveider1/python-astral-template
```

Or with Cookiecutter already installed:

```bash
cookiecutter gh:alexveider1/python-astral-template
```

You will be prompted for:

| Prompt              | Description                                             | Default        |
| ------------------- | ------------------------------------------------------- | -------------- |
| `project_name`      | Human-readable project name                             | `Project name` |
| `project_slug`      | Package/folder name (auto-derived from `project_name`)  | *(derived)*    |
| `project_description` | Short description                                     | `Project description` |
| `author_name`       | Used in the generated `LICENSE`                         | `Your Name`    |
| `python_version`    | Target Python version (choose from the list)            | `3.12`         |
| `use_type_checking` | Include `ty` type checking (`y`/`n`)                    | `y`            |

## What gets generated

```text
<project_slug>/
├── .env
├── .env.example
├── .gitignore
├── LICENSE            # MIT, filled with author + current year
├── README.md
├── markdownlint.jsonc
├── pyproject.toml     # uv-managed; ruff (+ ty if enabled) in the dev group
├── ruff.toml
└── ty.toml            # only when type checking is enabled
```

The chosen `python_version` flows into `requires-python` (pyproject.toml),
`target-version` (ruff.toml), and `python-version` (ty.toml).

If you answer `n` to `use_type_checking`, a post-generation hook removes `ty`
from the dev dependencies, deletes `ty.toml`, and drops the type-checking
section from the generated README.

## Getting started with a generated project

```bash
cd <project_slug>
uv sync
uv run ruff check .
uv run ruff format .
uv run ty        # only if type checking was enabled
```
