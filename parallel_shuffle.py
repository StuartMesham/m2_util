import argparse
from sklearn.utils import shuffle

parser = argparse.ArgumentParser()
parser.add_argument('--f1', help='Path to file 1', required=True)
parser.add_argument('--f2', help='Path to file 2', required=True)
args = parser.parse_args()

input_file_names = [args.f1, args.f2]

output_file_names = []
for input_file_name in input_file_names:
    if input_file_name.endswith('.train.txt'):
        output_file_names.append(f'{input_file_name[:-10]}.shuffled.train.txt')
    elif input_file_name.endswith('.dev.txt'):
        output_file_names.append(f'{input_file_name[:-8]}.shuffled.dev.txt')

input_files = [open(input_file_name, 'r') for input_file_name in input_file_names]
input_files_lines = [input_file.readlines() for input_file in input_files]
for input_file in input_files:
    input_file.close()

output_files_lines = shuffle(*input_files_lines)
output_files = [open(output_file_name, 'w') for output_file_name in output_file_names]
for output_file_lines, output_file in zip(output_files_lines, output_files):
    output_file.writelines(output_file_lines)
    output_file.close()
