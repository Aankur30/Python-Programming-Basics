class sampleClass():
    pass

my_class_1=sampleClass()

class dog():
    def __init__(self,breed):
        self.breed=breed

my_dog=dog(breed="husky")
print(my_dog.breed)