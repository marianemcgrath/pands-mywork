# This program prints a random fruit

import random
fruits = ('Apple', 'Orange', 'Banana', 'Pear')

# We want a random number between 0 and length-1
index = random.randint(0,len(fruits)-1)

fruit = fruits[index]
print ("A Random fruit:{}".format(fruit))
