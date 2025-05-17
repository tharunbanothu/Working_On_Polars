#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#class, Object, inheritence, abstraction, encapsulation, polymorphism


# In[10]:


class Car:
    def __init__(self, windows, doors, enginetype):
        self.windows=windows
        self.doors=doors
        self.enginetype=enginetype
    def drive(self):
        print(f"the person will drive the {self.enginetype} car")
        print(self.windows)
        print(self.doors)
        self.doors=6
        print(self.doors)

car1=Car(4,4,"petrol")
car1.drive()
print(car1.windows)


# In[5]:


#inheritence---- it is a fundamental concept in oop that allow a class to inhert properties and methods from another class.
#  single, multi level, multiple, hybrid, hirarchical



get_ipython().run_line_magic('pinfo', 'used')
To access instance variables and methods within the class.

To differentiate between instance variables and local variables.

It helps in modifying object-specific data.


# In[20]:


#single inheritence
class Car:
    def __init__(self, windows, doors, enginetype):
        self.windows=windows
        self.doors=doors
        self.enginetype=enginetype
    def drive(self):
        print(f"the person will drive the {self.enginetype} car")

class Tesla(Car):
    def __init__(self,windows,doors,enginetype, is_selfdriving):
        super().__init__(windows,doors,enginetype)
        self.is_selfdriving=is_selfdriving
    
    def selfdriving(self):
        print(f"Telsa supports selfDriving: {self.is_selfdriving}")
        
tesla1 = Tesla(4,4,"electric",True)

tesla1.selfdriving()
print(tesla1.windows)
tesla1.drive()   


# In[24]:


#multiple inheritence

#base class 1
class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print("subclass must implement this method")
#base class 2
class Pet:
    def __init__(self,owner):
        self.owner=owner
#derived class 
class Dog(Animal, Pet):
    def __init__(self,name,owner,breed):
        Animal.__init__(self,name)
        Pet.__init__(self,owner)
        self.breed=breed

    def speak(self):
        print(f'{self.name} says bow')
        
dog1=Dog("rio","rupa","pomerian")
dog1.speak()
print(dog1.owner)


# In[ ]:


#polymorphism
#it provides a way to perform a single action in different forms.
#it is achieved by using method overriding and interfaces


# In[26]:


#base class 1
class Animal:
    def speak(self):
        print("sound of an animal")
#derived class 
class Dog(Animal):
    def speak(self):
        print("says bow!")
dog1=Dog()
dog1.speak()
ani=Animal()
ani.speak()



# In[ ]:


#Abstraction--- the concept of hiding complex implementation details and showing only necessary features  of an object.
#this helps in reducing programming complexity and effort



You're importing ABC (Abstract Base Class) and abstractmethod from the abc module.

ABC is used to mark a class as abstract, and abstractmethod is used to force implementation in child classes.


# In[32]:


from abc import ABC,abstractmethod      #ABC- Abstract Base Class

#Abstract base class 
class Vehicle(ABC):
    def drive(self):
        print("The vehicle is used for driving")
    
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

car1=Car()
car1.start_engine()
car1.drive()
    
        


# In[ ]:





# In[ ]:


#Encapsuation---- concept of wrapping data(variables) and methods(functions) as a single unit.
#It restricts direct access to some of the objects components,
#which is a means of preventing accidental interference and misuse of the data.
#access modifiers ---public, protected, private


# In[ ]:


#Encapsulation with getter and setter methods
#access modifiers ---public, protected, private variable


# In[ ]:





# In[2]:


#encapsulation using access modifiers

class Person:
    def __init__(self,name,age,gender):
        self.__name=name     #private variable
        self._age=age       #protected variable
        self.gender=gender    #public variable
class Employee(Person):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)

emp1= Employee("tharun", 23,"Male")
print(emp1.__name)


# In[1]:


#encapsulation with help of getter and setter methods
class Person:
    def __init__(self,name,age,gender):
        self.__name=name     #private variable
        self._age=age       #protected variable
        self.gender=gender    #public variable
    
    #getter and setter methods
    
    #getter for name
    def get_name(self):
        return self.__name
    
    #setter for name
    def set_name(self,name):
        self.__name=name
    
    #getter for age
    def get_age(self):
        return self._age
    
    #setter for age
    def set_age(self,age):
        self._age=age
person1 = Person("tharun",22,"Male")
print(person1.get_name())
        
        
        
 


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




