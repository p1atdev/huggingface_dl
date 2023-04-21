from urllib.parse import urlparse


class HfURLParser:
    def __init__(self, url: str):
        self.url = url
        parsed_url = self.parse(url)

        self.parsed_url = parsed_url

    def parse(self, url: str):
        parsed_url = urlparse(url)

        if parsed_url.netloc != "huggingface.co":
            raise ValueError("This url is not a valid huggingface url")

        path_parts = parsed_url.path.strip("/").split("/")

        repo_type = "model"
        if path_parts[0] in ["datasets", "spaces"]:
            repo_type = path_parts.pop(0)[:-1]

        repo_id = "/".join(path_parts[:2])
        path_parts = path_parts[2:]

        revision = None
        file_path = ""
        is_folder = True

        if len(path_parts) >= 2 and path_parts[0] in [
            "blob",
            "resolve",
        ]:  # /blob/revision(/path/to/file)
            path_parts.pop(0)
            revision = path_parts.pop(0)
            file_path = "/".join(path_parts)
            is_folder = False
        elif (
            len(path_parts) >= 2 and path_parts[0] == "tree"
        ):  # /tree/revision(/path/to/folder)
            path_parts.pop(0)
            revision = path_parts.pop(0)
            file_path = "/".join(path_parts)
            is_folder = True
        else:
            file_path = "/".join(path_parts)

        return {
            "repo_type": repo_type,
            "repo_id": repo_id,
            "revision": revision,
            "file_path": file_path,
            "is_folder": is_folder,
        }
