from argparse import _SubParsersAction
from pathlib import Path

from huggingface_dl.parser import HfURLParser
from huggingface_dl.utils import (
    get_all_files,
    download_file,
    get_drive,
    custom_drive_cache_dir,
)


class HfCommands:
    @staticmethod
    def register_command(parser: _SubParsersAction):
        download_parser = parser.add_parser(
            "download", aliases=["dl"], help="Download files from huggingface"
        )
        download_parser.add_argument(
            "url",
            type=str,
            help="The url of the file to download",
        )
        download_parser.add_argument(
            "--output",
            "-o",
            type=str,
            help="The output path of the file to download",
            default=None,
        )
        download_parser.set_defaults(func=lambda args: DownloadCommand(args))

        ls_parser = parser.add_parser("ls", help="List files from huggingface")
        ls_parser.add_argument(
            "url",
            type=str,
            help="The url of the file to list",
        )
        ls_parser.set_defaults(func=lambda args: LsCommand(args))


class DownloadCommand:
    def __init__(self, args):
        self.args = args

    def run(self):
        url = HfURLParser(self.args.url)

        output = self.args.output
        if output is None:
            output = Path("./").resolve()
            if url.parsed_url["is_folder"] and url.parsed_url["file_path"] != "":
                output = output / url.parsed_url["file_path"].split("/")[-1]
            elif url.parsed_url["is_folder"] and url.parsed_url["file_path"] == "":
                output = output / url.parsed_url["repo_id"].split("/")[-1]
            else:
                pass
            output = str(output)

        files = get_all_files(
            url.parsed_url["repo_id"],
            url.parsed_url["repo_type"],
            url.parsed_url["revision"],
            url.parsed_url["file_path"],
            url.parsed_url["is_folder"],
        )

        if url.parsed_url["is_folder"]:
            print(f"Found {len(files)} file(s) in {url.parsed_url['file_path']}")
            for file in files:
                print(f"- {file}")
        else:
            print(f"Found 1 file {url.parsed_url['file_path']}")

        print(f"Downloading {len(files)} file(s) to {output}")

        drive = get_drive(output)

        with custom_drive_cache_dir(drive) as cache_dir:
            for file in files:
                download_file(
                    url.parsed_url["repo_id"],
                    url.parsed_url["repo_type"],
                    url.parsed_url["revision"],
                    file,
                    output,
                    cache_dir,
                )

        print("Done!")


class LsCommand:
    def __init__(self, args):
        self.args = args

    def run(self):
        url = HfURLParser(self.args.url)

        files = get_all_files(
            url.parsed_url["repo_id"],
            url.parsed_url["repo_type"],
            url.parsed_url["revision"],
            url.parsed_url["file_path"],
            url.parsed_url["is_folder"],
        )

        print(f"Found {len(files)} file(s) in {url.parsed_url['file_path']}")

        for file in files:
            print(f"- {file}")
