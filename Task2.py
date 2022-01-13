
#Insert Existing task into task_list from PendingTask.txt file

f = open("PendingTask.txt","r")
task_list = []
for line in f:
    temp = line
    for i in range(3,len(line)-1):
        if line[i] == "[":
            index = i
            break
    pr = int(temp[index+1:len(temp)-2])
    job = temp[3:index-1]
    task_list.append([pr,job])



Completed_list = [] 
file = open("PendingTask.txt","a")
fileComplete = open("CompletedTask.txt","a")

#returns the Index address For the addition of new item
def sort_add(priority):
    index = len(task_list)
    for i in task_list:
        if priority == i[0]:
            index = task_list.index(i)+1
            
        elif(priority<i[0]):
            index = task_list.index(i)
            break
    return index


#display the Usage i.e The list of commands
def display():
    print('Usage :-')
    print('$ ./task add 2 hello world    # Add a new item with priority 2 ')
    print('$ ./task ls                   # Show incomplete priority list ')
    print('$ ./task del INDEX            # Delete the incomplete item ')
    print('$ ./task done INDEX           # Mark the incomplete item with the given index as complete')
    print('$ ./task help                 # Show usage')
    print('$ ./task report               # Statistics')

#Adding priority and Task to the list
def add(priority,task):
    priority = int(priority)
    task = ' '.join(task)
    index = sort_add(priority)
    task_list.insert(index,[priority,task])

    f = open("PendingTask.txt","w")
    for i in range(0,len(task_list)):
        f.writelines(str(i+1)+'. '+str(task_list[i][1])+" ["+str(task_list[i][0])+"]\n")
        #file.write(str(task_list[i]))


    #print(task_list)

#Displaying The pending list
def incomplete_list():
    for i in range(0,len(task_list)):
        print(str(i+1)+'. '+str(task_list[i][1])+" ["+str(task_list[i][0])+"]")


#Displaying the complete list
def complete_list():
    for i in range(0,len(Completed_list)):
        print(str(i+1)+'. '+str(Completed_list[i][1]))



if __name__ =='__main__':
    try:
        while(1):
            task_input = input(">>").split()
            if len(task_input) == 1:
                display()
            else:
                if task_input[1] == "add":
                    add(task_input[2],task_input[3:])
                    print("Added task: '"+' '.join(task_input[3:])+"' with priority",task_input[2])

                elif task_input[1] == "ls":
                    incomplete_list()

                elif task_input[1] == "del":
                    index = int(task_input[2])
                    try:
                        temp = task_list.pop(index-1)
                        print("Deleted item:",str(temp),"with index:",index)

                        f = open("PendingTask.txt","w")
                        for i in range(0,len(task_list)):
                            f.writelines(str(i+1)+'. '+str(task_list[i][1])+" ["+str(task_list[i][0])+"]\n")

                    except:
                        print("Error: item with index",index,"does not exist. Nothing deleted.")
                    #print(temp)
                
                elif task_input[1] == "done":
                    index = int(task_input[2])

                    try:
                        temp = task_list.pop(index-1)
                        f = open("PendingTask.txt","w")
                        for i in range(0,len(task_list)):
                            f.writelines(str(i+1)+'. '+str(task_list[i][1])+" ["+str(task_list[i][0])+"]\n")

                        Completed_list.append(temp)
                        print("Marked item as done")
                    except:
                        print("Error: no incomplete item with index",index,"exists.")

                elif task_input[1] == "report":
                    print("Pending: ",len(task_list))
                    incomplete_list()
                    print("\nCompleted: ",len(Completed_list))
                    complete_list()

                elif task_input[1] == "help":
                    display()
                else:
                    print("INVALID COMMAND ENTERED")    
            print("\n")
    except KeyboardInterrupt:
        print("exiting")