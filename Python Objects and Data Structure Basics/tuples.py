tup_1=("A","B","C","D");
print(tup_1);
print(type(tup_1));
tup_1=("a","b","c","d","e","f","c","h","c","j","k","l");
print(tup_1);
# tuple has only two functions count and indexing
print(tup_1.count("a"));#counts the same type of entity in the tuple
print(tup_1.index("a"));#put the value in the index argument and it gives the index of the entity
#it takes 3 arguments  first is value then starting index and stoppind index
print(tup_1.index("c",3,10));

#theory part of the tuples
# 1. Ordered 
#2.Unchangeable
#3.Allow duplicate
#4.Immutable
# there is a tuple constructor
