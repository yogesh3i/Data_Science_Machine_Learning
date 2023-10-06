dict1={"Maharashtra":"Mumbai","Goa":"Panji","Rajstan":"Jaipur","Andhra pradesh":"Haidrabad"}
for item, item2 in dict1.items():
    print(item,":",item2)
state=input("Enter a state ")
print("The capital of {state} is {dict1[state]}")