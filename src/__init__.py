from argparse import Namespace, ArgumentParser
import os
import shutil

parser = ArgumentParser(description='Copies the files from the sourse folder to the destination folder')

parser.add_argument('source', type=str, help='Enter the source folder', const=os.listdir(), nargs='?')

parser.add_argument('destination', type=str, help='Enter the destination folder', const=os.listdir(), nargs='?')

args: Namespace = parser.parse_args()

for file in os.listdir(args.source):
    file_path = os.path.join(args.source, file)
    if os.path.isdir(file_path):
        shutil.copytree(file_path, os.path.join(args.destination, file))
    elif os.path.isfile(file_path):
        shutil.copy(file_path, args.destination)

print(f'Copying files from {args.source} to {args.destination}')

