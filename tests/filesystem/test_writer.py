from pathlib import Path
import pytest

from leetcode_importer.filesystem.writer import FileWriter


def test_write_creates_file(tmp_path: Path):
    writer = FileWriter()

    path = tmp_path / "solution.py"

    writer.write(
        path,
        "print('hello')",
    )

    assert path.exists()
    assert path.read_text() == "print('hello')"


def test_write_creates_parent_directories(tmp_path: Path):
    writer = FileWriter()

    path = (
        tmp_path
        / "python"
        / "array"
        / "solution.py"
    )

    writer.write(
        path,
        "content",
    )

    assert path.exists()


def test_write_raises_when_file_exists(tmp_path: Path):
    writer = FileWriter()

    path = tmp_path / "solution.py"

    path.write_text("old")

    with pytest.raises(FileExistsError):
        writer.write(
            path,
            "new",
        )


def test_write_overwrites_existing_file(tmp_path: Path):
    writer = FileWriter()

    path = tmp_path / "solution.py"

    path.write_text("old")

    writer.write(
        path,
        "new",
        overwrite=True,
    )

    assert path.read_text() == "new"