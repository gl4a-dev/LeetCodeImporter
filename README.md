# LeetCodeImporter

A Python library and CLI for importing LeetCode problems into your local project. It retrieves the problem statement and starter code directly from the LeetCode GraphQL API, then generates a source file using language-specific templates.

The project was designed to be modular and extensible, making it easy to support new programming languages, customize templates, and integrate into different workflows.

---

## Features

* Fetch problems directly from the LeetCode GraphQL API.
* Generate starter files from language-specific templates.
* Simple command-line interface built with Click.
* Modular architecture following the Single Responsibility Principle.
* Easy to extend with additional languages.
* Fully tested with `pytest`.

---

## Installation

### Clone the repository

```bash
git clone https://github.com/gl4a-dev/LeetCodeImporter.git
cd LeetCodeImporter
```

### Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**Linux / macOS**

```bash
source .venv/bin/activate
```

**Windows**

```powershell
.venv\Scripts\activate
```

### Install in editable mode

```bash
pip install -e .
```

## Simple installation

```bash
pip install git+https://github.com/gl4a-dev/LeetCodeImporter.git@v0.1.0
```

---

## Usage

Generate a Python solution file for a LeetCode problem:

```bash
leetcode-importer --id 1 --language python
```

By default, the generated file will be placed inside the `problems` directory.

### Custom output directory

```bash
leetcode-importer \
    --id 30 \
    --language python \
    --output-dir solutions
```

### Overwrite an existing file

```bash
leetcode-importer \
    --id 1 \
    --language python \
    --overwrite
```

---

## Generated File

Example output:

```python
"""
0001. Two Sum

Given an array of integers...
"""

class Solution(object):
    def twoSum(self, nums, target):
        ...
```

---

## Project Structure

```text
src/
└── leetcode_importer/
    ├── client/
    ├── filesystem/
    ├── generators/
    │   └── templates/
    ├── models/
    ├── parsers/
    ├── services/
    ├── cli.py
    └── exceptions.py

tests/
```

---

## Architecture

The library is organized into independent components:

| Component          | Responsibility                                   |
| ------------------ | ------------------------------------------------ |
| `LeetCodeClient`   | Fetches data from the LeetCode API               |
| `LeetCodeProblem`  | Represents a LeetCode problem                    |
| `GeneratorFactory` | Creates the appropriate generator for a language |
| `PythonGenerator`  | Renders the output file using Jinja2 templates   |
| `FileWriter`       | Writes generated content to disk                 |
| `ImportService`    | Coordinates the complete import workflow         |
| `CLI`              | User-facing command-line interface               |

---

## Running the Tests

Run all tests:

```bash
pytest
```

Run with coverage:

```bash
pytest --cov=leetcode_importer
```

---

## Adding Support for a New Language

Supporting a new language involves three steps:

1. Create a new generator.

```text
generators/
    java.py
```

2. Create a new Jinja template.

```text
generators/templates/
    java.j2
```

3. Register the generator in `GeneratorFactory`.

No changes to the CLI or the import workflow are required.

---

## License

This project is licensed under the MIT License. See the [LICENCE](LICENSE) file for details.
