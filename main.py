import os
import importlib
import argparse


def load_data(path):
    """Loads the data from a file called 'input.txt' located in the solution folder"""
    input_path = os.path.join(path, "input.txt")

    with open(input_path) as f:
        data = f.read()
    return data


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Advent of Code", description="Runs an advent of code solution"
    )
    parser.add_argument("year", type=int)
    parser.add_argument("month", type=int)

    args = parser.parse_args()

    relative_solution_path = f"{args.year}/{args.month:02}"
    folder_path = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(folder_path, relative_solution_path)

    data = load_data(path)

    import_path = f"{args.year}.{args.month:02}"
    i = importlib.import_module(import_path)
    i.solution(data)
