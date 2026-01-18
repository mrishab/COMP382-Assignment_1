import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from logic.matcher import match

# Test basic literals and special symbols
def test_literals():
    # Test 'a' literal
    assert match('a', 'a') == True
    assert match('a', 'b') == False

    # Test ε (empty string)
    assert match('ε', '') == True
    assert match('ε', 'a') == False

    # Test ∅ (empty set)
    assert match('∅', '') == False
    assert match('∅', 'a') == False

# Test union operator
def test_union():
    # Simple unions
    assert match('a∪b', 'a') == True
    assert match('a∪b', 'b') == True
    assert match('a∪b', 'ab') == False

    # Union with ε
    assert match('a∪ε', 'a') == True
    assert match('a∪ε', '') == True

# Test concatenation operator
def test_concatenation():
    # Simple concatenation
    assert match('a◦b', 'ab') == True
    assert match('a◦b', 'a') == False

    # Concatenation with ε
    assert match('a◦ε', 'a') == True
    assert match('ε◦a', 'a') == True

# Test star operator
def test_star():
    # a*
    assert match('a*', '') == True
    assert match('a*', 'a') == True
    assert match('a*', 'aa') == True
    assert match('a*', 'b') == False

    # (ab)*
    assert match('(a◦b)*', '') == True
    assert match('(a◦b)*', 'ab') == True
    assert match('(a◦b)*', 'abab') == True

# Test parentheses
def test_parentheses():
    # Simple parentheses
    assert match('(a)', 'a') == True
    assert match('(a◦b)', 'ab') == True

    # Parentheses with union
    assert match('(a∪b)◦a', 'aa') == True
    assert match('(a∪b)◦a', 'ba') == True
    assert match('(a∪b)◦a', 'bb') == False

# Test combined operators
def test_combined_operators():
    # Union of concatenations
    assert match('a◦b∪b◦a', 'ab') == True
    assert match('a◦b∪b◦a', 'ba') == True

    # Concatenation with star
    assert match('a◦b*', 'a') == True
    assert match('a◦b*', 'ab') == True

    # Star with union inside
    assert match('(a∪b)*◦a', 'a') == True
    assert match('(a∪b)*◦a', 'aba') == True

def run_all_tests():
    print("\n" + "="*70)
    print("RUNNING REGEX MATCHER TESTS")
    print("="*70)

    test_functions = [
        ("Basic Literals", test_literals),
        ("Union Operator", test_union),
        ("Concatenation Operator", test_concatenation),
        ("Star Operator", test_star),
        ("Parentheses", test_parentheses),
        ("Combined Operators", test_combined_operators),
    ]

    passed = 0
    failed = []

    for test_name, test_func in test_functions:
        try:
            test_func()
            passed += 1
            print(f"✓ {test_name}")
        except AssertionError as e:
            failed.append((test_name, str(e)))
            print(f"✗ {test_name} failed: {e}")
        except Exception as e:
            failed.append((test_name, f"Error: {e}"))
            print(f"✗ {test_name} error: {e}")

    print("\n" + "="*70)
    print("TEST SUMMARY")
    print("="*70)
    print(f"Total test categories: {len(test_functions)}")
    print(f"Passed: {passed}")
    print(f"Failed: {len(failed)}")

    if failed:
        print("\nFAILED TESTS:")
        for test_name, error in failed:
            print(f"  • {test_name}: {error}")
        return False
    else:
        print("\n ALL TESTS PASSED!")
        return True

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)