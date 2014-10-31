def value(card):
    c = card[0]
    if c.isdigit():
        return int(card[0])
    values = ['T', 'J', 'Q', 'K', 'A']
    return 10 + values.index(c)


def suit(card):
    return card[-1]


def update_hand(dst, src):
    del dst[:]
    for card in src:
        dst.append(card)


def is_flush(hand):
    p = suit(hand[0])
    for card in hand[1:]:
        if suit(card) != p:
            return False
    return True


def is_straight(hand):
    v = value(hand[0])
    for card in hand[1:]:
        x = value(card)
        if x + 1 != v:
            return False
        v = x
    return True


def is_straight_flush(hand):
    return is_straight(hand) and is_flush(hand)


def is_royal_flush(hand):
    top_val = value(hand[0])
    return top_val == 14 and is_straight_flush(hand)


def is_pair(hand):
    values = [value(card) for card in hand]
    for i, v1 in enumerate(values):
        for j, v2 in enumerate(values[i+1:]):
            if v1 == v2:
                indexes = [i, j+i+1,]
                for x in range(5):
                    if not x in indexes:
                        indexes.append(x)
                        
                new_hand = [hand[index] for index in indexes]        
                update_hand(hand, new_hand)
                
                return True
    return False


def is_3oak(hand):
    values = [value(card) for card in hand]
    
    for i, v1 in enumerate(values):
        
        for j, v2 in enumerate(values):
            if j <= i: continue
            
            for k, v3 in enumerate(values):
                if k <= j: continue
                
                if v1 == v2 == v3:
                    indexes = [i, j, k,]
                    for x in range(5):
                        if not x in indexes:
                            indexes.append(x)

                    new_hand = [hand[index] for index in indexes]        
                    update_hand(hand, new_hand)
                    
                    return True
    return False


def is_4oak(hand):
    values = [value(card) for card in hand]
    values.sort()

    if values[1] == values[3]:
        if values[0] == values[1]:
            return True
        if values[1] == values[4]:
            hand[0], hand[4] = hand[4], hand[0]
            return True
    
    return False


def is_full_house(hand):
    if is_3oak(hand):
        if value(hand[-1]) == value(hand[-2]):
            return True    
    return False


def is_two_pair(hand):
    if is_pair(hand):
        cut_values = [value(card) for card in hand[2:]]
        if cut_values[1] == cut_values[2]:
            hand[2], hand[4] = hand[4], hand[2]
            cut_values[0], cut_values[2] = cut_values[2], cut_values[0]
        elif cut_values[0] == cut_values[2]:
            hand[3], hand[4] = hand[4], hand[3]
            cut_values[1], cut_values[2] = cut_values[2], cut_values[1]
        return cut_values[0] == cut_values[1]
        
    return False


def evaluate_hand(hand):
    if is_royal_flush(hand):     return 0
    if is_straight_flush(hand):  return 1
    if is_4oak(hand):            return 2
    if is_full_house(hand):      return 3
    if is_flush(hand):           return 4
    if is_straight(hand):        return 5
    if is_3oak(hand):            return 6
    if is_two_pair(hand):        return 7
    if is_pair(hand):            return 8

    return 9
    

def compare_eq_evaluation(first, second):
    for x, y, in zip(first, second):
        a, b = value(x), value(y)
        if a > b:
            return True
        if a < b:
            return False
    return False


def is_win(winner, looser):
    winner.sort(key=value, reverse=True)
    looser.sort(key=value, reverse=True)

    ev1 = evaluate_hand(winner)
    ev2 = evaluate_hand(looser)

    if ev1 < ev2:
        return True
    if ev1 > ev2:
        return False
    
    return compare_eq_evaluation(winner, looser)
    

def hands():
    with open('p054_poker.txt', 'r') as ifs:
        for line in ifs:
            cards = line.split()
            yield (cards[:5], cards[5:])


def calc():
    ans = 0
    for hand in hands():
        if is_win(hand[0], hand[1]):
            ans += 1
    return ans
        

print(calc())
