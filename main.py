
inputvalues = input('Enter all elements values: ')
numbers1 = inputvalues.split() 
for i in range(len(numbers1)):
	numbers1[i] = int(numbers1[i]) 


numbers2 = []
numbers2 = [ v for v in numbers1 if v % 2 ==0]		
print('The list numbers \n', numbers1)
print('The list for even index elements\n', numbers2)

# The following line is the same as the for-loop
# numbers1 = list(map(int, numbers))

# print ("The original list: ", numbers1)

# ******************************
# Make your Code
# ******************************
