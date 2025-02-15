import random as rng
import os

from rich import print

filepath = 'data.txt'
max_val = 10
min_val = 2

if not os.path.isfile(filepath):
    print(f'File {filepath} does not exist.')
    exit()

with open(filepath, 'r') as file:
    objectives = [line.strip() for line in file]

print('Parsing progress...')
progress = int(objectives[-1])
objectives = objectives[:-1]

rng.shuffle(objectives)
results = [(title, rng.randint(min_val, max_val)) for title in objectives]

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
progress = min(actual_points + progress, 100)

print(f"""
Total Points: {total}
Reduction: {reduction}
Actual Points: {actual_points}
""")
print('|' + '█' * progress + ' ' * (100 - progress) + f'| {progress}/100')

with open(filepath, 'w') as file:
    for title, value in results:
        file.write(f'{title}\n')
    file.write(f'{progress}\n')

