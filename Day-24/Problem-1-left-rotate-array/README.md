# Left Rotate Array — Day 24

- **Topic:** Array Manipulation
- **Difficulty:** Easy
- **Language:** PYTHON
- **Live Challenge:** [View on 100 Days of Code Platform](https://challenge.atharvabaodhankar.me/day/24)

---

## 📌 Problem Statement
Given an array `arr` of size `N` and an integer `d`, rotate the array to the left by `d` positions. This means the first `d` elements will move to the end of the array, and the remaining `N-d` elements will shift to the left. The rotation should be performed in-place if possible, and `d` can be greater than `N`.

---

## 💡 Pedagogical Intuition & Approach
A naive approach would be to shift elements one by one `d` times, resulting in O(N*D) time complexity. A slightly better approach involves storing the first `d` elements in a temporary array, shifting the remaining `N-d` elements to the beginning, and then copying the temporary elements to the end. This takes O(N) time and O(D) space. For an optimal in-place solution with O(1) space, the 'reversal algorithm' is highly efficient.

### Step-by-Step Logic
The reversal algorithm works in three steps:
1. Reverse the first `d` elements of the array.
2. Reverse the remaining `N-d` elements of the array.
3. Reverse the entire array.

Before applying these steps, it's crucial to handle cases where `d` might be greater than `N`. In such scenarios, `d` should be normalized to `d % N` because rotating `N` times brings the array back to its original state.

---

## ⏱️ Complexity Analysis
- **Time Complexity:** `O(N) — Three passes for reversal, each taking O(N) time.`
- **Space Complexity:** `O(1) — In-place modification without extra space (excluding input/output storage).`

---
*Auto-synced via [100 Days of Code Platform](https://challenge.atharvabaodhankar.me)*
