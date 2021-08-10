# Accept number from user and print below pattern.
#input : 12     5
#output : 12  12  12  12  12

def Display(no1,no2):
    for i in range(no2):
        print(no1)

def main():
    print("Enter the number")
    value1 = int(input())
    
    print("Enter second number")
    value2 = int(input())
    
    Display(value1,value2)
    

    

if __name__=="__main__":
    main()