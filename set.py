# Set items are unordered, unchangeable, and do not allow duplicate values.
#set uses curly braces
#you can add new items in a set but you cant change
#cannot have two items with same value
#set allows different data types




school={"Hanna","kanna","Bannah"}
book = {1,2,3,4}
school.update(book)
print(school)
print(len(school))
print(type(school))
#use of constructor set
school = set (("Hanna","kanna","Bannah"))
print(school)
home={"HM","KL","pM"}
#getting each item
for x in home:
    print(x)
    #checking items in set
print("HM" in home)
home.add("Kb")
print(home)
one = {1,2,3,4,5}
two = {6,7,8,9}
set1=one.union(two)
print(set1)
set1=one.intersection(two)
print(set1)
set1=one.difference(two)
print(set1)
print(set1)
two.discard(7)
two.remove(8)
print(two)
one.update(two)

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

