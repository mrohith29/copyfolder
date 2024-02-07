from argparse import Namespace, ArgumentParser
import os
import shutil
from rich.console import Console

def move():
    console = Console()

    parser = ArgumentParser(description='Copies the files from the source folder to the destination folder')

    parser.add_argument('source', type=str, help='Enter the source folder')
    parser.add_argument('destination', type=str, help='Enter the destination folder')

    args = parser.parse_args()

    if not os.path.isdir(args.source):
        console.print(f"Source directory [red]{args.source}[/red] does not exist.")
        return

    if not os.path.isdir(args.destination):
        console.print(f"Destination directory [red]{args.destination}[/red] does not exist.")
        return

    for file in os.listdir(args.source):
        file_path = os.path.join(args.source, file)
        if os.path.isdir(file_path):
            shutil.copytree(file_path, os.path.join(args.destination, file))
        elif os.path.isfile(file_path):
            shutil.copy(file_path, args.destination)

    console.print(f'Copying files from [green]{args.source}[/green] to {args.destination}')

if __name__ == "__main__":
    move()