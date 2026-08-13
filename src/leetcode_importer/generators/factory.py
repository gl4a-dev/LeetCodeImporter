from leetcode_importer.generators.base import BaseGenerator
from leetcode_importer.generators.python import PythonGenerator


class GeneratorFactory:

    _generators: dict[str, type[BaseGenerator]] = {
        "python": PythonGenerator,
    }

    @classmethod
    def create(cls, language: str) -> BaseGenerator:

        try:
            generator = cls._generators[language.lower()]

        except KeyError as exc:
            supported = ", ".join(sorted(cls._generators))
            
            raise ValueError(
                f"Unsupported language '{language}'. "
                f"Supported languages: {supported}."
            ) from exc

        return generator()