import argparse
from benchlex.alexpy import AlexPy

def load_args():
    parser = argparse.ArgumentParser(description='Benchmark for ALEX')
    parser.add_argument('--keys_file', help='keys file', required=True)

    args = parser.parse_args()

    return args


def main() -> int:
    args = load_args()

    alex = AlexPy()
    alex.bench()

    return 0


if __name__ == "__main__":
    main()
