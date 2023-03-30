# count elements 

n = int(input("Input count of elements: "))
elements = []
for i in range(n):
    element = input("Input element " + str(i+1) + ": ")
    elements.append(element)

searchElement = input("Input your element for counting: ")
count = elements.count(searchElement)
print("Count of elements " + str(searchElement) + ": " + str(count) + ".")