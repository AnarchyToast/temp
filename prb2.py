def diff_check(sample, target):
    if(sample != target):
        return(int(target) - int(sample))
    else:
        return(0)

temp_input = input()
units = temp_input.split()

diff = []

for i in range(0, len(units)):
    i = int(i)
    if i == 0:
        diff.append(diff_check(units[i], 1))
    elif i == 1:
        diff.append(diff_check(units[i], 1))
    elif i == 5:
        diff.append(diff_check(units[i], 8))
    else:
        diff.append(diff_check(units[i], 2))

for i in range(0, len(diff)):
    print(diff[i], end = " ")