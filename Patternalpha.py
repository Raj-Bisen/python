# Accept number from user and display below pattern.
# input : 5     A
# output : A    A    A    A    A

def DisplayPattern(no,k):
    for i in range(0,no):
        print(k,end = "    ")
 
def main():
    print("Enter the number of rows : ")
    value = int(input())
    print("Enter the character")
    char = input()
    print("--------------------------------")
    DisplayPattern(value,char)
    print("\n--------------------------------\n")

if __name__=="__main__":
    main()