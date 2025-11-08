### 1611. Minimum One Bit Operations to Make Integers Zero

**Problem**  
Given a non-negative integer `n`, transform it into `0` using the following operations any number of times:
1. Flip the rightmost (0th) bit.
2. Flip bit `i` (i > 0) only if bit (i-1) is `1` and bits `(i-2)`…0 are all `0`.

Return the minimum number of operations needed.

**Examples**  
- n = 0 → 0  
- n = 3 → 2 (11 → 01 → 00)  
- n = 6 → 4 (110 → 010 → 011 → 001 → 000)

**Constraints**  
- 0 ≤ n ≤ 10^9  
- Hard difficulty  

**Intuition**  
Operations mirror the inverse Gray code sequence.  
If you let `ans = 0`, while (n > 0): `ans ^= n; n >>= 1;` then return `ans`.

### 🧮 Complexity

**Solution 1 — Python (Recursive Approach)**  
- **Time:** O((log n)<sup>2</sup>)  
- **Space:** O(log n) *(due to recursion stack)*  

**Solution 2 — TypeScript (Iterative Bitwise Approach)**  
- **Time:** O(log n)  
- **Space:** O(1)  

#### Notes
- The recursive Python solution recalculates the highest bit (`k`) in each call, adding an extra log n factor to its runtime.  
- The iterative TypeScript version performs one XOR + shift per bit, giving O(log n) time and constant space.
