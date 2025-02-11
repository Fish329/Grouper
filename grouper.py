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
  which=input("you can have a maximum of four exceptions. write the names of each student that cant be grouped together, separated by commas, with no spaces. ")
  notthem.append(which.lower())
  if input("Anyone else? (y/n)")=="n": break
  else:
    if exceptions==4:
     print("Sorry, too many exceptions!")
     break
 iter=0
 for i in notthem: #move students to exception list
  if (notthem[iter].split(","))[0] in students:
   students.remove((notthem[iter].split(","))[0])
  if (notthem[iter].split(","))[0] in students:
   students.remove((notthem[iter].split(","))[0])
  iter +=1
 pick1=notthem[0].split(",")[0]
 picked.append(pick1)
 notthem.insert(0,notthem[0].split(",").pop(1))
 notthem.pop(1)
 pick2=random.choice(students)
 picked.append(pick2)
 while len(picked)>pergroup:
  students.remove(pick2)
  pick2=random.choice(students)
