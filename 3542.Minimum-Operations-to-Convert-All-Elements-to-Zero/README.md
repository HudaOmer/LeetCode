### 3542. Minimum Operations to Convert All Elements to Zero

**Problem**  
You are given an integer array `nums` consisting of non-negative integers.  
In one operation, you can select **any subarray** and set **all occurrences of the smallest non-zero value** in that subarray to zero.  

Return the **minimum number of operations** required to make all elements in the array equal to zero.

**Examples**  
- nums = [0, 2] → 1  
  Select subarray `[2]`, min = 2 → set 2 → 0 → `[0, 0]`.

- nums = [3, 1, 2, 1] → 3  
  (3,1,2,1) → set min(1) → (3,0,2,0)  
  → set min(2) → (3,0,0,0)  
  → set min(3) → (0,0,0,0).

- nums = [1, 2, 1, 2, 1, 2] → 4  
  Each new greater value (like 2 after 1) requires a new operation, leading to 4 total.

**Constraints**  
- 1 ≤ nums.length ≤ 10⁵  
- 0 ≤ nums[i] ≤ 10⁵  
- Medium difficulty  

**Intuition**  
Each time we encounter a **new value greater than the previous** (after removing larger ones), it represents a new operation.  
This can be efficiently tracked using a **monotonic non-decreasing stack**:  
- Traverse the array.  
- Pop larger values when you find a smaller one.  
- If the current value is greater than the top of the stack, it means a new “level” appears — count it as an operation and push it.  

This approach mimics the process of gradually reducing elements through layers of increasing values.

---

### 🧮 Complexity

**Solution — Monotonic Stack Approach**  
- **Time:** O(n)  
- **Space:** O(n)  

#### Notes  
- Each element is pushed and popped at most once.  
- The number of operations equals the count of unique non-decreasing “steps” in the array.  
- This method avoids repeatedly scanning subarrays, achieving linear time performance.
