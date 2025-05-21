# sets

myset = {1, 2, 3}
print(myset)

myset = {1.0, 'hello', (1,2,3)}
print(myset)

myset = {1,1,1,1,2,2,3,4,3,1,5}
print(myset)

myset = set([54, 'hi', 2.1, True])
print(myset, "\n")

# remove a number from a set:

numset = set([1,8, 5, 5, 5, 6, 4, 2, 8, 1, 7])
print("Original set:", numset)

numset.pop()

print("after removing the first elment from the set we get:", numset)



# Operations on set:

setx = {'green', 'blue'}
sety = {'blue', 'yellow'}
print("Original set elements:")
print(setx)
print(sety)
print("\n    intersection of two sets")
setz = setx.intersection(sety)
setu = setx.union(sety)
print(setz)
print(setu)



# ARRAY:
import array as arr

# create an array:

array_num = arr.array('i', [1,3,5,3,7,9,3])
print("Original array:" + str(array_num))

# count number of occurences:
print("Number of occurences of 3 in the given above array:" + str(array_num.count(3)))

# reversing Aaray:
r = array_num.reverse
print("after reversing the contents of the Aaray:", r)


''' cars = arr.array("b",['Pagani','Lambo','Toyota', 'Honda'])
print(cars[0])'''

