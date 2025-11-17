# Daily Habit Tracker

A simple, interactive Python script to help you build and maintain daily habits. Track what you've accomplished each day, view your progress, add new habits, and reset for a fresh start. Built using only Python basics: variables, lists, loops, and functions—no external libraries required!

## Features
- **Habit Management**: Start with predefined habits (e.g., Exercise, Read 30 minutes) and easily add your own.
- **Daily Marking**: Quickly mark habits as "done" or "not done" via user prompts.
- **Progress Tracking**: See completion count and percentage with a summary.
- **Interactive Menu**: A loop-based menu for viewing, marking, adding, resetting, or quitting.
- **Visual Feedback**: Emojis (✅/❌) for quick status glances.

## Requirements
- Python 3.6+ (tested on 3.12)

No additional dependencies—pure Python!

## Installation
1. Clone or download this repository:
   ```
   git clone https://github.com/yourusername/daily-habit-tracker.git
   cd daily-habit-tracker
2. Use the menu options:
- **1. View habits**: Displays all habits with current statuses.
- **2. Mark today's habits**: Prompts for each habit (yes/no).
- **3. Show progress**: Prints done/total and percentage.
- **4. Add a new habit**: Input a new habit name to append.
- **5. Reset for new day**: Clears all statuses to "not done".
- **6. Quit**: Exit the program.

## Customization
- Edit the `habits` list in the code to personalize your starting habits.
- Add more features like saving to a file: Use `open('habits.txt', 'w')` in a function.

## Learning This Project
This script was built step-by-step to teach Python fundamentals:
- **Variables**: Store habits and statuses.
- **Lists**: Hold multiple habits and their states.
- **Loops**: For iteration (e.g., `for` over lists, `while` for menu).
- **Functions**: Modular code for display, marking, etc.

Great for beginners—try modifying it!

## Contributing
Feel free to fork, improve, or submit pull requests. Ideas: Add data persistence, streaks, or GUI with Tkinter.
