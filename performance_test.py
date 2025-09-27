import time
from codes_testing import find_sums, maxNumberWithOppositeSigns

print("=== PERFORMANCE TESTS ===\n")

# Test 1: find_sums
print("1. Testing find_sums with 1M numbers:")
numbers = list(range(1000000))
target = 2000000

start_time = time.time()
result = find_sums(numbers, target)
end_time = time.time()

print(f"   Result: {result}")
print(f"   Time taken: {end_time - start_time:.4f} seconds")
print(f"   Should be < 0.5 seconds: {'PASS' if end_time - start_time < 0.5 else 'FAIL'}")

# Test 2: maxNumberWithOppositeSigns
print("\n2. Testing maxNumberWithOppositeSigns with 1M numbers:")
# Create array with positive and negative numbers
big_array = list(range(-500000, 500000))  # [-500000, -499999, ..., 499999]

start_time = time.time()
result = maxNumberWithOppositeSigns(big_array)
end_time = time.time()

print(f"   Result: {result}")
print(f"   Time taken: {end_time - start_time:.4f} seconds")
print(f"   Should be < 0.5 seconds: {'PASS' if end_time - start_time < 0.5 else 'FAIL'}")

print("\n=== TESTS COMPLETED ===")

# Original output from codes_testing.py will appear above these results