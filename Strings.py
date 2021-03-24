# Version 1.1
#string slices
# A segment of a string is called a slice. Selecting a slice is similar to selecting a character

s = 'Monty Python'

# The operator returns the part of the string from the “n-th” character to the “m-th” character, 
#  including the first BUT EXCLUDING the last.

slice  = s[0:3]   # evaluates to Mon
print(slice)
slice  = s[0:5]   # evaluates to Monty
print(slice)
    
print(s[6:12])     # evaluates to Python
print(s[6:16])     # evaluates to Python
print()

# omit the index before the colon, the slice starts at beginnig of string
# omit the index after the colon, slice goes to the end of the string

fruit = 'banana'
print(fruit[:3])
print(fruit[3:])

# If the first index is greater than or equal to the second the result is an empty string
print('index is greater than or equal to the second')
print(fruit[3:3])
print()

print('Given that fruit is a string, what does fruit[:] mean?')
print(fruit[:])
print()
