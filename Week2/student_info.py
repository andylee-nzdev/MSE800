
student_list = []

class Student:

    def __init__(self, name, age, id):
            self.name = name
            self.age = age
            self.id = id

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, ID: {self.id}")


def collect_students():
    print("Collect students information")
    for i in range(3):
        name = input("Name: ")
        age = input("Age: ")
        id = input("ID: ")
        sdt = Student(name, age, id)
        student_list.append(sdt)


def display_students():
    print("Show student information sorted by name:")
    sorted_students = sorted(student_list, key=lambda s: s.name.casefold())
    for sdt in student_list:
        sdt.display_info()


def main():
    collect_students()
    display_students()


if __name__ == "__main__":
    main()