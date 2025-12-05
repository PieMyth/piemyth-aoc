# Main.py to solve Day 1 of Advent Code 2025


# Imports

# Code

# Function to read the "combination.txt" file and then convert
# it into a list of the steps from the code
def convert_file_to_text() -> list[str]:
    steps:list[str] = []
    try:
        with open("combination_example.txt", "r", encoding="utf-8") as file:
            for step in file.readlines():
                steps.append(step.strip())
    except FileNotFoundError as file_error:
        print("Error reading the file")
        print(file_error)
    return steps

# Parse step and return it as a tuple with (direction:str, number:int)
def parse_step(step:str) -> tuple[str, int]:
    return (step[0], int(step[1:]))

def execute_step(step: tuple[str, int], current_number: int) -> int:
    move, amount = step
    if move == "L":
        current_number -= amount
        while current_number < 0:
            current_number += 100
    if move == "R":
        current_number += amount
        while current_number > 99:
            current_number -= 100
    return current_number

# Function to use the combination and then return the value of the entry after
def solve_combo(steps:list[str]):
    # Starts at 50
    current_number = 50
    # Number of times it lands on 0 is the combo
    password = 0

    for step in steps:
        current_number = execute_step(parse_step(step), current_number)
        print("Current Number: ", current_number)
        if current_number == 0:
            password += 1

    # Return the output back
    return password

def main():
    print("Reading the combination.txt file")
    combo_steps = convert_file_to_text()
    solution = solve_combo(combo_steps)
    print("Got solution for lock: ", solution)

if __name__ == "__main__":
    main()
