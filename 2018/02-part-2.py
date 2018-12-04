import collections


def get_inputs(file_name):
    with open(file_name, 'r') as f:
        return [line.strip() for line in f.readlines()]


def get_matched_ids(inputs):
    matched = []

    for id1 in inputs:
        for id2 in inputs:
            chars = []

            for i in range(len(id2)):
                if id2[i] == id1[i]:
                    chars.append(id2[i])

            if len(chars) + 1 == len(id1):
                id = ''.join(chars)
                if id not in matched:
                    matched.append(id)

    return matched


print(get_matched_ids(get_inputs('02.input.txt')))
