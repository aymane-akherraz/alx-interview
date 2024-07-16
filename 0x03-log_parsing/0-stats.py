#!/usr/bin/python3
""" Reads stdin line by line and computes metrics """
import sys


def print_metrics(f_size, st_dict):
    """ Print metrics to stdout """
    print('File size: {}'.format(f_size))
    sorted_keys = sorted(st_dict.keys())
    for k in sorted_keys:
        if st_dict[k] > 0:
            print('{}: {}'.format(k, st_dict[k]))


my_dict = {str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}
total_file_size = 0
i = 0
try:
    for line in sys.stdin:
        line = line.strip('\n')
        try:
            file_size = int(line.split()[-1])
            total_file_size += file_size
            status_code = line.split()[-2]
            if status_code in my_dict.keys():
                my_dict[status_code] += 1
        except Exception:
            pass
        i += 1
        if i == 10:
            print_metrics(total_file_size, my_dict)
            i = 0
except KeyboardInterrupt:
    print_metrics(total_file_size, my_dict)
    raise
print_metrics(total_file_size, my_dict)
