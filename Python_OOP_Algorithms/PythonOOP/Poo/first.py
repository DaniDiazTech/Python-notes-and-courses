class person:
    
    def __init__(self, name, age):
      self.name = name
      self.age = age
    def greeting(self, other_person):
        return f"Hi, {other_person} I'm {self.name}, and I'm glad to meet you"

monica = person("Monica", 22)
raul = person("Raul", 22)

print(raul.greeting(monica.name))
print(monica.greeting(raul.name))
    