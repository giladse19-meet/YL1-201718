num = 0
num1 = 0
list1 = [1,2,3,4,5,6,7,8,9]
list2 = [1,3,5,6,8]
list3 = []
for num2 in range(len(list1)*len(list2)):
    for num1 in range (len(list1)):
        if list1[num] == list2[num1]:
            list3.append(list1[list2[num]])
            num = num +1
            num1 = 0 
    num1 = 0
print(list3)
##does not work
