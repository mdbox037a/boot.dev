from steps_to_zero import *

run_cases = [
    (14, 6),
    (8, 4),
    (0, 0),
]

submit_cases = run_cases + [
    (1, 1),
    (123, 12),
    (1000, 15),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input number: {input1}")
    result = steps_to_zero(input1)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    if result == expected_output:
        return True
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
            print("Pass")
        else:
            failed += 1
            print("Fail")
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
