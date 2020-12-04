def get_sum_two(expenses: list, total: int) -> (int, int):
    """
    Gets two lines in the expense list that sum up to the passed in total.
    :param expenses:
        List of int.
    :param total:
        The total that should be met.
    :return:
        Two numbers that make up the total.
    """
    for expense in expenses:
        remaining = total - expense

        if remaining in expenses:
            return expense, remaining

    return 0, 0


def get_sum_three(expenses: list, total: int) -> (int, int, int):
    """
    """
    for i, expense in enumerate(expenses):
        for _, other_expense in enumerate(expenses, i):
            remaining = total - (expense + other_expense)

            if remaining in expenses:
                return expense, other_expense, remaining

    return 0, 0, 0


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        lines = [int(line) for line in f]

        num1, num2 = get_sum_two(lines, 2020)
        print('One: ', num1 * num2)

        num1, num2, num3 = get_sum_three(lines, 2020)
        print('Two: ', num1 * num2 * num3)