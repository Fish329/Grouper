import random
students=["alice","bob","catherine","dan","elanor","frank","gianna","harry","iris","justin"]
notthem=list()
grouped=list()
picked=list()
splitall=list()
exceptions=0
print("Students:")
for x in students:
 print(x)
pergroup=int(input("divide into groups of how many? (2-4)"))
if input("Is there anyone that can't be grouped together? (y/n)")=="y":
 while True:
  which=input("""
  you can have a maximum of four exceptions. 
  write the names of two students that cant be grouped together, alphabetically, separated by commas, with no spaces. 
  only one exception per student.""")
  if not which in notthem:
   notthem.append(which.lower())
  if input("Anyone else? (y/n)")=="n": break
  else:
   if exceptions==4:
    print("Sorry, too many exceptions!")
    break
 itr=0
 for i in notthem: #move students to exception list
  if (notthem[itr].split(","))[0] in students:
   students.remove((notthem[itr].split(","))[0])
  if (notthem[itr].split(","))[0] in students:
   students.remove((notthem[itr].split(","))[0])
  itr +=1
 