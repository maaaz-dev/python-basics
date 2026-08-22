class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display_result(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

        if self.marks >= 40:
            print("Result: Pass")
        else:
            print("Result: Fail")


student1 = Student("Maaaz", 85)
student2 = Student("Rahul", 32)

student1.display_result()
student2.display_result()