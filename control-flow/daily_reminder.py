task = input("Enter your task: ").strip().lower()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()


match priority:
    case "high":
        print(f"Reminder: {task} is a high priority task", end="")

    case "low":
        print(f"Reminder : {task} is a low priority task", end="")

    case "medium":
        print(f"Reminder : {task} is a medium priority task", end="")
    case _:
        print("Invalid priority")


if time_bound == "yes":
    print(f" that requires immediate attention today!", end="")
else:
    print(f".Consider completing it when you have free time", end="")

print()
