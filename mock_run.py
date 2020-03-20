from script import run
from folder_tidy import folder_tidy

prefix_input = 'playground/input/'
prefix_result = 'playground/result/'
data = [
    (prefix_input + 'bad01', prefix_result + 'bad01'),
    (prefix_input + 'bad02', prefix_result + 'bad02'),
    (prefix_input + 'bad03', prefix_result + 'bad03'),
    (prefix_input + 'good01', prefix_result + 'good01'),
    (prefix_input + 'good02', prefix_result + 'good02'),
        ]

for entry in data:
    print(f"Mock work in {entry[0]}")
    run(entry[0], entry[1])
    print(f"Removing empty folders from {entry[0]}")
    folder_tidy(entry[0])
    print()

