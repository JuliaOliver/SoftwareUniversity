cards = input().split()
shuffles_count = int(input())
middle_length = len(cards) // 2

for i in range(shuffles_count):
    res = []

    for index in range(middle_length):
        first_card = cards[index]
        current_index_second_deck = index + middle_length
        second_card = cards[current_index_second_deck]

        res.append(first_card)
        res.append(second_card)

    cards = res

print(cards)
