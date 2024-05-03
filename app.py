import uuid
class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
""" new_id = str(uuid.uuid4())
mark = User(new_id, "Mark") ##new instance of User
print(mark) """
class Student(User):
    def __init__(self, id, name, official_class):
        super().__init__(id,name)
        self.official_class = official_class
    def __str__(self):
        return f"{self.name}, {self.official_class}, {self.id}"
class Teacher(User):
    def __init__(self, id, name, department, tenure):
        super().__init__(name,id)
        self.department = department
        self.tenure = tenure ##Boolean true or false
        self.privileges = "Teacher"
    def __str__(self):
        return f"{self.name}, {self.id}, {self.tenure}, {self.department}"
    
class Admin(Teacher):
    def __init__(self, id, name, department, tenure):
        super().__init__(id, name,department, tenure)
        self.privileges = "Admin"
    def __str__(self):
        return f"{self.name}, {self.id},{self.department}, tenure = {self.tenure}"

students =[]
teachers =[]
admins = []

def create_new_student(name, official_class):
    id = str(uuid.uuid4())
    new_student = Student(id, name, official_class)
    students.append(new_student)
    for student in students:
        print(student)

def create_new_teacher(name, department, tenure):
    id = str(uuid.uuid4())
    new_teacher = Teacher(id, name, department, tenure)
    teachers.append(new_teacher)
    for teacher in  teachers:
        print(teacher) 
    
def create_new_admin(name, department,tenure):
    id = str(uuid.uuid4())
    new_admin = Admin(id, name, department, tenure)
    admins.append(new_admin)
    for admin in admins:
        print(admin) 

add_more_users = "Y"
def check_tenure(status):
    if status.lower() == "y":
        return True
    else:
        return False

while add_more_users == "Y":
    user_request = input("What type of user do you want to add? Ex. ADMIN, TEACHER, OR STUDENT? ")
    if user_request.upper() == "STUDENT":
        name = input("Enter User Name ")
        official_class = input("Enter Official Class ")
        create_new_student(name, official_class)
    elif user_request.upper() == "TEACHER":
         name = input("Enter User Name")
         department = input("Enter Department Name ")
         tenure_query = input("Does the user have tenure? Y/N")
         tenure = check_tenure(tenure_query)
         create_new_teacher(name, department, tenure)
    elif user_request.upper() == "ADMIN":
         name = input("Enter User Name ")
         department = input("Enter Department Name ")
         tenure_query = input("Do they have tenure Y/N ")
         tenure = check_tenure(tenure_query)
         create_new_admin(name, department, tenure)
    else:
        print("Soemthing went wrong, are you sure you typed the request correctly? ")
    still_continue = input("Would you like to continue Y/N ").upper()
    add_more_users = still_continue