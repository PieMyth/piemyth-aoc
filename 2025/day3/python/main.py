# Main.py to solve Day 3 of Advent Code 2025

def parse_file() -> list[str]:
    try:
        with open("battery_example.txt", "r", encoding="utf-8") as file:
            contents = file.readlines()
            trimed_contents = []
            for line in contents:
                trimed_contents.append(line.strip())
            return trimed_contents
    except FileNotFoundError as file_not_found_error:
        print("Could not find the file ", file_not_found_error)
        return None
    
def analyze_battery_bank_part_1(battery_bank: str):
    highest_output = 0
    bank_len = len(battery_bank)
    for i in range (0, bank_len):
        for j in range (i+1, bank_len):
            highest_output = max(highest_output, int(battery_bank[i] + battery_bank[j]))
    print("Highest output from this bank: ", highest_output)
    return highest_output
    
def solve(batteries: list[str]) -> int:
    total_power = 0

    for battery_bank in batteries:
        new_power = analyze_battery_bank_part_1(battery_bank)
        total_power += new_power

    return total_power

def main():
    batteries = parse_file()
    total_power = solve(batteries)
    print("Total power is: ", total_power)


if __name__ == "__main__":
    main()
