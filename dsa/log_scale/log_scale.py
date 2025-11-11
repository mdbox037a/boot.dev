import math


def log_scale(data, base):
    log_list = []
    for d in data:
        log_list.append(math.log(d, base))
    return log_list
