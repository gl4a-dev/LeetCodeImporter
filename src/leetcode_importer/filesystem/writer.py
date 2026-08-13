from pathlib import Path


class FileWriter:

    def write(self, path: Path, content: str, overwrite: bool = False) -> Path:

        if path.exists() and not overwrite:
            raise FileExistsError(
                f"File '{path}' already exists."
            )

        path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        path.write_text(
            content,
            encoding="utf-8",
        )

        return path