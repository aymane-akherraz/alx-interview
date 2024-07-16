#!/usr/bin/python3
""" Reads stdin line by line and computes metrics """
import sys
import re


def print_metrics():
    """ Print metrics to stdout """
    print('File size: {}'.format(file_size))
    sorted_keys = sorted(my_dict.keys())
    for k in sorted_keys:
        print('{}: {}'.format(k, my_dict[k]))


my_dict = {}
file_size = 0
i = 0
pattern = (
    r"([0-9]{1,3}\.){3}[0-9]{1,3}"
    r"\s-\s"
    r"\["
    r"[0-9]{4}-[0-9]{2}-[0-9]{2}"
    r"\s"
    r"([0-9]{2}:){2}[0-9]{2}"
    r"\.[0-9]{6}"
    r"\]"
    r'\s"GET\s/projects/260\sHTTP/1\.1"'
    r"\s"
    r"(?P<status_code>200|301|400|401|403|404|405|500)"
    r"\s"
    r"(?P<file_size>[0-9]{1,4})"
)
try:
    for line in sys.stdin:
        line = line.strip('\n')
        matched = re.fullmatch(pattern, line)
        if matched:
            file_size += int(matched.group('file_size'))
            status_code = int(matched.group('status_code'))
            if status_code in my_dict:
                my_dict[status_code] += 1
            else:
                my_dict[status_code] = 1
            if i < 9:
                i += 1
            else:
                print_metrics()
                i = 0
except KeyboardInterrupt:
    print_metrics()
    raise
