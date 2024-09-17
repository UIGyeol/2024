# Study
def mul(*values):
    output=1
    for value in values:
        output*=value
    return output

print(mul(5,7,9,10))

# Apply Calling name
listname = []
def Callname(*values):
    for i in values:
        listname.append(i)  
    return listname[0] 


username1 = input("Wait.. What is your name?\n")
username2 = input("And your surname is?\n")
userfullname= username1+username2
print(f"{Callname(username1,username2)}? Is it a real name or just a fake one?\n")
print(f"What is wrong with you? My full name is {userfullname}!\n")
print(f"{userfullname} is your legal name? Then, my name is John Smith.\n")
