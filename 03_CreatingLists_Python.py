cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
# this is a list
print(cheese[1])
# [1] is 2nd on list, as list starts from [0]
# As stilton is 2nd that is [1], program will print "Stilton"

cheese [-1] = 'Red Leicester'
# pops 'Red Leicester' to replace last on list 'Cornish Yarg'
print(cheese)

cheese = ['Cheddar', ['Camembert', 'Brie'], 'Stilton']
print(cheese [1][0])
# position [1] in outer list is "Camembert", and then position [0] in nested list is still "Camembert"