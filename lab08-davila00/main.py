from people import Faculty, Student

faculties = []
students = []

while (True):
    print("\n\t\t***TUFFY TITATN CONTACT MAIN MENU***\n")

    print("a. Add faculty \nb. Print faculty \nc. Add student")
    print("d. Print student \ne. Exit the program")
    choice = input("\nEnter Menu Choice: ")

    if choice == 'a':
        first_name = str(input("Enter first name: "))
        last_name = str(input("Enter last name: "))
        department = str(input("Enter department: "))
        classFaculty = Faculty(first_name, last_name, department)
        faculties.append(classFaculty)

    elif choice == 'b':
        print("=" *20 + " FACULTY " + "=" *20)
        print("{0:<7} {1:<15} {2:<25} ".format("Record", "Name", "Deparment"))
        print("=" *7 + " " + "=" *15 + " " + "=" *25)
        for i in range(len(faculties)):
            faculty = faculties[i]
            print("{0:<7} {1:<15} {2:<25} ".format(i, faculty.firstname + " " +
            faculty.lastname, faculty.department))

    elif choice == 'c':
        first_name = str(input("Enter first name: "))
        last_name = str(input("Enter last name: "))
        classyear = str(input("Enter class year: "))
        major = str(input("Enter major: "))
        advisor = str(input("Enter faculty advisor: "))

        classStudent = Student(first_name, last_name)
        classStudent.set_class(classyear)
        classStudent.set_major(major)
        classStudent.set_advisor(advisor)
        students.append(classStudent)

    elif choice == 'd':
        print("=" *40 + " STUDENTS " + "=" *40)
        print("{0:<20} {1:<15} {2:<25} {3:20} ".format("Name", "Class", "Major",
                "Advisor"))
        print("=" *20 + " " + "=" *15 + " " + "=" *25 + " " + "=" *20)
        for i in range(len(students)):
            student = students[i]
            print("{0:<20} {1:<15} {2:<25} {3:20} ".format(student.firstname +
            " " + student.lastname, student.classyear, student.major,
            student[i].advisor.firstname + " " + student[i].advisor.lastname))

    elif choice == 'e':
        break

    else:
        print("invalid choice")
