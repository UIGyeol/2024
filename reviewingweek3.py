class Person:
    name="jason"
    age=20
    def Hello(self):
        print(f"Hello my name is {self.name}")
    def Plus10(self):
        print(f"10년 후 의 나이는 {self.age+10}")
p1=Person()
p1.Hello()
p1.Plus10()

class Person:
    def __init__ (self,name,age):
        self.name=name
        self.age=age
    def Hello(self):
        print(f"Hello my name is {self.name}")

    def age10(self):
        print(f"Hello my age after 10 years is {self.age+10}")
p1 = Person("Sammy",20)
p1.Hello()
p1.age10()

class Student():
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def printinfo(self):
        print(f"My name is {self.name} and student id is {self.id}")
    def setname(self,name):
        self.name= name
        print(f"I am {self.name}") 
    def getname(self):
        return self.name
stu1=Student("Sammy",202010222)
stu1.printinfo()
stu1.setname("Eva")


class Circle:
    def __init__(self, r):
        self.r= r
    def area(self):
        a=3.14*self.r**2
        return a
    def perimeter(self):
        p=3.14*2*self.r
        return p
c1=Circle(3)
print(c1.area())
print(c1.perimeter())
for i in range(1,10):
    ci=Circle(i)
    if ci.area()==ci.perimeter():
        print(i)

class Car():
    def __init__(self,color,speed):
        self.color=color
        self.speed=speed
        self.printinfo()
    def speedUp(self):
        self.speed=self.speed+10
        return self.speed
    def speedDown(self):
        self.speed=self.speed-10
        return self.speed
    def printinfo(self):
        print(f"색: {self.color} \n속도: {self.speed}")
    def setColor(self,color):
        self.color=color
        self.printinfo()
        car1 = Car("black", 0)
car1=Car("black",10)
car1.printinfo()
car2 = Car("red", 120)
car3 = Car("yellow", 30)
car4 = Car("blue", 0)
car5 = Car("green", 0)

car4.speedUp()
car2.speedDown()
print(car3.color) # "yellow"
car3.color = "purple"
print(car3.color) # "purple"
car3.setColor("Pink")
print(car3.color) # "pink"

car3.printinfo()
car5.speed = 80
car5.printinfo()
car5.speedUp()
car5.speedUp()


