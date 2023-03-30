#find dublicates 

list1 = set(input("Input your first list of elements: ").split())
list2 = set(input("Input your second list of elements: ").split())
list3 = set(input("Input your third list of elements: ").split())

dublicates = list1 & list2 & list3
print("Your dublicates: " + str(dublicates))