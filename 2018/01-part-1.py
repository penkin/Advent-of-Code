with open('01.input.txt', 'r') as f:
    print(sum([int(frequency) for frequency in f.readlines()]))
