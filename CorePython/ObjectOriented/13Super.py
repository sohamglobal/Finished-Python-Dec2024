class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"


class Dog(Animal):
    def __init__(self, name, breed):
        # Call the parent class's constructor using super()
        super().__init__(name)
        self.breed = breed

    def speak(self):
        # Call the parent class's speak() method using super()
        return super().speak() + f", and barks loudly as a {self.breed}"


# Create an instance of the Dog class
dog = Dog("Buddy", "Golden Retriever")

# Call the speak() method of the Dog class
print(dog.speak())
