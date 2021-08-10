# Accept number from user and check whether number is even or odd.
#input : 6
#output : It is  even number
#input : 3
#output : It is odd number
def ChckNum(no):
    if no % 2 == 0:
        return True
    else:
        return False

def main():
    print("Enter the number")
    value = int(input())
    
   
    
    bret = ChckNum(value)
    if (bret == True):
        print("Number is  even")
    else:
        print("Number is odd")
    
    

    

if __name__=="__main__":
    main()