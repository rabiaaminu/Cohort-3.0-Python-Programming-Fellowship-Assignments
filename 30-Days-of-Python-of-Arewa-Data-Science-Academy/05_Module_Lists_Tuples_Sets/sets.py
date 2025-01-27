# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Exercises: Level 1
print(len(it_companies))
it_companies.add('Twitter')
it_companies.update(['Infosys', 'Flipkart'])
it_companies.remove('Infosys')
'''remove() raises an exception/error if element is not present in set'''

# Exercises: Level 2
print(A.union(B))
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.union(B))
print(B.union(A))
print(A.symmetric_difference(B))
del A
del B
del it_companies

# Exercises: Level 3
print(len(set(age)) < len(age))  # len of list is bigger

'''
A string is a series of characters (Anything inside quotes is considered a string in Python, and you can use single or double quote around your string)
List  list is a collection of items in a particular order
Tuple is an immutable list (Python refers to values that cannot change as immutable)
Set data structure is also an immutable data structure but stores in single row
'''

string = 'I am a teacher and I love to inspire and teach people.'
print(len(set(string.split())))
