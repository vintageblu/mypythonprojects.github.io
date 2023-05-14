# This is a GPA calculator
tg = 0
tc = 0
print("enter semester (1-8)")
sem = int(input())
while sem >= 1 and sem <=8:
  sg = 0
  sc = 0
  print("how many courses have been taken for semester " + str(sem))
  n = int(input())
  for i in range(1, n+1, 1):
    print("Enter the course name")
    crs = input()
    print("Enter credit hours")
    c = int(input())
    print("Enter your numeric grade. (A=4, B=3.5, C=3.0, D=2.5, F=0)")
    g = float(input())
    gradepoint = c * g
    sg = sg + gradepoint
    print("semester grade" + str(sg))
    sc = sc + c
    tg = tg + gradepoint
    print("total grade" + str(tg))
    tc = tc +c
  gpa = sg / sc
  print("your gpa is " + str(gpa))
  print("Enter semester number (1-8) enter any other key (other than 1-8) to see yout cgpa")
  sem = int(input())
cgpa = tg / tc
print("CGPA" + str(cgpa))

