import random
students=["alice","bob","catherine","dan","elanor","frank","gianna","harry","iris","justin","katy","link"] #list of students
notthem=list() #in order, list of exceptions, list of made groups, list for storing chosen students about to be grouped
grouped=list()
picked=list()
exceptions=0 #the number of exceptions that have been made. the max is 4
print("Students:")
for x in students:
 print(x)
pergroup=int(input("divide into groups of how many? (2-4)")) #input group size
if input("Is there anyone that can't be grouped together? (y/n)")=="y":
 while True: #exception loop
  which=input("""
  you can have a maximum of four exceptions. 
  write the names of two students that cant be grouped together, separated by commas, with no spaces. 
  only one exception per student.""")
  if not which.split(",")[0] in notthem and not which.split(",")[1] in notthem:
    notthem.append(which.split(",")[0]) #put pair in list
    notthem.append(which.split(",")[1])
    exceptions+=1
  if input("Anyone else? (y/n)")=="n": break #stop getting exceptions
  else:
   if exceptions==4: #stop user from making too many exceptions
    print("Sorry, too many exceptions!")
    break
 for i in notthem: #move students to exception list
  if notthem[0] in students:
   students.remove(notthem[0])
 print("unfinished")
 random.shuffle(notthem)
else: #if there are no exceptions, start from here
 while len(students)>0: #repeat until there are no students left
  pick1=random.choice(students) #pick 1 student
  picked.append(pick1) #student is picked
  students.remove(pick1) #picked student removed from pool
  while len(picked)<pergroup: #keep picking students until there are enough for 1 group
   pick2=random.choice(students) #^
   picked.append(pick2) #^
   students.remove(pick2) #^
  if len(students)==1: #take in straggler
   picked.append(students[0])
   students.remove(students[0])
  grouped.append(str(picked)) #add group to list of groups
  picked.clear()
 print("groups:") #print finished list
 for x in grouped:
  print(x)
 