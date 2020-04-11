class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person CLASS to create an instance, and then execute the printname method:

<<<<<<< HEAD
p = Person("Johnny", "Doe")
=======
p = Person("Johnny", "bravo")
>>>>>>> 5a071ea20252abd99740f587e17eac76ecfec462
p.printname()
