import main
from pathlib import Path as P

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
    current = P(entry[0])
    print(f"Mock work in {current.name}")
    main.run(entry[0], entry[1])
    print()

