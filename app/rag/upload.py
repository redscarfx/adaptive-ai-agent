from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DOCUMENTS_DIR = PROJECT_ROOT / "data" / "documents"


class UploadManager:

    @staticmethod
    def save(uploaded_file):

        DOCUMENTS_DIR.mkdir(
            parents=True,
            exist_ok=True,
        )

        path = DOCUMENTS_DIR / uploaded_file.name

        with open(path, "wb") as file:

            file.write(
                uploaded_file.getbuffer()
            )

        return path