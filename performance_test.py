import time
from codes_testing import find_sums

# Performance test as suggested
numbers = list(range(1000000))
target = 2000000

start_time = time.time()
result = find_sums(numbers, target)
end_time = time.time()

print(f"Result: {result}")
print(f"Time taken: {end_time - start_time:.4f} seconds")
print(f"Should be < 0.5 seconds: {'✅ PASS' if end_time - start_time < 0.5 else '❌ FAIL'}")