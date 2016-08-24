class Student:
   studentCount = 0

   def __init__(self, name, marks):
      self.name = name
      self.marks = marks
      Student.studentCount += 1

   def displayStudent(self):
      print ("Student Name : ", self.name,  ", marks: ", self.marks)

student1 = Student("umesh", 96)
student2 = Student("aravind", 97)
student1.displayStudent()
student2.displayStudent()
print ("No of students :" ,Student.studentCount)
