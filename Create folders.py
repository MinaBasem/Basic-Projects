
# Author: Mina Basem
# This software allows you to create
# multiple folders / directories where you save the code file

import os
from random import *
import string

numberOfDirectories = 5         # Number of folders you would like to create, adjust as needed
lengthOfName = randint(3, 5)    # Amount of letters needed in the title (name) of each folder / directory

path = os.getcwd()
print ("The current working directory is %s" % path)

for number in range(numberOfDirectories):
    random = ''.join(choice(string.ascii_letters) for n in range(lengthOfName))
    os.mkdir(random)

