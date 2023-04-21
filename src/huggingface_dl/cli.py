# ref: https://github.com/huggingface/huggingface_hub/blob/main/src/huggingface_hub/commands/huggingface_cli.py

from argparse import ArgumentParser

from huggingface_dl.commands.huggingface import HfCommands


def main():
    parser = ArgumentParser("huggingface-dl", usage="huggingface-dl <command> [<args>]")
    commands_parser = parser.add_subparsers(help="huggingface-dl command helpers")

    # Register commands
    HfCommands.register_command(commands_parser)

    # Let's go
    args = parser.parse_args()

    if not hasattr(args, "func"):
        parser.print_help()
        exit(1)

    # Run
    service = args.func(args)
    service.run()


if __name__ == "__main__":
    main()
