import argparse
from benchlex.alexpy import AlexPy


def main() -> int:
    alex = AlexPy()
    alex.bench()
    return 0


if __name__ == "__main__":
    main()
