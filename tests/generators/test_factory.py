import pytest

from leetcode_importer.generators.factory import GeneratorFactory
from leetcode_importer.generators.python import PythonGenerator
from leetcode_importer.generators.cpp import CppGenerator
from leetcode_importer.generators.java import JavaGenerator


def test_create_python_generator():
    generator = GeneratorFactory.create("python")

    assert isinstance(generator, PythonGenerator)


def test_create_python_generator_case_insensitive():
    generator = GeneratorFactory.create("PyThOn")

    assert isinstance(generator, PythonGenerator)


def test_create_java_generator():
    generator = GeneratorFactory.create("java")

    assert isinstance(generator, JavaGenerator)


def test_create_cpp_generator():
    generator = GeneratorFactory.create("cpp")

    assert isinstance(generator, CppGenerator)


def test_create_unsupported_generator():
    with pytest.raises(ValueError):
        GeneratorFactory.create("javascript")