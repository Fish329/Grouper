import random
students=["alice","bob","catherine","dan","elanor","frank","gianna","harry","iris","justin","katy","link","mary","nick","oprah","pat","quinn","ryan","sam","tom"] #list of students
notThem=list() #list of exceptions 
grouped=list() #list of groups
picked=list() #for storing students about to be grouped
flag=False #true when exceptions should be empty
exceptions=0 #the number of exceptions that have been made. the max is 4
print("Students:")
for x in students:
 print(x)
pergroup=int(input("divide into groups of how many? (2-4)")) #input group size
if input("Is there anyone that can't be grouped together? (y/n)")=="y":
 flag=True
 while True: #exception loop
  which=input("""===================READ THIS=====================
  you can have a maximum of four exceptions.
  each student can only be involved in 1 exception.
  =================================================
  write the names of two students that cant be grouped together, separated by commas, with no spaces: """)
  if not which.split(",")[0] in notThem and not which.split(",")[1] in notThem:
    notThem.append(which.split(",")[0]) #put pair in list
    notThem.append(which.split(",")[1])
    exceptions+=1
  if input("Anyone else? (y/n)")=="n": break #stop getting exceptions
  else:
   if exceptions==4: #stop user from making too many exceptions
    print("Sorry, too many exceptions!")
    break
 itr=0
 for i in notThem:
  students.remove(notThem[itr])
  itr+=1
 random.shuffle(notThem) #shuffle exception list
 while len(notThem)>0: #until all excepted students are grouped
  pick1=notThem[0] #pick first student in shuffled list
  picked.append(pick1) #student is picked
  notThem.pop(0) #remove picked student from list
  while len(picked)<pergroup: #keep picking students until we have enough for one group
   pick2=random.choice(students)
   picked.append(pick2)
   students.remove(pick2)
  if len(students)==1: #take in straggler
   pick2=students[0]
   picked.append(pick2)
  grouped.append(str(picked))#add group to list of groups
  picked.clear()
 flag=False #all exceptions are taken care of. now start with normal students.
if flag==False: #if there are no exceptions, start from here
 while len(students)>1: #repeat until there are no students left
  pick1=random.choice(students) #pick 1 student
  picked.append(pick1) #student is picked
  students.remove(pick1) #picked student removed from pool
  while len(picked)<pergroup or len(students)>0: #keep picking students until there are enough for 1 group
   pick2=random.choice(students)
   picked.append(pick2)
   students.remove(pick2)
   if len(picked)>=pergroup or len(students)==0: break
  if len(students)==1: #take in straggler
   picked.append(students[0])
   students.remove(students[0])
  grouped.append(str(picked)) #add group to list of groups
  picked.clear()
 print("done! here are your groups:") #print finished list
 for x in grouped:
  print(x)
 
