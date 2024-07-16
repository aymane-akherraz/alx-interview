#!/usr/bin/python3
""" Reads stdin line by line and computes metrics """
import sys
import re


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
        try:
            file_size = int(matched.group('file_size'))
            total_file_size += file_size
            status_code = matched.group('status_code')
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
