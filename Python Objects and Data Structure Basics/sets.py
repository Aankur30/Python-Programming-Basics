set_1={"x","y","z",1,2,3,4,5,6,7,8};
print(type(set_1));
x=set([1,2,3]);
print(x);
print(type(x));
y=set((1,2,3,3,4,4,2,1,3,4,5,32,35,3,43,2,3,4,3));
print(y);

#cannot indexing because sets are unordered data types and we cannot tell the position of the elements, it is not fixed 
#so slicing is also not possible 
#functions applied over the sets
y.add(100);
print(y);
y.add("f");#this works
print(y);
y.update(x);
print(y);
y.update(set_1);#in update we can add the whole set into another set but with add we can add only one element into it
print(y);
print(y.pop());
print(y);
x=x.union(set_1);
print(x);
x=x.intersection(set_1);
print(x);