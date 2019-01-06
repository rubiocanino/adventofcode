import time
# Get the sizes of the boxes
print("---------------------------------------------------")
# You only need to change the variable for the inputs
# I try to do it with the input but weird stuff happen when you read the input
# So better working that not working
print('Reading the file Day2-Z.txt')
sizes = open('Day2-Z.txt')
print("---------------------------------------------------")
time.sleep(1)

# To split the string in an array of chars 
sizesArray = list(sizes)
totalArea = []
for i in sizesArray:
    splitSizes = i.split('x')
    splitSizes = map(int, splitSizes)
    # The formula given by the problem 2*l*w + 2*w*h + 2*h*l
    area = (2*splitSizes[0]*splitSizes[1]) + (2*splitSizes[1]*splitSizes[2]) + (2*splitSizes[2]*splitSizes[0])
    # Sorting the array to find the smallest sizes of the box
    splitSizes = sorted(splitSizes)
    # Adding the extra papper
    area+= splitSizes[0]*splitSizes[1]
    # Adding to an array that saves all the square feets needed
    totalArea.append(area)

# Concatenate and sum all the array of the square feet needed
print('The elves need to order:' + str(sum(totalArea))+ ' of wrap paper')