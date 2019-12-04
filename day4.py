import sys

def meets_criteria_part1(value):
    numeral_array = list(str(value))
    if len(numeral_array) != 6:
        return False
    
    repeat_exists = False
    prev_val = 0
    for string_val in numeral_array:
        int_val = int(string_val)
        if int_val < prev_val: return False
        if int_val == prev_val: repeat_exists = True
        prev_val = int_val

    return repeat_exists

def meets_criteria_part2(value):
    numeral_array = list(str(value))
    if len(numeral_array) != 6:
        return False

    repeat_clusters = []
    current_repeat_cluster = []

    prev_val = 0
    for string_val in numeral_array:
        int_val = int(string_val)
        if int_val < prev_val: return False
        elif int_val == prev_val:
            if (len(current_repeat_cluster) > 0):
                current_repeat_cluster.append(int_val)
            else:
                current_repeat_cluster.append(int_val)
                current_repeat_cluster.append(int_val)
        elif (len(current_repeat_cluster) > 0):
            repeat_clusters.append(current_repeat_cluster.copy())
            current_repeat_cluster = []
        prev_val = int_val

    if (len(current_repeat_cluster) > 0):
        repeat_clusters.append(current_repeat_cluster.copy())
        current_repeat_cluster = []

    repeat_exists = False
    for cluster in repeat_clusters:
        if len(cluster) == 2: repeat_exists = True

    return repeat_exists
    

def valid_values_in_range_part1(min_val, max_val):
    valid_values = [x for x in range(min_val, max_val) if meets_criteria_part1(x)]
    return len(valid_values)


def valid_values_in_range_part2(min_val, max_val):
    valid_values = [x for x in range(min_val, max_val) if meets_criteria_part2(x)]
    return len(valid_values)

if __name__ == '__main__':
    print("Valid values in range in part 1: {0}".format(valid_values_in_range_part1(int(sys.argv[1]), int(sys.argv[2]))))
    print("Valid values in range in part 2: {0}".format(valid_values_in_range_part2(int(sys.argv[1]), int(sys.argv[2]))))
