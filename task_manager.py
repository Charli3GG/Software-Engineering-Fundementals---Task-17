# Notes:
# 1. Use the following username and password to access the admin rights
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the
# program will look in your root directory for the text files.

#=====importing libraries===========
import os
from datetime import datetime

DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Function to print task details
def print_task_details(task):
    print(f"Task: \t\t {task['title']}")
    print(f"Assigned to: \t {task['username']}")
    print(f"Date Assigned: \t {task['assigned_date'].strftime(DATETIME_STRING_FORMAT)}")
    print(f"Due Date: \t {task['due_date'].strftime(DATETIME_STRING_FORMAT)}")
    print(f"Task Description: \n {task['description']}\n")

# Function to get a valid numerical input that is greater than a certain value
def get_valid_numeric_input(
        min_value: int = 0,
        max_value: int = 0,
        input_string: str = "Enter numeric input",
        less_than_mix_string: str = "Value too low",
        greater_than_max_string: str = "Value too high",
        invalid_input_string: str = "Input not numeric"
        ):

    valid_int_only = min_value == max_value

    valid_input = min_value

    # Loop until the user enters a valid input
    while valid_input == min_value:
        # Ask for inpout using given string
        valid_input = input(input_string)

        # Check the input is numeric
        if valid_input.isnumeric() or valid_input[1:].isnumeric():
            valid_input = int(valid_input)

            if not valid_int_only:
                # Check of the input is less than the specifed value, display string if it not
                if valid_input < min_value:
                    print(f"""
{less_than_mix_string}
""")
                    valid_input = min_value
                elif valid_input > max_value:
                    print(f"""
{greater_than_max_string}
""")
                    valid_input = max_value
            # If the input is not numeric display the given string
        else:
            print(f"""
{invalid_input_string}
""")
            valid_input = min_value

    # Return the valiud input
    return valid_input

# Add a new user to the user.txt file
def reg_user():
    with open("user.txt", "r+", encoding = "utf-8") as reg_user_file:
        # - Loop to request input of a new username that does not already exist
        valid_new_user = False

        while not valid_new_user:
            new_username = input("New Username: ")
            valid_new_user = True

            for line in reg_user_file:
                if new_username in line:
                    print("That username already exists, please enter a different username")
                    valid_new_user = False
                    break

        # - Request input of a new password
        new_password = input("New Password: ")

        # - Request input of password confirmation.
        confirm_password = input("Confirm Password: ")

        # - Check if the new password and confirmed password are the same.
        if new_password == confirm_password:
            # - If they are the same, add them to the user.txt file,
            print("New user added")
            username_password[new_username] = new_password
            reg_user_data = []

            for key, user_password in username_password.items():
                reg_user_data.append(f"{key};{user_password}")

            reg_user_file.write("\n".join(user_data))

        # - Otherwise you present a relevant message.
        else:
            print("Passwords do no match")

def add_task():
    # Allow a user to add a new task to task.txt file
    #   Prompt a user for the following:
    #       A username of the person whom the task is assigned to,
    #       A title of a task,
    #       A description of the task and
    #       the due date of the task
    task_username = input("Name of person assigned to task: ")

    if task_username not in username_password.keys():
        print("User does not exist. Please enter a valid username")
        return

    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")

    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break

        except ValueError:
            print("Invalid datetime format. Please use the format specified")


    # Then get the current date.
    curr_date = datetime.today()

    # Add the data to the file task.txt and include 'No' to indicate if the task is complete.
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }

    task_list.append(new_task)

    with open("tasks.txt", "w", encoding = "utf-8") as tasks_file:
        task_list_to_write = []

        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]

            task_list_to_write.append(";".join(str_attrs))

        tasks_file.write("\n".join(task_list_to_write))
    print("Task successfully added.")

# Reads the task from task.txt file and prints to the console in the format of
# Output 2 presented in the task pdf (i.e. includes spacing and labelling).
def view_all():
    for t in task_list:
        print_task_details(t)

# Reads the task from task.txt file and prints to the console in the format of
# Output 2 presented in the task pdf (i.e. includes spacing and labelling).
def view_mine():
    task_number = 0
    user_task_list = []
    print("""
Your tasks:
""")

    for t in task_list:
        if t['username'] == curr_user:
            user_task_list.append(t)
            print(f"Task index: \t{str(task_number).zfill(3)}")
            print_task_details(t)
            task_number += 1

    viewing_task = 0

    # Sub menu for viewing and editing tasks
    while viewing_task > -1:
        viewing_task = get_valid_numeric_input(-2,
            len(user_task_list),
            "Please select a task number to view or enter -1 to return to the main menu\n",
            "The minimum value is 0 for a task or -1 to return to the main menu\n",
            f"The maximum value is the last task's index, currelty {len(user_task_list)}\n",
            "Please only enter a numeric value\n"
            )
        if viewing_task > -1:
            task = user_task_list[viewing_task]
            print_task_details(task)
            edit_task(task)

    # Write any task edits to the tasks.txt file
    with open("tasks.txt", "w", encoding = "utf-8") as tasks_file:
        task_list_to_write = []

        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]

            task_list_to_write.append(";".join(str_attrs))

        tasks_file.write("\n".join(task_list_to_write))
    print("Tasks updated successfully.")

# Generating two reports from user and task data
def generate_reports():
    total_tasks = len(task_list)
    current_date = datetime.now()

    # Loops though all tasks and count completed and overdue tasks
    with open("task_overview.txt", "w", encoding = "utf-8") as task_overview_file:
        task_overview_content = []
        completed_tasks = 0
        overdue_tasks = 0

        for t in task_list:
            if t['completed'] == "Yes":
                completed_tasks += 1

            if t['due_date'] < current_date:
                overdue_tasks += 1

        # Calculate the various report statistics and add to content list
        task_overview_content.append(f"Total Tasks: \t\t{total_tasks}")
        task_overview_content.append(f"Completed Tasks: \t{completed_tasks}")
        task_overview_content.append(f"Overdue Tasks: \t\t{overdue_tasks}")
        task_overview_content.append(
            f"Incomplete: \t\t{round((100 / total_tasks) * (total_tasks - completed_tasks), 2)}&")
        task_overview_content.append(
            f"Overdue: \t\t\t{round((100 / total_tasks) * overdue_tasks, 2)}&")

        task_overview_file.write("\n".join(task_overview_content))

    with open("user_overview.txt", "w", encoding = "utf-8") as user_overview_file:
        user_overview_content = []
        user_data_overview = {}

        for u_name in username_password.keys():
            user_data_overview[u_name] = {'tasks' : 0,
                                            'complete' : 0,
                                            'overdue' : 0}

        # Loops though all tasks and count completed and overdue tasks per user
        for t in task_list:
            user_data_overview[t['username']]['tasks'] += 1

            if t['completed'] == "Yes":
                user_data_overview[t['username']]['complete'] += 1

            if t['due_date'] < current_date:
                user_data_overview[t['username']]['overdue'] += 1

        # Calculate the various report statistics for each user and add to content list
        for u, data in user_data_overview.items():
            user_overview_content.append(f"User: {u}")
            user_overview_content.append(f"\tTotal Tasks: \t\t{data['tasks']}")
            user_overview_content.append(
                f"\tAssigned: \t\t\t{round((100 / total_tasks) * data['tasks'], 2)}&")
            user_overview_content.append(f"\tCompleted Tasks: \t{0}"
                .format(round((100 / data['tasks']) * data['complete'], 2)))
            user_overview_content.append(f"\tIncomplete: \t\t{0}&"
                .format(round((100 / data['tasks']) * (data['tasks'] - data['complete']), 2)))
            user_overview_content.append(f"\tOverdue: \t\t\t{0}&"
                .format(round((100 / data['tasks']) *  data['overdue'], 2)))
            user_overview_content.append("")

        user_overview_file.write("\n".join(user_overview_content))
        print("\nReports generated successfully!")

# Viewing reports prints the selected reports to the console, reports are generated if none exist
def view_reports():
    if not os.path.exists("task_overview.txt") or not os.path.exists("user_overview.txt"):
        generate_reports()

    viewing = True
    while viewing:
        view_selection = input('''
Select a report to view:
to - Task Overview
uo - User Overview
e - Exit
: ''').lower()

        if view_selection == "to":
            with open("task_overview.txt", 'r', encoding = "utf-8") as task_overview_file:
                print(task_overview_file.read())
        elif view_selection == "uo":
            with open("user_overview.txt", 'r', encoding = "utf-8") as user_overview_file:
                print(user_overview_file.read())
        elif view_selection == "e":
            viewing = False
        else:
            print("Invalid input, please check selection")

# Tasks can have thier due date, assigned user and completion status editied
def edit_task(task):
    valid_edit_command = False

    while not valid_edit_command:
        task_edit = input('''Select one of the following options:
c - Mark the task as completed, then exit menu
u - Reassign the task to the entered user
dd - Update the due date
e - Exit menu
''').lower()

        if task_edit == "c":
            task['completed'] = "Yes"
            valid_edit_command = True
        elif task_edit == "dd" or "u":
            valid_input = False

            # Sub loop for editing menu to validate input
            while not valid_input:
                if task_edit == "u":
                    assignee = input(
                        "\n Please enter the username that the task should be reassigned to: \n")
                    for t in task_list:
                        if assignee == t['username']:
                            task['username'] = assignee
                            print("Task assignee updated \n")
                            valid_input = True
                            break
                    if not valid_input:
                        print(f"Username {assignee} not found \n")
                elif task_edit == "dd":
                    due_date = input('''
Please enter the updated due date for the task.
The format should be as follows YYYY-MM-DD
''')
                    # Check entered date format is readable and convertable to a datetime
                    try:
                        datetime.fromisoformat(due_date)
                        task['due_date'] = datetime.strptime(due_date, DATETIME_STRING_FORMAT)
                        print("Task due date updated \n")
                        valid_input = True
                    except ValueError:
                        print("Invalid date format \n")
        elif task_edit == "e":
            valid_edit_command = True
        else:
            print("Invalid input, please check selection and retry \n")

    print(task_list)

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w", encoding = "utf-8") as default_file:
        pass

with open("tasks.txt", 'r', encoding = "utf-8") as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]

task_list = []

for t_str in task_data:
    curr_t = {}
    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(
        task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False
    task_list.append(curr_t)


#====Login Section====
# This code reads usernames and password from the user.txt file to allow a user to login.
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w", encoding = "utf-8") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r', encoding = "utf-8") as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True

while True:
# presenting the menu to the user and making sure that the user input is converted to lower case.
    print()
    menu = input('''Select one of the following options:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - Generate Reports
vr - View Reports
ds - Display statistics
e - Exit
: ''').lower()

    if menu == 'r':
        reg_user()
    elif menu == 'a':
        add_task()
    elif menu == 'va':
        view_all()
    elif menu == 'vm':
        view_mine()
    elif menu == 'gr':
        generate_reports()
    elif menu == 'vr':
        view_reports()
    elif menu == 'ds' and curr_user == 'admin':
        # If the user is an admin they can display statistics about number of users and tasks.
        num_users = len(username_password.keys())
        num_tasks = len(task_list)

        print("-----------------------------------")
        print(f"Number of users: \t\t {num_users}")
        print(f"Number of tasks: \t\t {num_tasks}")
        print("-----------------------------------")
    elif menu == 'e':
        print('Goodbye!!!')
        exit()
    else:
        print("You have made a wrong choice, Please Try again")
