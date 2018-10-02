task = []

class To_do_list():
  
    def repeat(self):
        tasks = input("Enter task here: ")
        priorities = input("Range priority of task, 1-3: ")
        task.append(tasks)
        task.append(priorities)
        quit = input("Press Q to quit, Enter to continue: ")
        if (quit == "q"):
            print(task)
        else:
            todolist.repeat(To_do_list)
        

todolist = To_do_list
todolist.repeat(To_do_list)

    
    

    
