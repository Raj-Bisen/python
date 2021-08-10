# Accept number from user and display below pattern.
# input : 5     
# output : A    B    C    D    E

def DisplayPattern(no):
    k = ord("A")
    for i in range(0,no):
        print(chr(k),end = "    ")
        k += 1
 
def main():
    print("Enter the number of rows : ")
    value = int(input())
    print("--------------------------------")
    DisplayPattern(value)
    print("\n--------------------------------\n")

if __name__=="__main__":
    main()