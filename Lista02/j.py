entrada = input()

cards = entrada.split(" ")
integer_cards = []

for card in cards:
    integer_cards.append(int(card))

integer_cards.sort(reverse = True)

dict_cards = {}
for card in integer_cards:
    if (dict_cards.get(card) != None):
        dict_cards[card] += 1
    else:
        dict_cards.update({card: 1})

t1 = 0
t2 = 0
for card in dict_cards:
    if dict_cards[card] == 2:
        t1 = max(t1, card)
    elif dict_cards[card] >= 3:
        t2 = max(t2, card)

if t1*2 > t2*3:
    print(sum(integer_cards) - t1*2)
else:
    print(sum(integer_cards) - t2*3)