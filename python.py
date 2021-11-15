class Human:
    def __init__(self, name, age, sex):    
        self.name = name
        self.age = age
        self.sex = sex
    def view(self):
        print("이름: ",self.name)
        print("나이: ",self.age)
        print("성: ",self.sex)

p = Human("요환",41,"남자")
#p.view()
print("이름: ",p.name);
print("나이: ",p.age);
print("성: ",p.sex);