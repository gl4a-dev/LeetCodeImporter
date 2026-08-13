from abc import ABC, abstractmethod

from jinja2 import Environment, PackageLoader

from leetcode_importer.models.problem import LeetCodeProblem


class BaseGenerator(ABC):
    template_name: str
    language: str
    extension: str

    _environment = Environment(
        loader=PackageLoader(
            package_name="leetcode_importer.generators",
            package_path="templates",
        ),
        autoescape=False,
        trim_blocks=True,
        lstrip_blocks=True,
    )

    @abstractmethod
    def generate(self, problem: LeetCodeProblem) -> str:
        """Generate the source code for a problem."""

    def render(self, **context) -> str:
        template = self._environment.get_template(self.template_name)
        return template.render(**context)