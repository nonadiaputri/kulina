from collections import Counter
# my_list = [5, 4, 3, 4, 2, 1, 3, 5,3, 5, 3, 5,]
x = int(input("How many numbers do you want to store? "))
y = input(f"Please enter numbers seperated by a space: ")
my_list = y.split(" ")[:x]
print(f"We have a list of {len(my_list)} numbers: {my_list}")
match = sum(num//2 for num in Counter(my_list).values())
# print(match)
print("there are "+str(match)+" match number")