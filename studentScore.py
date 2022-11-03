maths = int(input("Enter the marks scored in mathematics:"))
science = int(input("Enter the marks scored in science:"))
computer = int(input("Enter the marks scored in computer science:"))
total_marks = maths + science + computer
max_marks = 300
percentage = (total_marks/max_marks)*100
if (maths>=101) and (science>=101) and (computer>=101):
  print(maths,science,computer,("out of range in all the three subjects"))
elif (maths>100) and (science>100):
    print(maths,science,("out of range in maths and science"))
elif (maths>100) and (computer>100):
    print(maths,computer,("out of range in maths and computer"))
elif (science>100) and (computer>100):
    print(science,computer,("out of range in science and computer"))
elif (maths>100):
    print(maths,",maths marks out of range")
elif (science>100):
    print(science,",science marks out of range")
elif (computer>100):
    print(computer,",computer marks out of range")
elif(maths<100) or (science<100) or (computer<100):
    if (percentage>=0) and (percentage<=40):
        print("Grade: F")
        print("total marks scored in class x: %d" %(total_marks))        
        print("percentage scored by the student = %.2f" %(percentage))     
    elif(percentage>=41) and (percentage<=50):
        print("Grade: C")
        print("total marks scored in class x: %d" %(total_marks))        
        print("percentage scored by the student = %.2f" %(percentage))     
    elif(percentage>=51) and (percentage<=65):
        print("Grade: B")
        print("total marks scored in class x: %d" %(total_marks))        
        print("percentage scored by the student = %.2f" %(percentage))     
    elif (percentage>=66) and (percentage<=75):
        print("Grade: B+")
        print("total marks scored in class x: %d" %(total_marks))        
        print("percentage scored by the student = %.2f" %(percentage))     
    elif (percentage>=76) and (percentage<=85):
        print("Grade: A")
        print("total marks scored in class x: %d" %(total_marks))        
        print("percentage scored by the student = %.2f" %(percentage))     
    elif (percentage>=86) and (percentage<=100):
        print("Grade: A+")
        print("total marks scored in class x: %d" %(total_marks))        
        print("percentage scored by the student = %.2f" %(percentage))     
    else:print('Out of Range')