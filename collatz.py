# This is an a simple implementation of the Collatz conjecture
# Inspiration can be found here: https://en.wikipedia.org/wiki/Collatz_conjecture
# And this PWL talk: https://www.youtube.com/watch?v=OyfBQmvr2Hc
import argparse

def calculate_sequence(input):
    while input is not 1:
        if is_even(input):
            input = input / 2
        elif is_odd(input):
            input = (3 * input) + 1
        print "Next value in sequence is {}".format(input)
    print "Sequence terminated at 1"

def is_even(i):
    return i % 2 == 0

def is_odd(i):
    return i % 2 == 1

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default=2)
    args = parser.parse_args()

    calculate_sequence(int(args.input))
