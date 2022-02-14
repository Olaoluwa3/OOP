import StudentClass as sc

def main():

    student1 = sc.Student(23124, "Jacob Hill", "02/04/2002", "F")

    #Calculate Age
    student1.Calc_age()

    #get schedule
    print(student1.get_schedule())

main()
