from script import run

data = [
    ('source1', 'dest1'),
    ('source2', 'dest2'),
    ('source3', 'dest3'),
        ]

for entry in data:
    run(entry[0], entry[1])
