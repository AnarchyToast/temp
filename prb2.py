def diff_check(sample, target):
    if(sample != target):
        return(target - sample)
    else:
        return(0)

temp_input = input()
input = temp_input.split()

diff = []

for i in input:
    if i == 0:
       diff.append(diff_check(int(input[i]), 1))
    elif i == 1:
        diff.append(diff_check(int(input[i]), 1))
        



print(diff)