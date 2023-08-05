input1 = input()
numbers = input1.split()

if (len(numbers) != 2):
    print("wrong number of inputs :(")
    exit()

num_cards = int(numbers[0])
target = int(numbers[1])

if(num_cards > 100 or num_cards < 3):
    exit()

if(target > 300000 or target < 10):
    exit()

#print("num_cards = " + num_cards + " target = " + target)

input2 = input()
cards = input2.split()

if (len(cards) != num_cards):
    print("too many cards :(")
    exit()
    
#print(cards)

sum = []

for i in range(0, len(cards)):
    for j in range(0, i):
        for k in range(0, j):
            temp = int(cards[i]) + int(cards[j]) + int(cards[k])
            if (temp <= target):
                sum.append(temp)

sum_nova = []
for i in range(0, len(sum)):
    sum_nova.append(sum[i] - target)

max = sum_nova[0]
c_idx = 0

for i in range(0, len(sum_nova)):
    if(sum_nova[i] > max):
        max = sum_nova[i]
        c_idx = i

print(sum[c_idx])