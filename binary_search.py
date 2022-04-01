# ToDo: Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. Write a function to help Bob locate the card.

tests = {
    'test': [{'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 7}, 'output': 3},
             {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 1}, 'output': 6},
             {'input': {'cards': [4, 2, 1, -1], 'query': 4}, 'output': 0},
             {'input': {'cards': [3, -1, -9, -127], 'query': -127}, 'output': 3},
             {'input': {'cards': [6], 'query': 6}, 'output': 0},
             {'input': {'cards': [9, 7, 5, 2, -9], 'query': 4}, 'output': -1},
             {'input': {'cards': [], 'query': 7}, 'output': -1},
             {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 3},
              'output': 7},
             {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
                        'query': 6},
              'output': 2}]
}


def binary_search(cards, query):
    start = 0
    end = len(cards) - 1

    def check_left(pos):
        if pos - 1 > 0 and cards[pos - 1] == query:
            return True
        else:
            return False

    while start <= end:
        pos = (start + end) // 2
        print(f'start: {start}, end: {end}, pos: {pos},num: {cards[pos]} query: {query}')
        if cards[pos] == query:
            while check_left(pos):
                pos -= 1
            return pos

        elif cards[pos] < query:
            end = pos - 1
        else:
            start = pos + 1
    return -1


for one_test in tests['test']:
    print(f"input- cards: {one_test['input']['cards']} , query: {one_test['input']['query']} \nExp output: {one_test['output']}")
    result = False
    if one_test['output'] == binary_search(one_test['input']['cards'], one_test['input']['query']):
        result = True
    print(f"result = {result}\n")

