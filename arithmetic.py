import random

def ask_positive_int(prompt: str) -> int:
    while True:
        raw = input(prompt)
        try:
            num = int(raw)
            if num > 0:
                return num
            print("Enter a positive int")
        except ValueError:
            print("Enter a positive int")
    
def ask_y_n(current: str) -> bool:
    while True:
        ans = input(current).strip().lower()
        if ans in ("y", "n"):
            return ans == "y"
        print("Type y or n")

def num_range(intOrDec):
    if intOrDec:
        while True:
            minI = input("Smallest number in game: ")
            maxI = input("Largest number in game: ")
            try:
                minimum = float(minI)
                maximum = float(maxI)
                if minimum < maximum:
                    return minimum, maximum 
                print("First number must be less than second.")
            except ValueError:
                print("Enter a Rational Number")
    else:
        while True:
            minI = input("Smallest number in game: ")
            maxI = input("Largest number in game: ")
            try:
                minimum = int(minI)
                maximum = int(maxI)
                if minimum < maximum:
                    return minimum, maximum 
                print("First number must be less than second.")
            except ValueError:
                print("Enter integers.")

def operations_maker(add, sub, mult, div):
    arith_list = []
    if add:
        arith_list.append("+")
    if sub:
        arith_list.append("-")
    if mult:
        arith_list.append("*")
    if div:
        arith_list.append("/")
    
    return arith_list

def sample_non_zero(lo, hi, use_decimals):
    while True:
        val = round(random.uniform(lo, hi), 2) if use_decimals else random.randint(int(lo), int(hi))
        if val != 0:         
            return val

def equations(min1, max1, min2, max2, iOrD, operations):
    ranEq = random.choice(operations) 
    if iOrD:
        ran1 = sample_non_zero(min1, max1, iOrD)
        ran2 = sample_non_zero(min2, max2, iOrD)
    else:
        ran1 = sample_non_zero(min1, max1, iOrD) 
        ran2 = sample_non_zero(min2, max2, iOrD)

    if ranEq == "+":
        answer = ran1 + ran2
        equation = f"{ran1} + {ran2}"
        pInput = input(f"{equation} = ")
    elif ranEq == "-":
        answer = ran1 - ran2
        equation = f"{ran1} - {ran2}"
        pInput = input(f"{equation} = ")
    elif ranEq == "*":
        answer = ran1 * ran2
        equation = f"{ran1} * {ran2}"
        pInput = input(f"{equation} = ")
    else:
        product = ran1 * ran2
        answer = ran1 
        equation = f"{product} / {ran2}"
        pInput = input(f"{equation} = ") 
        
        
    return answer, pInput, equation

def game():
    print("Arithmetic practice")
    numQs = ask_positive_int("How many questions do you want: ")

    use_add = ask_y_n("Do you want to use addition (y/n): ")
    use_sub = ask_y_n("Do you want to use subtraction (y/n): ")
    use_mult = ask_y_n("Do you want to use multiplication (y/n): ")
    use_div = ask_y_n("Do you want to use division (y/n): ")
    operations_list = operations_maker(use_add, use_sub, use_mult, use_div)
    if not operations_list:
        print("No ops chosen — defaulting to addition.")
        operations_list = ["+"]


    int_or_decimals = ask_y_n("Do you want to use decimals (y/n): ")
        
    print("(__) to (__) and (__) to (__)")
    oneLow, oneHi = num_range(int_or_decimals)
    print(f"{oneLow} to {oneHi} and (__) to (__)")
    twoLow, twoHi = num_range(int_or_decimals)
    print(f"{oneLow} to {oneHi} and {twoLow} to {twoHi}")

    correct = 0
    wrong = 0
    wrong_list = []
    for _ in range(numQs):
        rAnswer, pAnswer, eq = equations(oneLow, oneHi, twoLow, twoHi,
                                        int_or_decimals, operations_list)
        try:
            user_val = float(pAnswer) if int_or_decimals else int(pAnswer)
            correct_flag = abs(user_val - rAnswer) < 0.01
        except ValueError:
            correct_flag = False

        if correct_flag:
            correct += 1
        else:
            wrong += 1
            wrong_list.append(f"{eq} = {rAnswer}")

    print(f"Correct: {correct}")
    print(f"Wrong: {wrong}")
    print(f"List of wrong answer: {wrong_list}")
            
game()