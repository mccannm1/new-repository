# Dictionaries
# Version 1.2

""" The indices can be (almost) of any type
    A mapping between a set of indices called keys
    and a set of values. Each key maps to a value
    This assoociation is called key-value pairs or items
    A list is a very ordered collection, linear collection 
    of values. In dictionaries order doesn't matter.
    They are like associative arrays in Perl """

# Create a Dictionary
purse = dict()

purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)
print()
print(purse['candy'])

purse['candy'] = purse['candy'] + 2
print(purse)
print()

###
ddd =dict()
ddd['age'] = 21
ddd['course'] = 182
print(ddd)

# mutable
ddd['age'] = 23
print(ddd)
