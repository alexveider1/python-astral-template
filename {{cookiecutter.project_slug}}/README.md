# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Setup

This project uses [`uv`](https://docs.astral.sh/uv/) for fast Python dependency management.

```bash
uv sync
```

## Linting and Formatting

This project uses [`ruff`](https://docs.astral.sh/ruff/). To check and format your code:

```bash
uv run ruff check .
uv run ruff format .
```
{% if cookiecutter.use_type_checking == 'y' %}
## Type Checking

This project uses [`ty`](https://github.com/astral-sh/ty) for static type analysis.

```bash
uv run ty
```
{% endif %}
