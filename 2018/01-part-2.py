def get_inputs(fileName):
    with open(fileName, 'r') as f:
        return [int(frequency) for frequency in f.readlines()]


def get_calibration_frequency(inputs):
    frequency = 0
    past_frequencies = set()
    past_frequencies.add(frequency)

    while True:
        for change in inputs:
            frequency += change

            if frequency in past_frequencies:
                return frequency

            past_frequencies.add(frequency)


inputs = get_inputs('01.input.txt')
print(get_calibration_frequency(inputs))
