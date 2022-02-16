
from datetime import date

class Student:

    def __init__(self, StuID, Name, Bdate, Classification):
        self.__StuID = StuID
        self.__Name = Name
        self.__BDate = Bdate
        self.__Classification = Classification

    def Calc_age(self):
        today = date.today() 
        born = self.__BDate.split("/")
        stu_year = int(born[2])
        age = date.today().year - stu_year
        print("This students age is", age)


    def get_schedule(self):
        if self.__Classification == "F":
            return "Freshmen can register from 11/10 thru 11/12"
        elif self.__Classification == "S":
            return "Sophomores can register from 11/7 thru 11/9"
        elif self.__Classification == "Jr":
            return "Juniors can register from 11/4 thru 11/6"
        elif self.__Classification == "Sr":
            return "Seniors can register from 11/1 thru 11/3"
        else:
            return "No schedule to display: The classification passed in does not exist"





        

        