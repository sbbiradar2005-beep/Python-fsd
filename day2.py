# ####for loop#####

# for i in range(5):
#     print("hi")

# for i in range(1,11):
#     print("hello")

######while loop######

# i=1
# while i<=5:
#     print("gm")
#     i += 1


######function##### 

# def greet():         #[ ()-> parameter]
#     print("hello")
#     print("welcome to python programming")
# greet()

######function with parameters#####


# def add(a,b):        
#     print(result)
# add(10,20)
# add(50,60)


#####list######              []

# students=["revati","trupti","bhandu"]
# print(students)


# students=["revati","trupti","bhandu"]
# print(students[2])



# students=["revati","trupti","bhandu"]
# students.append("sonu")    #add
# students.remove("trupti")   
# students.insert(1,"bhandu")
# print(students)


#############tuple##############     ()

# students=("revati","trupti","bhandu")
# print(students)


# students=("revati","trupti","bhandu")
# print(students[1])


############dictionary############     {}

# students={"name":"sneha",
#           "age":20,
#           "marks":90,
#           "passed":True}
# print(students)


# students={"name":"sneha",
#           "usn":145,
#           "dept":"cse",
#           "college":"GCEM"}
# students["course"]="python"
# print(students["name"])
# print(students["usn"])
# print(students["dept"])
# print(students["college"])
# print(students["course"])


#############  class n objects  #################

# class student:
#     def display(self):
#         print("hello ")
#         print("welcome to python programming")
# s1=student()
# s1.display()


############# consructor ###################

# class student:
#     def __init__(self,name ,age ,marks):
#         self.name=name
#         self.age=age
#         self.marks=marks
#     def display(self):
#         print("Name:",self.name)
#         print("Age:", self.age)
#         print("Marks",self.marks)
# s1=student("sneha",20,90)
# s2=student("bhadu",18,91)
# s1.display()
# s2.display()


############# encapsulation ###################

# class student:
#      def __init__(self):
#          self.__marks = 0

#      def self_marks(self, marks):
#          self.__marks = marks

#      def show_marks(self):
#          print("student marks:",self.__marks)

#          s1=student()
#          s1.set_marks(85.5)
#          s1.show_marks()


############# inheritance ###############

# class grandfather:
#    def land(self):
#       print("grand father has a land")



# class father(grandfather):
#    def house(self):
#       print("father has house")

# class son(father):
#    def car(self):
#       print("son has a car")

# s=son()
# s.land()
# s.house()
# s.car()

######## multi #####

# class father:
#     def house(self):
#         print("father has a house")

# class son(father):
#     def car(self):
#         print("son has a car")

# class daughter(father):
#     def money(self):
#         print("daughter has money")

# d = daughter()
# s = son()

# s.house()
# s.car()
# d.money()

########### polymorphism ############


# class Animal:
#     def sound(self):
#         print("Animal makes a sound")


# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")


# class Cat(Animal):
#     def sound(self):
#         print("Cat meows")


# animals = [Dog(), Cat(), Animal()]

# for animal in animals:
#     animal.sound()


########### abstract #############


from abc import ABC,abstractmethod

class payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

class UPI(payment):
     def pay(self,amount):
         print(f"paid {amount} using UPI")

class Card(payment):
      def pay(self,amount):
              print(f"paid {amount} using Card")

p1=UPI()
p2=Card()
p1.pay(1000)
p2.pay(2000)
           






        







