# Accpet number from user and Display result of student on screen ...

def ChckResult(Marks):
    if(Marks < 0)|(Marks > 100):
        print("Invalid Marks")
        return
    if (Marks >= 0)&(Marks <= 35): 
        print("student is Fail")
    elif(Marks >= 35)&(Marks <=50):
        print("Student is pass")
    elif(Marks >= 50)&(Marks <= 60):
        print("Student is second class")
    elif(Marks >= 60)&(Marks <= 70):
        print("Student is First class")
    else:
        print("Student is in Destination ")

def main():
   
    print("Enter the marks of student")
    value1 = int(input())
    
    bret = ChckResult(value1)
    

if __name__=="__main__":
    main()