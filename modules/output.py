def get_uncompleted_tasks(list):
    uncompleted_tasks = []
    for task in list:
        if task["completed"] == False:
            uncompleted_tasks.append(task)
    return uncompleted_tasks

## Get list of completed tasks
def get_completed_tasks(list):
    completed_tasks = []
    for task in list:
        if task["completed"] == True:
            completed_tasks.append(task)
    return completed_tasks

## Print list of task descriptions
def print_task_descriptions(list):
    for task in list:
        print(task["description"])

## Refactor get_uncompleted_tasks and get_completed_tasks
def get_tasks_by_status(list, status):
    tasks = []
    for task in list:
        if task["completed"] == status:
            tasks.append(tasks)
    return tasks

## Get tasks where time_taken is at least a given time
def get_tasks_taking_longer_than(list, time):
    tasks = []
    for task in list:
        if task["time_taken"] >= time:
            tasks.append(task)
    return tasks

## Find any task with specific description
def get_task_with_description(list, description):
    for task in list:
        if task["description"] == description:
            return task
    return "Task Not Found"

def print_task(task):
    print(f'Description: { task["description"] }')
    print(f'Status: { "Completed" if task["completed"] else "Incomplete"}')
    print(f'Time Taken: {task["time_taken"]} mins')

def print_list(list):
    for task in list:
        print_task(task)

def mark_task_complete(task):
    task["completed"] = True