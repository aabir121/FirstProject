print "GPA calculator"

marks=input("Enter your marks: ")

if(marks>=80 and marks<=100):
    print "A+"
elif(marks>=75  and marks<80):
    print "A"
elif(marks>=70  and marks<75):
    print "A-"
elif(marks>=65  and marks<70):
    print "B+"
elif(marks>=60  and marks<65):
    print "B"
elif(marks>=55  and marks<60):
    print "B-"
elif(marks>=50  and marks<55):
    print "C+"
elif(marks>=45  and marks<50):
    print "C"
elif(marks>=40  and marks<45):
    print "C-"
else:
    print "fail"