import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--argument-with-a-long-name")

args = parser.parse_args()

print(args.argument_with_a_long_name)