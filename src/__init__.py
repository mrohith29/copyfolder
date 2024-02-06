from argparse import Namespace, ArgumentParser
import os
import shutil

def move():
    parser = ArgumentParser(description='Copies the files from the source folder to the destination folder')

    parser.add_argument('source', type=str, help='Enter the source folder', action='store_true')
    parser.add_argument('destination', type=str, help='Enter the destination folder', action='store_true')

    args: Namespace = parser.parse_args()

    if not os.path.isdir(args.source):
        print(f"Source directory {args.source} does not exist.")
        return

    if not os.path.isdir(args.destination):
        print(f"Destination directory {args.destination} does not exist.")
        return

    for file in os.listdir(args.source):
        file_path = os.path.join(args.source, file)
        if os.path.isdir(file_path):
            shutil.copytree(file_path, os.path.join(args.destination, file))
        elif os.path.isfile(file_path):
            shutil.copy(file_path, args.destination)

    print(f'Copying files from {args.source} to {args.destination}')

if __name__ == "__main__":
    move()