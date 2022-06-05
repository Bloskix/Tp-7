list_num = []
print("Add a number:")
num = int(input())
list_num.append(num)
while len(list_num) < 3:
    print("Add a number:")
    num = int(input())
    list_num.append(num)
list_num.sort(reverse = True)
if list_num:

else:
    for i in range(len(list_num)):
        while len(list_num) < 2:
            sum += list_num[i] - list_num[i+1]

