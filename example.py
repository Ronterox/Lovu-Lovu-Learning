import random as rng
import os

from rich import print

"""
Miko miko, miko pen
y apps, y juegos, y discord, y bots, y bolsa, y todo
Learn by doing
Add stuff we get about learning, ON THE FUTURE
"""

"""
Akinator like
Aks you about project
centers it and reduces size

makes priority
keeps track of it
lets you adapt

make sure to be close to closing
have everything packed in a way that doesn't mess with creativy
"""

"""
Akinator relies on four key components to function effectively:
binary search, decision trees, machine learning, and collaborative filtering
"""

FILEPATH = 'data.txt'
TARGET = 100

if not os.path.isfile(FILEPATH):
    print(f'File {FILEPATH} does not exist.')
    exit()

with open(FILEPATH, 'r') as file:
    objectives = [line.strip() for line in file]

print('Parsing progress...')
progress = int(objectives[-1])
objectives = objectives[:-1]

rng.shuffle(objectives)
results = [(title, rng.randint(1, len(objectives))) for title in objectives]

total = 0
reduction = 0
for title, value in results:
    print(f'[bold]Did you complete [purple]{title}? [blue](y/n) ', end='')
    ans = input()

    if ans != 'y':
        reduction -= value
        print(f'[bold red]{title}: {-value}')
    else:
        print(f'[bold green]{title}: {value}')

    total += value

actual_points = max(total + reduction, 0)
progress = min(actual_points + progress, TARGET)

print(f"""
Total Points: {total}
Reduction: {reduction}
Actual Points: {actual_points}
""")
print('|' + '█' * progress + ' ' * (TARGET - progress) + f'| {progress}/{TARGET}')

if progress >= TARGET:
    # NOTE: Little selenium script for pizza
    print('[bold green]You did it, [blue]pizza is on the way!')
    exit()

with open(FILEPATH, 'w') as file:
    for title, value in results:
        file.write(f'{title}\n')
    file.write(f'{progress}\n')
