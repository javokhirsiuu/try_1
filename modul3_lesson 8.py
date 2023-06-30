class Parrent:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age


p_obj = Parrent(name="Siu",age = "17")

print(p_obj.get_name())
print(p_obj.get_age())