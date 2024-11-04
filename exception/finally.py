l=[1,5,6,7];
i=input("Enter the intex: ");
# print(l[i]);

try:
    for j in range(1,11):
        print(f"{i}X{j} = {int(i)*j}");
except:
    print("Invalid input");
finally:
    print("I am always executed!");
    
    

    