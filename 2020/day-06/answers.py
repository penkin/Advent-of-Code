import re


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        text = f.read()

    yes_answers = 0
    yes_consensus = 0

    for group in re.findall(r'(?P<answers>(?:\S+[ \n]?)+)(?=(?:\n){2}|)', text):
        # Get total yes answers for the group.
        yes_answers += len(set(list(group.replace('\n', ''))))

        # Here we want to split the groups answers and get consensus answers using the
        # intersection method of sets.
        answers = group.split('\n')
        consensus_answer = answers[0]
        for answer in answers[:-1]:
            consensus_answer = set(consensus_answer).intersection(answer)

        yes_consensus += len(set(consensus_answer))

    print('Yes', yes_answers)
    print('Yes consensus', yes_consensus)
