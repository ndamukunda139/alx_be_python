# Prompt user to enter task and its priority
task = input("Enter the task you want to be reminded of: ")
priority = input("Enter the priority level (high/medium/low): ").lower()
time-bound = input("Is the task time bound? (yes/no): ").lower()

# Process the Task Based on Priority and Time Sensitivity
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: {task} is a high priority task. Please address it as soon as possible.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: {task} is a medium priority task and is time bound. Please plan to complete it soon.")
        else:
            print(f"Reminder: {task} is a medium priority task. Please get to it when you can.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: {task} is low priority task and is time bound. Try to complete it when possible.")
        else:
            print(f"Reminder: {task} is low priority task. Consider completing it when you have free time")
    case _:
        print("Invalid priority level. Please enter high, medium, or low.")
