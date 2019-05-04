import itertools

def straight_flush(hand):
    if straight(hand) and flush(hand):
        return ['straight_flush',[max([(x-1)%13 for x in hand])+1]]
    else:
        return False

def straight(hand):
    mod_hand= [(x-1)%13 for x in hand]
    mod_hand.sort()
    if mod_hand[0] != 0:
        for i in range(0,5):
            if mod_hand[i]-mod_hand[0] != i:
                return False
        return ['straight',[max(mod_hand)+1]]
    else:
        for i in range(0,5):
            if mod_hand[i]-mod_hand[0] != i:
                break
        else:
            return ['straight',[max(mod_hand)+1]]

        mod_hand[0] = 13
        mod_hand.sort()
        for i in range(0,5):
            if mod_hand[i]-mod_hand[0] != i:
                return False
        return ['straight',[max(mod_hand)+1]]


def flush(hand):
    if all(i in range(1,14) for i in hand) or all(i in range(14,27) for i in hand) or all(i in range(27,40) for i in hand) or all(i in range(40,53) for i in hand):
        return  ['flush',hand]        
    else:
        return False

   
def pairs(hand):
    mod_hand= [(x-1)%13 for x in hand]
    count_hand = [mod_hand.count(x) for x in mod_hand]
    if 4 in count_hand:
        four = mod_hand[count_hand.index(4)]+1
        other = mod_hand[count_hand.index(1)]+1
        return ['four_of_a_kind',four,other]
    if 3 in count_hand and 2 in count_hand:
        three = mod_hand[count_hand.index(3)]+1
        two = mod_hand[count_hand.index(2)]+1
        return ['full_house',three,two]
    elif 3 in count_hand:
        three = mod_hand[count_hand.index(3)]+1
        other = [x+1 for x in mod_hand if x !=three-1]
        other.sort(reverse=True)
        return ['three_of_a_kind',three,other]
    if count_hand.count(2) ==4:
        high_pair = mod_hand[count_hand.index(2)]+1
        low_pair = [x for x in mod_hand if x != high_pair-1][count_hand.index(2)]+1
        other = mod_hand[count_hand.index(1)]+1
        if high_pair > low_pair:
            return ['two_pair',high_pair,low_pair,other]
        else:
            return ['two_pair',low_pair,high_pair,other]
    if 2 in count_hand:
        pair = mod_hand[count_hand.index(2)]+1
        other = [x+1 for x in mod_hand if x !=pair-1]
        other.sort(reverse=True)
        return ['pair',pair,other]
    return [0]

def test_hand(hand):
    hand.sort()
    if straight_flush(hand) != False:
        return straight_flush(hand)
    pairs_results = pairs(hand)
    if pairs_results[0] == 'four_of_a_kind' or pairs_results[0]== 'full_house':
        return pairs_results
    if flush(hand) != False:
        return flush(hand)
    if straight(hand) != False:
        return straight(hand)
    if len(pairs_results) > 1  :
        return pairs_results
    else:
        mod_hand= [((x-1)%13)+1 for x in hand]
        mod_hand = [14 for x in mod_hand if x == 0]
        mod_hand.sort(reverse=True)
        return ['high_card'] + [mod_hand]


def best_hand(in_hands):
    list_of_hands = ['straight_flush','four_of_a_kind','full_house','flush','straight','three_of_a_kind','two_pair','pair','high_card']
    list_of_strengths = [list_of_hands.index(x[0]) for x in in_hands]
    if list_of_strengths.count(min(list_of_strengths)) == 1:
        return in_hands[list_of_strengths.index(min(list_of_strengths))]
    else:
        same_hand = [x for x in in_hands if x[0] == list_of_hands[(min(list_of_strengths))]]
        same_hand.sort(reverse=True)
        return same_hand[0]


def winning_hand(in_hands):
    list_of_hands = ['straight_flush','four_of_a_kind','full_house','flush','straight','three_of_a_kind','two_pair','pair','high_card']
    list_of_strengths = [list_of_hands.index(x[0]) for x in in_hands]
    if list_of_strengths.count(min(list_of_strengths)) == 1:
        return [in_hands.index(in_hands[list_of_strengths.index(min(list_of_strengths))])]
    else:
        same_hand = [x for x in in_hands if x[0] == list_of_hands[(min(list_of_strengths))]]
        same_hand.sort(reverse=True)
        return [x for x,val in enumerate(in_hands) if val == same_hand[0]]


def handler(on_table_cards,player_cards):
    player_hands = [x+on_table_cards for x in player_cards]
    player_best_hands = [best_hand([test_hand(j) for j in [list(x) for x in itertools.combinations(i,5)]]) for i in player_hands]
    print(player_best_hands)
    return winning_hand(player_best_hands)







if __name__ == "__main__":
    tab = [9,11,12,13,48]
    hand1 = [2,36]
    hand2 = [14,42]
    winners = handler(tab,[hand1,hand2])
    print(winners)











