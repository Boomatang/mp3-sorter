import os
import shutil
import sys
from pathlib import Path as P

def run(source: str, destination: str):
    print(f"Working on file in {source} and moving them to {destination}")
    files = get_files(source)

    for file in files:
        work(file, source, destination)

def get_files(source: str):
    for dir_path, dirs, file_name in os.walk(source):
        for name in file_name:
            yield P(dir_path, name)


def create_parent_folders(root):
    if root.is_dir():
        return
    else:
        os.makedirs(str(root))


def copy_file(source: P, destination: str, file_name: str):
    print(f"copy '{source}' to '{destination}' with new name of '{file_name}' ")

    new_file = P(destination, file_name)
    if new_file.exists():
        raise FileExistsError(f"File already exists: {new_file}")
    create_parent_folders(new_file.parent)

    shutil.copyfile(str(source), str(new_file))

    return new_file

def remove_file(source: P):
    print(f'remove the file {source}')
    os.remove(str(source))

def get_new_filename(source):
    return source.name

def work(source: P, root: str, destination: str):

    new_filename = get_new_filename(source)
    dest = get_save_destination(source, root, destination)
    new_file: P
    try:
        new_file = copy_file(source, dest, new_filename)
    except FileExistsError as err:
        print(err)
        print("Exiting")
        sys.exit(1)

    if new_file.exists():
        remove_file(source)

def get_save_destination(source: P, root: str, destination: str):
    root = P(root)
    destination = P(destination)
    name = str(source.parent)
    dest = name.replace(root.parent.name, destination.parent.name)
    return dest