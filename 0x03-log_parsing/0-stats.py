#!/usr/bin/python3
""" Reads stdin line by line and computes metrics """
import sys


def print_metrics(f_size, status_dict):
    """ Print metrics to stdout """
    print('File size: {}'.format(f_size))
    sorted_keys = sorted(status_dict.keys())
    for k in sorted_keys:
        if status_dict[k] > 0:
            print('{}: {}'.format(k, status_dict[k]))


my_dict = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
file_size = 0
i = 0
try:
    for line in sys.stdin:
        line = line.strip('\n')
        splited = line.split()
        if len(splited) == 7:
            file_size += int(splited[-1])
            status_code = int(splited[-2])
            if status_code in my_dict:
                my_dict[status_code] += 1
            i += 1
            if i % 10 == 0:
                print_metrics(file_size, my_dict)
        else:
            continue
except KeyboardInterrupt:
    print_metrics(file_size, my_dict)

