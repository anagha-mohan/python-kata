friends_age={"Ann":10,"Bob":15}
friends_age["Charlie"]=5
print(friends_age)
friends_age["Ann"]=0
print(friends_age)

#To access names without knowing them
#Tuples of Dictions
friends_age=( 
  {"name":{"Ann","n"},"age": 10},
  {"name": "Bob","age": 15}
  )
print(friends_age[0]["name"])

#Convert List to Dictionary
friends=[("a",1),("b",2),("c",3)]
dictionary_friends=dict(friends)
print(dictionary_friends)