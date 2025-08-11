my_list=[]
my_list.append([10, 20, 30, 40])
print(my_list)
#Insert the value 15 at the second position in the list.
my_list[0].insert(1, 15)
print(my_list)
#Extend my_list with another list: [50, 60, 70].
list_to_extend = [50, 60, 70]
my_list.extend(list_to_extend)
print(my_list)
#Remove the last element from my_list.
my_list.remove(70)
#Sort my_list in ascending order.
my_list.sort()
print(my_list)
#Find and print the index of the value 30 in my_list.
print(my_list[0].index(30))
