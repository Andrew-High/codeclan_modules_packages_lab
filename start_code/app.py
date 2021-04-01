from modules.output import *
# from modules.task_list import *
from data.task_list import *
from modules.input import *

def print_menu():
    print("Options:")
    print("1: Display All Tasks")
    print("2: Get Uncompleted Tasks")
    print("3: Get Completed Tasks")
    print("4: Mark Task as Complete")
    print("5: Get Tasks Which Take Longer Than a Given Time")
    print("6: Find Task by Description")
    print("7: Add a new Task to list")
    print("Q or q: Quit")
    
while (True):
    print_menu()
    option = menu_select()
    if (option.lower() == 'q'):
        break
    if option == '1':
        print_list(tasks)
    elif option == '2':
        print_list(get_uncompleted_tasks(tasks))
    elif option == '3':
        print_list(get_completed_tasks(tasks))
    elif option == '4':
        description = description_search()
        task = get_task_with_description(tasks, description)
        if task != "Task Not Found":
            mark_task_complete(task)
    elif option == '5':
        time = int(task_duration())
        print_list(get_tasks_taking_longer_than(tasks, time))
    elif option == '6':
        description = task_description()
        print(get_task_with_description(tasks, description))
    elif option == '7':
        description = task_description()
        time_taken = int(task_duration())
        task = create_task(description, time_taken)
        tasks.append(task)
    else:
        invalid()
