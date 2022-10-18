
inputvalues = input('Enter all elements values: ')
numbers = list(map(int,inputvalues.split()))   


numbers2 = []
#length = len(numbers)
for i in range(5):
    numbers2.append(numbers.pop(i))

print('The list numbers \n', numbers)
print('The list for even index elements\n', numbers2)

# The following line is the same as the for-loop
# numbers1 = list(map(int, numbers))

# print ("The original list: ", numbers1)

# ******************************
# Make your Code
# ******************************
