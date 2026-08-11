# LeetCodeImporter

A Python library and CLI tool for importing LeetCode problems and generating organized source files for solving them.

The project is designed to make it easier to start working on a LeetCode problem by automatically retrieving its information and creating a ready-to-use source file.

## Features

* Fetch LeetCode problem information.
* Generate source files for different programming languages.
* Organize problems into directories based on their topics.
* Use the tool directly from the command line.
* Provide a reusable Python library.
* Support automated testing for each project module.

> **Current status:** Early development. Python is the first supported language.

## Installation

Clone the repository and install the project in editable mode:

```bash
git clone <repository-url>
cd LeetCodeImporter

python -m venv .venv
source .venv/bin/activate

pip install -e .
```

## Usage

Once installed, the project can be used through its command-line interface:

```bash
leetcode-importer --id 30 --language python
```

This will retrieve the specified LeetCode problem and generate the corresponding source file.

## Project Structure (proposed)

```text
LeetCodeImporter/
├── pyproject.toml
├── README.md
├── src/
│   └── leetcode_importer/
│       ├── __init__.py
│       ├── cli.py
│       │
│       ├── client/
│       │   ├── __init__.py
│       │   └── leetcode.py
│       │
│       ├── models/
│       │   ├── __init__.py
│       │   └── problem.py
│       │
│       ├── generators/
│       │   ├── __init__.py
│       │   ├── base.py
│       │   └── python.py
│       │
│       └── services/
│           ├── __init__.py
│           └── file_creator.py
│
└── tests/
    ├── client/
    ├── generators/
    └── services/
```

The project follows a modular architecture so that fetching problems, representing problem data, generating source code, and creating files can evolve independently.

## Development

Install the project in editable mode and run the test suite with:

```bash
pip install -e .
pytest
```

Tests are added alongside new modules to ensure that each component can be developed and validated independently.

## Roadmap

The initial development focuses on:

* [ ] Project structure
* [ ] Python package configuration
* [ ] Basic CLI
* [ ] LeetCode API client
* [ ] Problem data model
* [ ] Python source generator
* [ ] File creation service
* [ ] End-to-end CLI workflow
* [ ] Support for additional programming languages

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
