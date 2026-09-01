# Move Zeros To End — Day 24

- **Topic:** Array Manipulation
- **Difficulty:** Medium
- **Language:** PYTHON
- **Live Challenge:** [View on 100 Days of Code Platform](https://challenge.atharvabaodhankar.me/day/24)

---

## 📌 Problem Statement
Given an integer array `nums`, move all `0`'s to the end of it while maintaining the relative order of the non-zero elements. You must do this in-place without making a copy of the array.

---

## 💡 Pedagogical Intuition & Approach
A straightforward approach would be to create a new array, copy all non-zero elements, and then fill the rest with zeros. This takes O(N) time and O(N) space. However, the problem explicitly asks for an in-place solution. This suggests a two-pointer approach where we can effectively 'compress' the non-zero elements to the front of the array.

### Step-by-Step Logic
We can use two pointers: `i` to iterate through the array and `j` to keep track of the position where the next non-zero element should be placed. As we iterate with `i`:
1. If `nums[i]` is non-zero, we place it at `nums[j]` and increment `j`. This effectively moves all non-zero elements to the beginning of the array, maintaining their relative order.
2. If `nums[i]` is zero, we simply skip it. The `j` pointer remains unchanged, effectively leaving a 'gap' for a zero.
After iterating through the entire array, all non-zero elements will be at indices `0` to `j-1`. The remaining elements from `j` to `N-1` must be zeros, so we fill these positions with zeros.

---

## ⏱️ Complexity Analysis
- **Time Complexity:** `O(N) — Two passes over the array (one to move non-zeros, one to fill zeros).`
- **Space Complexity:** `O(1) — In-place modification without extra space.`

---
*Auto-synced via [100 Days of Code Platform](https://challenge.atharvabaodhankar.me)*
