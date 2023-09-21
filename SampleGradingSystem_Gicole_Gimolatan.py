FullName = input(str("Enter Your Full Name: "))
Id = input(str("Enter Your ID Number: "))
Course = input(str("Enter Your Course Name: "))
FirstQuarter = eval(input("Enter Your First Quarter Score: "))
SecondQuarter = eval(input("Enter Your Second Quarter Score: "))
ThirdQuarter = eval(input("Enter Your Third Quarter Score: "))
FourthQuarter = eval(input("Enter Your Fourth Quarter Score: "))

average = (FirstQuarter + SecondQuarter + ThirdQuarter + FourthQuarter) / 4
print()
print(FullName)
print(Id)
print(Course)
print("The Average of your grades ", FirstQuarter, SecondQuarter, ThirdQuarter, FourthQuarter, "is", average)
