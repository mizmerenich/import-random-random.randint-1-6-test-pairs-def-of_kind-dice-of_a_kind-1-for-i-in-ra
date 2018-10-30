from difflib import SequenceMatcher
with open('file1.txt') as file_1,open('file2.txt') as file_2:
    file1_data = file_1.read()
    file2_data = file_2.read()
    similarity_ratio = SequenceMatcher(None,file1_data,file2_data).ratio()
    print (similarity_ratio)  #plagiarism detected
import random
random.randint(1,6)


#test pairs
def of_kind(dice):
    of_a_kind = 1
    for i in range(5):
        current = i + 1
        count = 1
        while count != -1:
            if current < 5:
                if dice[current] == dice[i]:
                    current = current + 1
                    count = count + 1
                    if count > of_a_kind:
                        of_a_kind = count
                else:
                    count = -1
            else:
                count = -1
#5 of a kind
    if of_a_kind == 5:
        print("Five of a Kind: 50 points.")
        return 50
#3 and 4 of a kind/full house    
    elif of_a_kind == 4 or of_a_kind == 3:
        total = 0
        for index in range(5):
            total = total + int(dice[index])
        if of_a_kind == 4:
            total = total + 10
            print("Four of a Kind: " + str(total) + " points.")
            return total
        else:
            no_duplicates = []
            for index in range(5):
                if dice[index] not in no_duplicates:
                    no_duplicates.append(dice[index])
            if len(no_duplicates) == 2:
                print("Full House: 25 points.")
                return 25
            else:
                total = total + 5
                print("Three of a Kind: " + str(total) + " points.")
                return total
    else:
        return 0
#small and 2 larger straight(added an extra to fill larger point gap)
def straight(dice):
    straight = 1
    for index in range(len(dice)):
        current = index
        count = 1
        while(current != -1):
            if current + 1 < len(dice):
                if int(dice[current + 1]) - int(dice[current]) == 1:
                    current = current + 1
                    count = count + 1
                elif int(dice[current + 1]) == int(dice[current]):
                    current = current + 1
                else:
                    current = -1
            else:
                current = -1
            if count > straight:
                straight = count
    if straight == 3:
        print("Small Straight: 30 points.")
        return 30
    elif straight == 4:
        print("Large Straight: 40 points.")
        return 40
    elif straight == 5:
        print("Large Straight: 50 points.")
        return 40
    else:
        return 0

def patterns(dice):
    score = of_kind(dice)
    if score == 0:
        score = straight(dice)
    if score == 0:
        print("No Pattern: 0 points.")
    return score

#program execution portion(begin with main, call main at end)    
def main():
    total_score = 0
    for i in range(1,6):
        print("Turn " + str(i) + "!")
        dice = []
        for i in range(5):
            dice.append(random.randint(1,6))
        print("Roll 1: ", end ="")
        for i in range(len(dice)):
            if i < len(dice) - 1:
                print(dice[i], end =" ")
            else:
                print(dice[i])
            
        keep = input("Which numbers (in position 0-4) would you like to keep? ")
        keep = keep.split(',')
        print("Roll 2: ", end ="")
        for i in range(5):
            if str(i) not in keep:  #works for 0-4 range
                dice[i] = random.randint(1,6)    #works for 0-4 range
            if i < len(dice) - 1:
                print(dice[i], end =" ")
            else:
                print(dice[i])
        dice.sort()
        print (dice[0:5])
        score = patterns(dice)
        total_score = total_score + score
    print("Final score: " + str(total_score) + " points.")
main()
