import random

# Filename to store leaderboard
FILE_NAME = "leaderboard.txt"

def format_binary_readable(binary_str):
    # Split the binary string into groups of 4 using list comprehension and then join them with spaces
    return ' '.join([binary_str[i:i+4] for i in range(0, len(binary_str), 4)])

def random_binary_to_decimal():
    binary_number = ''.join([str(random.choice([0, 1])) for _ in range(8)])
    decimal_number = int(binary_number, 2)
    return binary_number, decimal_number, 1

def random_binary_to_hexadecimal():
    binary_number = ''.join([str(random.choice([0, 1])) for _ in range(16)])
    hexadecimal_number = hex(int(binary_number, 2))[2:].upper()
    return binary_number, hexadecimal_number, 3

def random_hexadecimal_to_decimal():
    hexadecimal_number = ''.join([random.choice("0123456789ABCDEF") for _ in range(4)])
    decimal_number = int(hexadecimal_number, 16)
    return hexadecimal_number, decimal_number, 2

def load_leaderboard():
    try:
        with open(FILE_NAME, 'r') as file:
            lines = file.readlines()
            return [tuple(line.strip().split(": ")) for line in lines]
    except FileNotFoundError:
        return []

def save_leaderboard(leaderboard):
    with open(FILE_NAME, 'w') as file:
        for entry in leaderboard:
            file.write(f"{entry[0]}: {entry[1]}\n")

def display_leaderboard(leaderboard):
    print("\n--- LEADERBOARD ---")
    for idx, entry in enumerate(sorted(leaderboard, key=lambda x: x[1], reverse=True), start=1):
        print(f"{idx}. {entry[0]}: {entry[1]} points")

def main():
    leaderboard = load_leaderboard()
    total_score = 0

    print("Welcome to the conversion challenge game!")
    username = input("Enter your name: ")

    while True:
        challenge_type = random.choice(["b2d", "b2h", "h2d"])

        if challenge_type == "b2d":
            question, correct_answer, score = random_binary_to_decimal()
            user_answer = input(f"Convert the binary number {format_binary_readable(question)} to decimal: ")

        elif challenge_type == "b2h":
            question, correct_answer, score = random_binary_to_hexadecimal()
            user_answer = input(f"Convert the binary number {format_binary_readable(question)} to hexadecimal (without '0x' prefix): ").upper()

        elif challenge_type == "h2d":
            question, correct_answer, score = random_hexadecimal_to_decimal()
            user_answer = input(f"Convert the hexadecimal number {question} to decimal: ")

        if str(correct_answer) == user_answer:
            print(f"Correct! You earn {score} points!")
            total_score += score
        else:
            print(f"Incorrect. The correct answer is {correct_answer}.")
            break

    leaderboard.append((username, str(total_score)))
    save_leaderboard(leaderboard)

    display_leaderboard(leaderboard)

if __name__ == "__main__":
    main()

