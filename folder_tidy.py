import os

def run(source: str):
    counter = 1

    while counter > 0:
        for dir, folders, files in os.walk(source):
            if len(folders) == 0 and len(files) == 0:
                print(f"Removing: {dir}")
                os.removedirs(dir)
                counter += 1
        counter -= 1

    print("Folders tidied")