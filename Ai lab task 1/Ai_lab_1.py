
def check_eligibility(score, documents_complete, attendance, assignments):
    if score < 70:
        return "Fail", "Score is below 70"

    elif not documents_complete:
        return "Fail", "Documents are incomplete"

    elif attendance < 75:
        return "Fail", "Attendance is below 75%"

    elif assignments < 4:
        return "Fail", "Fewer than 4 assignments submitted"

    else:
        return "Pass", "All conditions satisfied"
    
test_cases = [
    {
        "input": (85, True, 80, 5),
        "expected": "Pass"
    },
    {
        "input": (85, True, 70, 5),
        "expected": "Fail"
    },
    {
        "input": (85, True, 80, 3),
        "expected": "Fail"
    },
    {
        "input": (70, True, 75, 4),
        "expected": "Pass"
    }
]

for i, case in enumerate(test_cases, 1):
    score, documents, attendance, assignments = case["input"]

    actual, reason = check_eligibility(
        score, documents, attendance, assignments
    )

    print(f"\nTest Case {i}")
    print(f"Input: Score={score}, Documents Complete={documents}, "
          f"Attendance={attendance}%, Assignments={assignments}")
    print(f"Expected Result: {case['expected']}")
    print(f"Actual Result: {actual}")
    print(f"Reason: {reason}")

