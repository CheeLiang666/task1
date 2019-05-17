
print("Hello World")
#name = input("Please enter your name: ")
#print("Nice to meet you "+ name)
str = "Hello World"

print(str[0])
print(str[2:6])
print(str[2:])
print(str * 3)
if("H" in str):
    print("True")

if("k" not in str):
    print("True")

print("My name is %s and i\'m %d kg" % ("Chong", 85))
print(r"\\Raw string displayed.")
str2 = "l"
print(str.count(str2, 0, len(str)))
print(str.find(str2, 0, len(str)))

list1 = ["Physics", "Science", "Science", "Mathematics", 1997, 1998, 2000]
list2 = [1, 2, 3, 4, 5, 6]
list1.remove(list1[0])
print("list1 repetition: ", list1 * 3)
print("list2[1:5]", list2[1:5])
print("List1 count object occur: ", list1.count("Science"))
print("List2 insert new number: ", list2.insert(len(list2), 7))
print("List2: ", list2)
list2.reverse()
print("List2 reverse: ", list2)

for x in range(10):
    print(x, end=" ")

#tuple
tuple1 = (1, "John", 2, "Jane", 3, "Robert")
tinyTuple = (4, "Rock", 5, "Jason")
print(tuple1)
print(tuple1[:2])
#create new tuple with existing tuples
newTuple = tuple1 + tinyTuple
print("New tuple created: ", newTuple)



x = 3
if x not in tuple1:
    print("Not found")
else:
    print("Found")


#Dictionary
dict = {}
dict['zero'] = "this is zero"
dict[1] = "this is one"
tinyDict = {'name' : 'john', 'code':67634, 'dept':'IT'}
print(dict['zero'])
print(dict[1])
print(dict)
print(tinyDict.keys())
print(tinyDict.values())
print(repr(tinyDict))

#print(dir(dict))