import re
from re import Pattern


def is_valid_min_max_password(entry: str, regex: Pattern) -> bool:
    """
    Uses the passed in regex pattern to get the data from the entry and validates that the character
    does not appear more than the max or less than the min amount according to the entry details.
    :param entry:
    :param regex:
    :return:
    """
    match = regex.match(entry)

    if not match:
        return False

    min_count = int(match.group('min'))
    max_count = int(match.group('max'))
    character = match.group('character')
    password = match.group('password')
    character_count = password.count(character)

    return min_count <= character_count <= max_count


def is_valid_position_password(entry: str, regex: Pattern) -> bool:
    """
    Uses the passed in regex pattern to get the data from the entry and validates that the character
    is found in one of the index positions. Returns false if it is found in both positions.
    :param entry:
    :param regex:
    :return:
    """
    match = regex.match(entry)

    if not match:
        return False

    first_index = int(match.group('min')) - 1
    second_index = int(match.group('max')) - 1
    character = match.group('character')
    password = match.group('password')

    check_first = password[first_index]
    check_second = password[second_index]

    return check_first != check_second and (check_first == character or check_second == character)


if __name__ == "__main__":
    password_re = re.compile(r'(?P<min>\d+)-(?P<max>\d+) (?P<character>\S): (?P<password>\S+)')
    valid_min_max_passwords = 0
    valid_position_passwords = 0

    with open('input.txt', 'r') as f:
        for line in f:
            if is_valid_min_max_password(line, password_re):
                valid_min_max_passwords += 1
            if is_valid_position_password(line, password_re):
                valid_position_passwords += 1

    print('Valid min/max passwords: ', valid_min_max_passwords)
    print('Valid position passwords: ', valid_position_passwords)
