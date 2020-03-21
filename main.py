import script
import folder_tidy

data = [
    ('path/to/exiting', 'path/to/save')
]

def run(root, dest):
    print(f"Working on files in: {root}")
    print(f"New files will be saved in {dest}")
    script.run(root, dest)
    folder_tidy.run(root)
    print("Completed")

if __name__ == '__main__':
    for entry in data:
        run(entry[0], entry[1])