import math


def find_middle(ticket: str, min: int = 0, max: int = 127) -> int:
    """
    Gets the middle of the min and max as it works through the passed in
    ticket information. 'F' and 'L' represent the 1st half of the range\
    while 'B' and 'R' represent the 2nd half of a range. When there is
    no more ticket data, we simply return the min which should equal the
    max as well.
    :param ticket:
    :param min:
    :param max:
    :return:
    """
    if not len(ticket):
        return min

    char = ticket[0]
    half = ((max - min) / 2) + min

    if char in ['F', 'L']:
        return find_middle(ticket[1:], min,  math.floor(half))
    elif char in ['B', 'R']:
        return find_middle(ticket[1:], math.ceil(half), max)


def find_missing_seat(seats: list) -> int:
    """
    We find the missing seats using the difference methods of sets. We
    generate a set with the min and max of the sorted list. The seat
    in the generated difference list where the seat Id before and after
    exist is our seat, our seat is also not in the back or the front
    of the seat list.
    :param seats:
    :return:
    """
    seats.sort()
    start = seats[0]
    end = seats[-1]
    missing_seats = set(range(start, end + 1)).difference(seats)

    for missing_seat in missing_seats:
        if missing_seat + 1 in seats and missing_seat - 1 in seats:
            return missing_seat

    return -1


if __name__ == "__main__":
    seat_list = []

    with open('input.txt', 'r') as f:
        for line in f:
            row = find_middle(line[:-4], 0, 127)
            column = find_middle(line[-4:-1], 0, 7)
            seat_id = row * 8 + column
            seat_list.append(seat_id)

    seat_id = find_missing_seat(seat_list)
    print('Max seat ID', seat_list[-1])
    print('Seat ID', seat_id)
