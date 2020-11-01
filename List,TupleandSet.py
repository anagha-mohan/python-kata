# Lists
#Use=Modify data
friends=["Ann","Bob","Charlie"]
friends.remove("Ann")
print(friends)
friends.append("Ann")
print(friends)

#Tuples
#Immutable cannot modify 
#Use=Constant data
Tuple=("Ann","Bob","Charlie")
print(friends)
friends=Tuple+("Ann",)
print(friends)

#Set
#No duplicates
#No order where added elements is put
#Useful to compare 2 sets
set={"Girl","Boy"}
set.add("Kids")
print(set)
set.remove("Boy")
print(set)

ClassA={"tom","dick","harry"}
ClassB={"tom","Richard","Jose","harry"}
AnotinB=ClassA.difference(ClassB)
BnotinA=ClassB.difference(ClassA)
NotinBoth=ClassA.symmetric_difference(ClassB)
Both=ClassA.intersection(ClassB)
Union=ClassA.union(ClassB)
print(AnotinB)
print(BnotinA)
print(NotinBoth)
print(Both)
print(Union)