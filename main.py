
inputvalues = input('Enter all elements values: ')
numbers = list(map(int,inputvalues.split()))   


numbers2 = []
length = len(numbers)
for i in range(len(numbers)):
   #length = len(numbers) 
   if (i % 2 == 0):
      #x = numbers.pop(i)
      #print(x)
      numbers2.append(numbers.pop(i))
      length = len(numbers)
   
print('The list numbers \n', numbers)
print('The list for even index elements\n', numbers2)

# The following line is the same as the for-loop
# numbers1 = list(map(int, numbers))

# print ("The original list: ", numbers1)

# ******************************
# Make your Code
# ******************************
