import random

# Grade-wise topics
TOPICS = {
    "K-2": ["Addition", "Subtraction", "Counting", "Comparing Numbers"],
    "3-5": ["Multiplication", "Division", "Fractions", "Word Problems"],
    "6-8": ["Decimals", "Factors & Multiples", "Basic Equations", "Pre-Algebra Word Problems"]
}

def get_grade():
    print("Select your grade group:")
    for i, g in enumerate(TOPICS.keys()):
        print(f"{i + 1}. {g}")
    choice = int(input("Enter choice: "))
    return list(TOPICS.keys())[choice - 1]

def ask_addition():
    a, b = random.randint(1, 20), random.randint(1, 20)
    print(f"What is {a} + {b}?")
    ans = int(input())
    return ans == a + b

def ask_subtraction():
    a, b = random.randint(1, 20), random.randint(1, 20)
    if b > a: a, b = b, a
    print(f"What is {a} - {b}?")
    ans = int(input())
    return ans == a - b

def ask_counting():
    n = random.randint(5, 20)
    print(f"Count up from 1 to {n}. What number do you reach?")
    ans = int(input())
    return ans == n

def ask_comparing():
    a, b = random.randint(1, 50), random.randint(1, 50)
    print(f"Which is greater? {a} or {b}?")
    ans = int(input())
    return ans == max(a, b)

def ask_multiplication():
    a, b = random.randint(2, 12), random.randint(2, 12)
    print(f"What is {a} x {b}?")
    ans = int(input())
    return ans == a * b

def ask_division():
    b = random.randint(2, 12)
    a = b * random.randint(2, 12)
    print(f"What is {a} ÷ {b}?")
    ans = int(input())
    return ans == a // b

def ask_fraction():
    num = random.randint(1, 9)
    den = random.randint(num+1, 10)
    print(f"What is {num}/{den} + {num}/{den}? (Answer as a fraction, e.g., 2/3)")
    ans = input().strip()
    return ans == f"{2*num}/{den}"

def ask_word_problem():
    apples = random.randint(2, 6)
    friends = random.randint(2, 5)
    print(f"You have {apples} apples and {friends} friends. If you share equally, how many apples does each friend get? (whole apples)")
    ans = int(input())
    return ans == apples // friends

def ask_decimals():
    a = round(random.uniform(1, 10), 1)
    b = round(random.uniform(1, 10), 1)
    print(f"What is {a} + {b}? (Round to 1 decimal place)")
    ans = float(input())
    return round(a + b, 1) == round(ans, 1)

def ask_factors():
    n = random.randint(10, 50)
    print(f"Name a factor of {n} other than 1 and itself:")
    ans = int(input())
    return n % ans == 0 and ans != 1 and ans != n

def ask_equation():
    x = random.randint(1, 10)
    b = random.randint(1, 10)
    print(f"Solve for x: x + {b} = {x + b}")
    ans = int(input())
    return ans == x

def ask_prealg_word():
    n = random.randint(2, 5)
    total = n * 4
    print(f"If you have {n} boxes and each has the same number of pencils. Altogether you have {total} pencils. How many pencils per box?")
    ans = int(input())
    return ans == 4

QUESTION_BANK = {
    "Addition": ask_addition,
    "Subtraction": ask_subtraction,
    "Counting": ask_counting,
    "Comparing Numbers": ask_comparing,
    "Multiplication": ask_multiplication,
    "Division": ask_division,
    "Fractions": ask_fraction,
    "Word Problems": ask_word_problem,
    "Decimals": ask_decimals,
    "Factors & Multiples": ask_factors,
    "Basic Equations": ask_equation,
    "Pre-Algebra Word Problems": ask_prealg_word
}

def main():
    print("Welcome to Kids Math Learning App!")
    grade = get_grade()
    topics = TOPICS[grade]
    print(f"You will be quizzed in: {', '.join(topics)}")
    score = 0
    for i in range(5):
        topic = random.choice(topics)
        print(f"\nQuestion {i+1} ({topic}):")
        if QUESTION_BANK[topic]():
            print("Correct!")
            score += 1
        else:
            print("Oops, that's not correct.")
    print(f"\nYour final score: {score}/5")
    print("Keep practicing to improve your math skills!")

if __name__ == "__main__":
    main()
