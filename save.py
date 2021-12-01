import argparse
import subprocess

parser = argparse.ArgumentParser(description='Read input')
parser.add_argument('day',type=int)
parser.add_argument('--year', type=int, default=2021)
args = parser.parse_args()



cmd = 'curl https://adventofcode.com/{}/day/{}/input --cookie "session=53616c7465645f5f64efa9c12a0edf13058100b6031b61cd0d17e044f49f1423be2c72b8d0d5938eabe7c6fa70bd0e1a" -o "{}.in"'.format(
    args.year, args.day, args.day)

output = subprocess.check_output(cmd, shell=True)
# print(output)
