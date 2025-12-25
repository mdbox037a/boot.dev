def verify_tsp(paths, dist, actual_path):
    total = 0
    for city in range(len(actual_path) - 1):
        total += paths[actual_path[city]][actual_path[city + 1]]
    if total < dist:
        return True
    else:
        return False
