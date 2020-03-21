import os
import shutil
import sys
from pathlib import Path as P
from eyed3 import id3

EXPECTED = 'expected'
REWORK = 'rework'

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
    if not  is_mp3(source):
        return None

    tag = id3.TagFile(str(source))
    if tag.tag is None:
        return None

    title = tag.tag.title
    track_num = str(tag.tag.track_num[0]).zfill(2)

    return f"{track_num} - {title}.mp3"


def file_does_exist(dest, new_filename):
    file = P(dest, new_filename)
    if file.exists():
        return True
    else:
        return False


def get_duplicate_album_dest(dest: P):
    counter = 1
    parent = str(dest.parent)
    name = dest.name
    new_dest = None

    while new_dest is None:
        temp_name = f"duplicate({str(counter).zfill(2)}) - {name}"
        temp_dest = P(parent, temp_name)
        if temp_dest.exists():
            counter += 1
        else:
            new_dest = temp_dest

    return new_dest


def work(source: P, root: str, destination: str):
    rework = False
    new_filename = get_new_filename(source)

    if new_filename is None:
        new_filename = source.name
        rework = True

    dest = get_save_destination(source, root, destination, rework)
    new_file: P
    try:
        if file_does_exist(dest, new_filename):
            dest = get_duplicate_album_dest(dest)
        new_file = copy_file(source, dest, new_filename)
    except FileExistsError as err:
        print(err)
        print("Exiting")
        sys.exit(1)

    if new_file.exists():
        remove_file(source)

def get_save_destination(source: P, root: str, destination: str, rework: bool):

    if rework:
        return rework_required(source, root, destination)

    if is_mp3(source):
        section = EXPECTED

        tag = id3.TagFile(str(source))

        if tag.tag is None:
            return rework_required(source, root, destination)

        artist = tag.tag.artist
        album = tag.tag.album

        if artist is None or album is None:
            return rework_required(source, root, destination)

        dest = P(destination, section, artist, album)
        return dest

    return rework_required(source, root, destination)


def is_mp3(source: P):
    if source.name.endswith('.mp3'):
        return True
    else:
        return False

def rework_required(source, root, destination):
    root = P(root)
    parts = source.parts[len(root.parts):]
    parts = parts[:-1]
    dest = P(destination, REWORK, *parts)
    return dest