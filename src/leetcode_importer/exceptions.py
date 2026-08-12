class LeetCodeImporterError(Exception):
    """Base exception for the project."""


class ProblemNotFoundError(LeetCodeImporterError):
    """Raised when the requested problem cannot be found."""


class InvalidAPIResponseError(LeetCodeImporterError):
    """Raised when the API returns an unexpected response."""