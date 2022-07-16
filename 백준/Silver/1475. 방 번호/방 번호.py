n = input()

card = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0}

for i in range(len(n)):
    if n[i] == '6' or n[i] == '9':
        card['6'] += 1
    else:
        card[n[i]] += 1

if card['6'] % 2 == 0:
    card['6'] = card['6'] // 2
else:
    card['6'] = card['6'] // 2 + 1

print(max(card.values()))