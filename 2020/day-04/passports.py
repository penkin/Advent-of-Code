import re


class Passport:
    """
    Parses the passport data and can validate that mandatory fields exist as
    well as have the correct data.
    """
    _mandatory_fields = {
        'byr': r'^(19[2-9]\d|200[0-2])$',
        'iyr': r'^20(1\d|20)$',
        'eyr': r'^20(2\d|30)$',
        'hgt': r'^(1(?:[5-8]\d|9[0-3]))cm|(59|6\d|7[0-6])in$',
        'hcl': r'^#[0-9a-f]{6}$',
        'ecl': r'^(amb|blu|brn|gry|grn|hzl|oth)$',
        'pid': r'^\d{9}$'
    }

    def __init__(self, passport_data: str):
        """
        Parses the passport_data into a dictionary for processing.
        :param passport_data:
        """
        self._fields = {}

        for item in re.findall(r'(?P<field>\S+):(?P<value>\S+)', passport_data):
            self._fields[item[0]] = item[1]

    def has_all_mandatory_fields(self):
        """
        Checks the set difference on the mandatory field's keys and
        the data fields. If an empty set is returned then there are
        no missing mandatory fields.
        :return:
        """
        result = set(self._mandatory_fields.keys()).difference(set(self._fields.keys()))
        return len(result) == 0

    def is_valid(self):
        """
        Runs through the mandatory field's validation checks. Each
        mandatory field has a regex value to test the field value
        against. If it matches then the field is valid.
        :return:
        """
        for key, check in self._mandatory_fields.items():
            value = self._fields.get(key, '')
            if not re.match(check, value):
                return False

        return True


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        text = f.read()

    has_mandatory_fields = 0
    has_valid_data_passports = 0

    for match in re.findall(r'(?P<passport>(?:\S+:\S+[ \n]?)+)(?=(?:\n){2}|)', text):
        passport = Passport(match)

        if passport.has_all_mandatory_fields():
            has_mandatory_fields += 1

        if passport.is_valid():
            has_valid_data_passports += 1

    print('Valid mandatory fields passports: ', has_mandatory_fields)
    print('Valid data passports: ', has_valid_data_passports)
