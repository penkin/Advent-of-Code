def get_inputs(file_name):
    with open(file_name, 'r') as f:
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


print(get_calibration_frequency(get_inputs('01.input.txt')))
