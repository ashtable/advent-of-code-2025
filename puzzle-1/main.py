from typing import List


def main() -> None:
    starting_point = 50

    # Read in the input file of turns
    input_list: List[str] = read_input()

    # Apply the turns to the dial to get
    # the "zero-count" (i.e., the password)
    password: int = apply_turns(input_list, starting_point)

    print(f"The real password is {password}")


def read_input() -> List[str]:
    print("Reading input ...")

    input_list: List[str] = []

    with open("input.txt", "r", encoding="utf-8") as input_file:
        for line in input_file:
            line = line.rstrip("\n")
            input_list.append(line)

    print(f"Read {len(input_list)} lines")
    return input_list


def apply_turns(input_list: List[str], starting_point: int) -> int:
    # Create a Dial using a List[int]
    safe_dial = list(range(100))  # 0 to 99

    # Create a variable to track the dial's index
    current_index = starting_point

    # Create a counter to track the number of
    # times the dial hits the zero marker
    zero_count = 0

    for turn in input_list:
        direction: str = turn[0]  # First char
        amount: int = int(turn[1:])  # Remaining chars

        # Ensure that we remove any 360-degree amounts
        amount = amount % 100

        print(f"Dial is at {safe_dial[current_index]}")
        print(f"Go {direction} by {amount}")

        match direction:
            case "R":
                # Turn dial right, increasing numbers
                current_index += amount
                if current_index > 100:
                    # Sub-Case R1: We looped passed 0
                    current_index = current_index % 100
                elif current_index < 100:
                    # Sub-Case R2: We did not reach 0
                    pass  # Do nothing
                else:
                    # Sub-Case R3: We are at 100, which is zero
                    current_index = current_index % 100
                    zero_count += 1
            case "L":
                # Turn dial left, decreasing numbers
                current_index -= amount

                if current_index < 0:
                    # Sub-Case L1: We looped past 0 and
                    # need to compute the "real" value
                    # of current_index
                    current_index = current_index % 100
                elif current_index > 0:
                    # Sub-Case L2: We didn't loop past 0
                    pass  # Do nothing
                else:
                    # Sub-Case L3: We are at 0
                    zero_count += 1
            case _:
                raise Exception("Unknown direction")

    return zero_count


if __name__ == "__main__":
    main()
