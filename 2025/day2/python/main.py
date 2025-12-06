# Main.py to solve Day 2 of Advent Code 2025


def parse_file() -> list[str]:
    try:
        with open("ids.txt", "r", encoding="utf-8") as file:
            file_contents = file.readline().strip()
            # Check to see if the file is truly comma seperated
            if "," in file_contents:
                return file_contents.split(",")
            else:
                print("Error, no commas found in the file")
                return None
    except FileNotFoundError as file_error:
        print("Error opening file\n", file_error)

# Solution for part 1
def is_not_valid_id_part_1(id_in_question: str) -> bool:
    id_len = len(id_in_question)
    # We are an odd length string, can't repeat exactly once, instantly valid
    if (id_len % 2 == 1):
        return False
    half_id_len = int(id_len/2)
    # Check the first half against the second half
    return id_in_question[0:half_id_len] == id_in_question[half_id_len:]

# Break the string apart into equal sized chunks
def chunk_id_string(id_to_chunk: str, length_to_chunk: int) -> list[str]:
    list_of_ids: list[str] = []

    # Build the list chunk by chunk
    for i in range(0, len(id_to_chunk), length_to_chunk):
        list_of_ids.append(id_to_chunk[i : i + length_to_chunk])
    return list_of_ids

# Solution for part 2
def is_not_valid_id_part_2(id_in_question: str) -> bool:
    # Part 1 is still not valid, do the quick check
    if is_not_valid_id_part_1(id_in_question):
        return True
    id_len = len(id_in_question)
    half_id_len = int(id_len/2)
    # Only need to check for half the length, don't need to go further than that
    # as it wouldn't be even
    for i in range(1, half_id_len + 1):
        # If we can't be equally chunked, instantly can't be a invalid case
        # return early
        if id_len % i != 0:
            continue
        # Get the chunked string
        chunked_id = chunk_id_string(id_in_question, i)
        # Get the first index so we can compare to the rest
        first_index = chunked_id[0]
        all_matching = True
        # Iterate through all of the values, if they are not equal, say so
        # Then exit the loop immediately, no need to keep checking
        for chunked_val in chunked_id:
            if first_index != chunked_val:
                all_matching = False
                break
        # All chunks matched, this id was invalid
        if all_matching:
            return True
    # Id was valid
    return False

# Taked the parsed ranges and check them for invalid ids
def check_range(id_min_str: str, id_max_str: str) -> int:
    ret_val = 0
    # Convert the min/max into ints
    id_min_int = int(id_min_str)
    id_max_int = int(id_max_str)
    # Check each value inside of the range for invalid ids
    for i in range (id_min_int, id_max_int + 1):
        id_string_value = str(i)
        # Was this string invalid?
        if is_not_valid_id_part_2(id_string_value):
            # If it was add it to the sum to be returned and go to the next
            ret_val += i
            print("SUM: ", ret_val, " Number: ", i)

    return ret_val

# Take the total sums from all of the ranges
def solve(list_of_ranges: list[str]) -> int:
    sum_of_invalid_ids = 0
    # Split each input and give the ranges to the function,
    # Adding any value to the total sum
    for id_range in list_of_ranges:
        ranges = id_range.split("-")
        sum_of_invalid_ids += check_range(ranges[0], ranges[1])

    return sum_of_invalid_ids

def main():
    parsed_ids = parse_file()
    solution = solve(parsed_ids)
    # Print the solution
    print("Solution: ", solution)

if __name__ == "__main__":
    main()
