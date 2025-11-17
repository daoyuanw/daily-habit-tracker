# Define variables and a list for habits
habits = ["Sleep before 0:00 AM", "Write a Journal","Exercise"]  # List of habit names
statuses = ["not done"] * len(habits)  # List of statuses (initialize all to "not done")

# Function to display habits and statuses
def display_habits():
    print("\nYour Daily Habits:")
    for i in range(len(habits)):
        status = "✅" if statuses[i] == "done" else "❌"
        print(f"- {habits[i]}: {status} {statuses[i]}")
              
# Function to mark habits (the input loop)
def mark_habits():
    print("Mark your habits for today!")
    for i in range(len(habits)):
        habit = habits[i]
        answer = input(f"Is '{habit}' done? (yes/no): ").lower().strip()
        statuses[i] = "done" if answer == "yes" else "not done"

# Function to show progress
def show_progress():
    done_count = sum(1 for status in statuses if status == "done")  # Count "done" items
    total = len(habits)
    percentage = (done_count / total) * 100
    print(f"\nProgress: {done_count}/{total} habits done ({percentage:.0f}% complete!)")

def add_habit():
    new_habit = input("Enter a new habit: ").strip()
    if new_habit:  # If not empty
        habits.append(new_habit)  # Add to end of list
        statuses.append("not done")  # Add matching status
        print(f"Added '{new_habit}'!")

# Function to reset for a new day
def reset_day():
    global statuses
    statuses = ["not done"] * len(habits)
    print("Statuses reset for a new day!")

# Main menu loop
def main():
    while True:  # Infinite loop until user quits
        print("\n--- Daily Habit Tracker ---")
        print("1. View habits")
        print("2. Mark today's habits")
        print("3. Show progress")
        print("4. Add a new habit")
        print("5. Reset for new day")
        print("6. Quit")
        
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            display_habits()
        elif choice == "2":
            mark_habits()
        elif choice == "3":
            show_progress()
        elif choice == "4":
            add_habit()
        elif choice == "5":
            reset_day()
        elif choice == "6":
            print("Great job tracking your habits! Goodbye.")
            break  # Exit the loop
        else:
            print("Invalid choice—try again.")

# Run the main program
if __name__ == "__main__":
    main()