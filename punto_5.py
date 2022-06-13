def consecutive(list,s_list):
    for i in range(len(list)):
        for j in range(len(s_list)):
            if (list[i] == s_list[j] and list[i + 1] == s_list[j + 1]):
                condition = "True"
                break

            else:
                condition = "False"
            return condition
#print("Select the first consecutive number")
#num1 = int(input())
#print("Select the second consecutive number")
#num2 = int(input())
#consecutive_numbers = []
#consecutive_numbers.append(num1,num2)
#list_numbers = []
#print("Add a number:")
#num = int(input())
#list_numbers.append(num)
#print("Do you want to add another number?\n1.Ye\n2.No")
#answer = int(input())
#while answer == 1:
#    list_numbers = []
#    print("Add a number:")
#    num = int(input())
#    list_numbers.append(num)
#    print("Do you want to add another number?\n1.Yes\n2.No")
#    answer = int(input())
#print(consecutive(consecutive_numbers,list_numbers))