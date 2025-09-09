# 🧪 Unit Testing - Quick Guide

> References:  
> 📘 [Python Docs – unittest](https://docs.python.org/3/library/unittest.html)  
> 📘 [Python Course – doctest & unittest](https://python-course.eu/advanced-python/tests-doctest-unittest.php)  

---

## 1. Why Unit Testing?
- **Catch bugs early** → problems spotted in isolated units.  
- **Confidence in changes** → refactor safely, tests flag regressions.  
- **Documentation** → shows expected behavior.  
- **Save time** → prevents hours of debugging.  
- **Reliable systems** → critical for pipelines, APIs, ML workflows.  

---

## 2. What is Unit Testing?
- Tests the **smallest piece of code** (function/method).  
- A unit is *small enough* to test independently.  

Example:
```python
def add(a, b):
    return a + b
```

Test:
```python
import unittest

class TestMathFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

if __name__ == "__main__":
    unittest.main()
```

---

## 3. Frameworks
- ✅ `unittest` (built-in)  
- `pytest`  
- `nose`  
- `doctest`  

---

## 4. Key Terminology
- **Unit** → smallest testable code.  
- **Test Case** → one input + expected output check.  
- **Test Suite** → group of test cases.  
- **Fixture** → setup/teardown for test environment.  
- **Test Runner** → executes tests (`unittest.main`).  
- **Assertion** → checks conditions.  
- **Mocking** → fake objects to isolate tests.  
- **Coverage** → % of code tested.  

---

## 5. Nitpicks & Key Aspects ⚡
- Test method names **must start with `test_`** (discovery rule).  
- Test classes should inherit from `unittest.TestCase`.  
- Always keep **tests independent** (don’t rely on order or shared state).  
- Use **fixtures** (`setUp`/`tearDown`) to prepare/clean environment.  
- Test both **happy paths** and **edge cases**.  
- Use `assertRaises` to test errors explicitly.  
- Keep test files separate (e.g., `tests/test_calculator.py`).  
- Name test files with prefix `test_` → so discovery picks them up.  
- Don’t over-test trivial code, but ensure **core logic** is well-covered.  
- Aim for **high coverage**, but remember: 100% coverage ≠ bug-free.  

---

## 6. Common Assertions
```python
self.assertEqual(a, b)     # a == b
self.assertNotEqual(a, b)  # a != b
self.assertTrue(x)         # x is True
self.assertFalse(x)        # x is False
self.assertIsNone(x)       # x is None
self.assertIn(a, b)        # a in b
with self.assertRaises(ValueError):
    func(bad_input)
```

---

## 7. Fixtures Example
```python
class Example(unittest.TestCase):
    def setUp(self):    # before each test
        self.data = [1, 2, 3]

    def tearDown(self): # after each test
        self.data.clear()

    def test_len(self):
        self.assertEqual(len(self.data), 3)
```

---

## 8. Coverage 🔍
Install:
```bash
pip install coverage
```

Run with coverage:
```bash
coverage run -m unittest
coverage report -m
coverage html   # generates htmlcov/index.html
```

Example report:
```
Name               Stmts   Miss  Cover
--------------------------------------
calculator.py          2      0   100%
test_calculator.py     6      0   100%
```

---

## 9. Mental Model
```
Test Runner → Test Suite → Test Case → Unit → Assertion
(setUp → test_* → tearDown)
```

---

## 10. Quick Commands
- Run all tests: `python -m unittest -v`  
- Run file: `python -m unittest -v test_calculator.py`  
- Run single test:  
  `python -m unittest -v test_calculator.TestMathFunctions.test_add`  
- Run with coverage:  
  `coverage run -m unittest && coverage report -m`  

---
