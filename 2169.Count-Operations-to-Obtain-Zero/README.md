### 2169. Count Operations to Obtain Zero

**Problem**  
You are given two non-negative integers `num1` and `num2`.  
In one operation, you must follow these rules:
1. If `num1 >= num2`, subtract `num2` from `num1`.  
2. Otherwise, subtract `num1` from `num2`.  

Repeat this operation until either `num1` or `num2` becomes `0`.  
Return the total number of operations required to make either integer zero.

**Examples**  
- num1 = 2, num2 = 3 → 3  
  (2,3) → (2,1) → (1,1) → (1,0)  

- num1 = 10, num2 = 10 → 1  
  (10,10) → (0,10)  

- num1 = 10, num2 = 4 → 5  
  (10,4) → (6,4) → (2,4) → (2,2) → (0,2)

**Constraints**  
- 0 ≤ num1, num2 ≤ 10⁵  
- Easy difficulty  

**Intuition**  
This operation pattern mirrors the **Euclidean algorithm** for computing the greatest common divisor (GCD).  
At each step, the smaller number is subtracted from the larger one — or equivalently, the larger number is reduced by a multiple of the smaller number.  
Instead of subtracting one-by-one, we can use integer division (`Math.floor(num1 / num2)`) and modulus (`num1 % num2`) to count and apply all subtractions in one step.

---

### 🧮 Complexity

**Solution 1 — Python (Recursive Approach)**  
- **Time:** O(max(num1, num2))  
- **Space:** O(max(num1, num2)) *(due to recursion stack)*  

**Solution 2 — TypeScript (Iterative Approach)**  
- **Time:** O(log(max(num1, num2)))  
- **Space:** O(1)  

#### Notes  
- The recursive version performs one subtraction per call, leading to linear time.  
- The optimized iterative version uses division and modulus to simulate multiple subtractions per iteration, achieving logarithmic performance.
