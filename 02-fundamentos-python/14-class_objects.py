
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def work(self):
        return f"{self.name} está trabajando duro"
    
person1 = Person('Cesar', 24);
person2 = Person('Eduardo', 42);

print(person1.work())
print(person2.work())


