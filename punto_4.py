import random
bingo_numbers = [2,9,7,14,16]
def bingo_check(list,s_list):
    for i in list:
        for j in s_list:
            if (i == j):
                ticket = "Winner"
                break
            else:
                ticket = "Loser"
    return ticket
bingo_list = []
j = 0
while j < 10:
    num = random.randint(0,26)
    bingo_list.append(num)
    j += 1
print(bingo_check(bingo_numbers,bingo_list))

