# Example Python script

import sys
# sys is importing a python module, modules gives specific function
# sys - module gives us access to system

count_of_arguments = len(sys.argv)
# refactoring - select word, right hand click, click on refactor and rename
#argc is a variable
# what is argv? argument vector - argument is a keyword we give to perimeters - vector = list
# list of the arguments / list of perimeters
# perimeters what we run when running sys
# sys is automatically populated, when running the python program 0 is default
if count_of_arguments > 1:
    print('Too many args')
    print('arg 1 is ' + sys.argv [1])
    print('arg 2 is ' + sys.argv [2])
    # argv only when your running program from terminal
else:
    where = 'World'
# where = variable, 'World' goes into where
    print("Hello", where)

    print('Goodbye from ' + sys.argv [0])
# concatinating - putting together + for strings concatinates, + for mumbers is additional
# operands and operators - operators work on operands ie, y + x, yx is operands + is operator
# operator overloading - has different versions for example + with strings and intergers it operates different
# '' "" - just represents a string
# copy file path from run window (2nd path), open up terminal, first type in python then copy and paste path, hit enter, then add word, name