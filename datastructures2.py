#Creating an empty list called my_list
my_list = []
#Append the following elements to my_list: 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
#check list 
print(f"List for step 2 is given as{my_list}")
#Insert the value 15 at the second position in the list.
my_list[1] = 15
#check list 
print(f"List for step 3 is given as{my_list}")
#Extend my_list with another list: [50, 60, 70].
my_list2 = [50,60,70]
my_list.extend(my_list2)
#check list 
print(f"List for step 4 is given as{my_list}")
#Remove the last element from my_list.
del my_list[6]
#check list 
print(f"List for step 5 is given as{my_list}")
#Sort my_list in ascending order.
my_list.sort()
print(my_list)
#check list 
print(f"List for step 6 is given as{my_list}")
#Find and print the index of the value 30 in my_list.
index = my_list.index(30)
print(f"The value 30 is index no. {index}")