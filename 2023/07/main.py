import re;
import time;
import numpy as np

filename = 'input.txt'

PART = 2

def get_card_map():
    card_map = {
        'A': 14,
        'K': 13,
        'Q': 12,
        'J': 11,
        'T': 10
    }
    if PART == 2:
        card_map['J'] = 1
    return card_map

def parse_line(line):
    numbers = re.search(r'(\w+) (\w+)', line)

    return [numbers.group(1), numbers.group(2)]

def map_hand_counts_to_power(hand_counts):
  if hand_counts == [5]:
    return 7
  elif hand_counts == [4, 1]:
    return 6
  elif hand_counts == [3, 2]:
    return 5
  elif hand_counts == [3, 1, 1]:
    return 4
  elif hand_counts == [2, 2, 1]:
    return 3
  elif hand_counts == [2, 1, 1, 1]:
    return 2
  elif hand_counts == [1, 1, 1, 1, 1]:
    return 1
  else:
    return 0

def sort_dict_by_value_desc(dict):
    keys = list(dict.keys())
    values = list(dict.values())
    sorted_value_index = np.argsort(values)[::-1]
    return { keys[i]: values[i] for i in sorted_value_index }

def get_hand_power(hand):
    power = 0
    cards = {}

    for index, card in enumerate(hand, 0):
        card_map = get_card_map()
        cards[card] = 1 if card not in cards else cards[card] + 1
        card_power = card_map[card] if not card.isdigit() else int(card)
        power += card_power * 100 ** (4 - index)

    cards = sort_dict_by_value_desc(cards)

    # part 2 section
    if PART == 2:
        joker_count = 0
        if 'J' in cards:
           joker_count = cards['J']
           del cards['J']

        if len(cards) > 0:
          first_key = next(iter(cards))
          cards[first_key] += joker_count
        else:
          cards['J'] = joker_count

    power += map_hand_counts_to_power([cards[x] for x in cards]) * 10000000000

    return power

def order_hands(hands):
    return sorted(hands, key=lambda x: x[1])

def count_winnings(sorted_hands):
    result = 0
    for index, hand in enumerate(sorted_hands, 1):
        bid = hand[2]
        result += int(bid) * index
    return result

with open(filename, 'r') as f:
    result = 0
    hands = []

    startT = time.time()

    for index, line in enumerate(f, 1):
        (hand, bid) = parse_line(line)
        hand_power = get_hand_power(hand)
        hands.append((hand, hand_power, bid))

    hands = order_hands(hands)

    # print(hands)

    endT = time.time()
    
    print('time:', endT - startT)
    print('result:', count_winnings(hands))