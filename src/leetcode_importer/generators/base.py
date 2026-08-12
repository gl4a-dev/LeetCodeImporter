from abc import ABC, abstractmethod

from leetcode_importer.models.problem import LeetCodeProblem


class BaseGenerator(ABC):
    @abstractmethod
    def generate(self, problem: LeetCodeProblem) -> str:
        """Generate the file content."""