# Accept number from user and if number is less than 10 print Hello else print Demo.
#input : 5
#outpur : Hello
#input : 12
#output : Demo
def Display(no):
    if(no < 10):
        print("Hello")
    else:
        print("Demo")

def main():
    print("Enter the number")
    value1 = int(input())
    
    Display(value1)
    

    

if __name__=="__main__":
    main()