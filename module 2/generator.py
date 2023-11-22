from typing import Generator

def generator_cubes(n: int) -> Generator:
    for j in range(1, n + 1):
        yield j ** 3

numbers_cubes = []

for i in (generator_cubes(10)):
    numbers_cubes.append(i)

print(numbers_cubes)