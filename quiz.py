QUESTIONS = [
    {
        "label": "Warm-Up: Lunch Check",
        "code": "if (!isHungry || hasFood)",
        "pseudo": "IF (NOT isHungry OR hasFood)",
        "claim": "This checks whether someone should eat lunch.",
        "answer": "disagree",
        "explanation": "!isHungry means NOT hungry, and || fires when either side is true - so anyone who is not hungry triggers it, even with no food. Fix: if (isHungry && hasFood)",
    },
    {
        "label": "Question 1: Weather Check",
        "code": "if (!(isRaining || isSnowing))",
        "pseudo": "IF (NOT (isRaining OR isSnowing))",
        "claim": "This checks whether it is neither raining nor snowing.",
        "answer": "agree",
        "explanation": "By De Morgan's Law, !(isRaining || isSnowing) is equivalent to (!isRaining && !isSnowing).",
    },
    {
        "label": "Question 2: Login Security",
        "code": "if (!hasPassword && hasBiometrics)",
        "pseudo": "IF ((NOT hasPassword) AND hasBiometrics)",
        "claim": "This checks whether a user lacks both a password and biometrics.",
        "answer": "disagree",
        "explanation": "It checks whether the user lacks a password AND has biometrics. Fix: if (!hasPassword && !hasBiometrics)",
    },
    {
        "label": "Question 3: Valid Score Range",
        "code": "if (score >= 0 && score <= 100)",
        "pseudo": "IF (score >= 0 AND score <= 100)",
        "claim": "This checks whether score is a valid percentage between 0 and 100 inclusive.",
        "answer": "agree",
        "explanation": "&& requires both bounds: at least 0 AND at most 100. (With || instead, every number would pass at least one test and the condition would always be true.)",
    },
    {
        "label": "Question 4: Weekend Detector",
        "code": 'if (day == "Sat" || day == "Sun")',
        "pseudo": 'IF (day = "Sat" OR day = "Sun")',
        "claim": "This checks whether day falls on a weekend.",
        "answer": "agree",
        "explanation": '|| needs only one match, and one day string only has to match one of them. (With && it could never be true - day cannot equal both strings at once.)',
    },
    {
        "label": "Question 5: Teenager Age Check",
        "code": "if (age > 13 && age < 19)",
        "pseudo": "IF (age > 13 AND age < 19)",
        "claim": "This checks whether someone is a teenager (from age 13 through 19 inclusive).",
        "answer": "disagree",
        "explanation": "Strict < and > exclude 13 and 19. Fix: if (age >= 13 && age <= 19)",
    },
    {
        "label": "Question 6: Discount Eligibility",
        "code": "if (!(isMember && hasCoupon))",
        "pseudo": "IF (NOT (isMember AND hasCoupon))",
        "claim": "This checks whether a shopper is neither a member nor has a coupon.",
        "answer": "disagree",
        "explanation": "By De Morgan's Law, this checks whether the shopper lacks membership OR lacks a coupon. Fix: if (!isMember && !hasCoupon)",
    },
    {
        "label": "Question 7: User Permissions",
        "code": "if (isAdmin || isEditor && isActive)",
        "pseudo": "IF (isAdmin OR isEditor AND isActive)",
        "claim": "This checks whether a user is active and is either an admin or an editor.",
        "answer": "disagree",
        "explanation": "&& has higher precedence than ||, so an inactive admin evaluates to true. Fix: if ((isAdmin || isEditor) && isActive)",
    },
    {
        "label": "Question 8: Body Temperature Check",
        "code": "if (!(temp != 98.6))",
        "pseudo": "IF (NOT (temp != 98.6))",
        "claim": "This checks whether temp is equal to 98.6.",
        "answer": "agree",
        "explanation": "Double negation simplifies directly to if (temp == 98.6).",
    },
    {
        "label": "Question 9: Ticket Status Filter",
        "code": 'if (status != "OPEN" || status != "PENDING")',
        "pseudo": 'IF (status != "OPEN" OR status != "PENDING")',
        "claim": 'This checks whether status is neither "OPEN" nor "PENDING".',
        "answer": "disagree",
        "explanation": 'Any string differs from at least one of those values, so this is always true. Fix: if (status != "OPEN" && status != "PENDING")',
    },
    {
        "label": "Question 10: Low-Battery Warning",
        "code": "if (isBatteryLow && !isPluggedIn)",
        "pseudo": "IF (isBatteryLow AND NOT isPluggedIn)",
        "claim": "This checks whether a laptop needs a low-battery warning while unplugged.",
        "answer": "agree",
        "explanation": "The warning fires when the battery IS low AND the laptop is NOT plugged in, and && requires both. (Putting the ! on isBatteryLow instead would check almost the opposite situation.)",
    },
]


def run_quiz():
    score = 0
    print("=== AP CSP Conditionals & Boolean Logic Quiz ===")
    print("Each question is shown in App Lab JavaScript and in AP exam pseudocode.\n")

    for i, q in enumerate(QUESTIONS, start=1):
        print(f"{q['label']} ({i}/{len(QUESTIONS)})")
        print(f"  Code:       {q['code']}")
        print(f"  Pseudocode: {q['pseudo']}")
        print(f"  Claim:      {q['claim']}")

        while True:
            user_input = input("Do you agree or disagree? (agree/disagree): ").strip().lower()
            if user_input in ("agree", "disagree"):
                break
            print("Please type 'agree' or 'disagree'.")

        if user_input == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect (Answer: {q['answer'].capitalize()}).")

        print(f"Explanation: {q['explanation']}\n")

    print(f"Final Score: {score}/{len(QUESTIONS)}")


if __name__ == "__main__":
    run_quiz()
