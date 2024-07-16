#!/usr/bin/python3
""" Reads stdin line by line and computes metrics """
import sys


def print_metrics():
    """ Print metrics to stdout """
    print('File size: {}'.format(total_file_size))
    sorted_keys = sorted(my_dict.keys())
    for k in sorted_keys:
        if my_dict[k] > 0:
            print('{}: {}'.format(k, my_dict[k]))


my_dict = {str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}
total_file_size = 0
i = 0
try:
    for line in sys.stdin:
        line = line.strip('\n')
        total_file_size += int(line.split()[-1])
        status_code = line.split()[-2]
        if status_code in my_dict.keys():
            my_dict[status_code] += 1
        i += 1
        if i == 10:
            print_metrics()
            i = 0
except KeyboardInterrupt:
    print_metrics()
    raise
print_metrics()
