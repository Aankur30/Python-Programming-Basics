dis={"fruit":"apple","car":"bugatti","gadgets":"laptop"}
dis_2={"fruit":"apple","car":"bugatti","gadgets":"mobile","personal":{"name":"Ankur","surname":"Verma","age":"12"}}
# changing values in the dictionary
dic_3={"name":"Ankur","Age":20,"List":["a",23,34.44]}
# indexing is possible in the dictionary but not the slicing

#INDEXING
print(dis_2["personal"]["age"])
print(dic_3["name"])
print(dic_3["List"])
print(dic_3["List"][1])
print(dic_3["List"][2])
# similar to the list indexing 
dic_3["name"]="Srishti" #the value in the dictionary got changed
print(dic_3)
d1={"fruits":"apple"}
d2={"object":"pen"}
d1.update(d2)
print(d1)
#add d2 at the end of the list d1
d1.update(d1)
print(d1) #it will return the same dictionary
# d1.clear()
print(d1) #clears the whole dictionary
a=dis_2.popitem() #this will give the value of the popped item and its pops the last item present the dictionary
print(a)
h=d1.pop("fruits")
print(h) #returns the popped dictionary item
print(dis.keys()) #dict_keys(['fruit', 'car', 'gadgets']) gives the output dictionary
print(dis.items()) #returns key and value as a 