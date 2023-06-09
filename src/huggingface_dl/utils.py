from pathlib import Path
import tempfile
import os
from typing import List, Optional
from contextlib import contextmanager
from huggingface_hub import hf_api, hf_hub_download


def get_all_files(
    repo_id: str, repo_type: str, revision: str, file_path: str, is_folder: bool
):
    api = hf_api.HfApi()

    files = api.list_repo_files(repo_id=repo_id, repo_type=repo_type, revision=revision)

    if is_folder:
        return [file for file in files if file.startswith(file_path)]
    else:
        return [file for file in files if file == file_path]


def download_file(
    repo_id: str,
    repo_type: str,
    revision: str,
    file_path: str,
    out_dir: str,
    cache_dir: Optional[str] = None,
):
    hf_hub_download(
        repo_id=repo_id,
        repo_type=repo_type,
        filename=file_path,
        revision=revision,
        local_dir=out_dir,
        cache_dir=cache_dir,
        local_dir_use_symlinks=False,
    )


def get_drive(path: str):
    resolved_path = Path(path).resolve()
    drive = resolved_path.drive
    root = resolved_path.root
    return drive + root


@contextmanager
def custom_drive_cache_dir(drive: str):
    resolved_drive = Path(drive)
    base_dir = resolved_drive / "tmp"
    if not base_dir.exists():
        os.makedirs(base_dir)
    print(f"Using {base_dir.resolve()} as cache dir")
    with tempfile.TemporaryDirectory(dir=base_dir) as tmp_dir:
        yield tmp_dir
