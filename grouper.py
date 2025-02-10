import random
students=["alice","bob","catherine","dan","elanor","frank","gianna","harry","iris"]
notthem=[]
grouped=[]
print("Students:")
for x in students:
    print(x)
pergroup=int(input("divide into groups of how many? (2-4)"))
cant=input("Anyone that cant be grouped together? (Y/N)")
if cant=="Y":
    which=input("write the names of each student that cant be grouped together, alphabetically, separated by commas, with no spaces.")
    not_them.append(which.lower())