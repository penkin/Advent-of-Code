import collections


def get_inputs(file_name):
    with open(file_name, 'r') as f:
        return [line.strip() for line in f.readlines()]


def get_checksum(inputs):
    d_count = 0
    t_count = 0

    for line in inputs:
        d = collections.defaultdict(int)

        for c in line:
            d[c] += 1

        d_counted = False
        t_counted = False

        for c in sorted(d, key=d.get, reverse=True):
            count = d[c]

            if count == 3 and not t_counted:
                t_count += 1
                t_counted = True
            elif count == 2 and not d_counted:
                d_count += 1
                d_counted = True

            if t_counted and d_counted:
                break

    return t_count * d_count


print(get_checksum(get_inputs('02.input.txt')))
