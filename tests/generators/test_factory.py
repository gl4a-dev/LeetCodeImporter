import pytest

from leetcode_importer.generators.factory import GeneratorFactory
from leetcode_importer.generators.python import PythonGenerator


def test_create_python_generator():
    generator = GeneratorFactory.create("python")

    assert isinstance(generator, PythonGenerator)


def test_create_python_generator_case_insensitive():
    generator = GeneratorFactory.create("PyThOn")

    assert isinstance(generator, PythonGenerator)


def test_create_unsupported_generator():
    with pytest.raises(ValueError):
        GeneratorFactory.create("javascript")