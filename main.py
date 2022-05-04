#!/usr/bin/python3
import sys
from os.path import exists


def my_process(input_stream):
    # Your processing will be here
    for line in input_stream:
        print(line, end="")


def main():
    if not sys.stdin.isatty():
        input_stream = sys.stdin

    else:
        if len(sys.argv) > 1:
            if exists(sys.argv[1]):
                try:
                    input_filename = sys.argv[1]
                    input_stream = open(input_filename, 'r')
                except Exception as e:
                    sys.stderr.write(f"{str(e)}\n")
                    sys.exit(1)
            else:
                sys.stderr.write("input file not found\n")
                sys.exit(1)
        else:
            sys.stderr.write(
                "input file is required. For example `./main.py input_file`. or pipe\n")
            sys.exit(1)

    try:
        my_process(input_stream)
    except Exception as e:
        sys.stderr.write(f"Only ASCII input is supported\n")
        sys.stderr.write(f"{str(e)}\n")
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()
