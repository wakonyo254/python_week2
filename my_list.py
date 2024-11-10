my_list = []

#append values to the empty list
for nums in [10, 20, 30, 40]:
    my_list.append(nums)
print(my_list) 

# insert int 15 at 2nd position in list
my_list.insert(1, 15)      #use the insert method(index, numb to insert)
print(my_list)

#extend my_list with another list
my_list2 = [50, 60, 70]
my_list.extend(my_list2)
print(my_list)

#remove the last element from the list
my_list.pop()
print(my_list)

#sort my_list in an ascending order
my_list.sort()
print(my_list)

#find and print index of value 30
index = my_list.index(30)
print(index)