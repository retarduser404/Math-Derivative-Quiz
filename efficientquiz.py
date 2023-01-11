# Python quiz game
# Asking user for their name
name = input("What is your name? ")
name = name.title()
print("""Hello {}, Welcome to Derivative Quiz! 
You will be presented with 6 questions.
Enter the appropriate answer the question
Good luck!""".format(name))
print("-------------------------------------------------")
# a tuple of questions
questions = ("Q1.Derivative of cos x?: ",
             "Q2.Derivative of sin x?: ",
             "Q3.Derivative of tan x?: ",
             "Q4.Derivative of sec x?: ",
             "Q5.Derivative of cosec x?: ",
             "Q6.Derivative of cot x?: ",
             "Q7.Calculate the derivative of 7x²?: ",
             "Q8.Calculate the derivative of 19x³+6x²?: ",
             "Q9.Calculate the derivative of  14x³-9x⁵?: ",
             "Q10.Calculate the derivative of 16tan x?: ")
# a 2D tuple of options
options = (("A. -sin x", "B. sec²x", "C. -cosec²x", "D. cot x"),
           ("A. -cosec²x", "B. tan x", "C. cos x", "D. sec x tan x"),
           ("A. sec²x", "B. -cosec x cot x", "C. cot x", "D. None Of The Above"),
           ("A. tan x", "B. cot x cosec x", "C. cos²x", "D. sec x tan x"),
           ("A. -cosec x cot x", "B. -sin x", "C. sec²x", "D. sec x tan x"),
           ("A. cos x", "B.-cosec²x ", "C. tan x cos x", "D. None Of The Above"),
           ("A. 14x", "B. 21x²", "C. 49x²+56", "D. 17x⁶"),
           ("A. 75²+12x", "B. 65x", "C. 23x+19x⁸", "D. 57x²+12x"),
           ("A. 41x+19x", "B. 42x²-45x⁴", "C. 31x+62x", "D. None of the Above"),
           ("A. 61sec³x", "B. 8tan x", "C. 16sec²x", "D. None of the Above"))

# a tuple of answers
answers = ("A", "C", "A", "D", "A", "B", "A", "D", "B", "C")
guesses = []
score = 0
question_num = 0
for question in questions:
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A , B , C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("------------------------")
print("         RESULT❗      ")
print("------------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()
print("guesses:", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = (score / len(questions) * 100)
print("--------------------------------------------------------------")
print(f"Your score is: {score}% thanks for answering questions xD!")
print("--------------------------------------------------------------")
