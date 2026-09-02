# Second Largest Element — Day 23

- **Topic:** Arrays
- **Difficulty:** Easy
- **Language:** PYTHON
- **Live Challenge:** [View on 100 Days of Code Platform](https://challenge.atharvabaodhankar.me/day/23)

---

## 📌 Problem Statement
Given an array of integers, find the second largest distinct element in the array. If there is no second largest element (e.g., array has less than two distinct elements or fewer than two elements), return -1.

---

## 💡 Pedagogical Intuition & Approach
A naive approach might involve sorting the array (O(N log N)) and then finding the second largest. However, we can achieve this in a single pass (O(N)) by keeping track of the largest and second largest elements encountered so far. We need to handle duplicates carefully and ensure we find a *distinct* second largest.

### Step-by-Step Logic
Initialize two variables, `largest` and `secondLargest`, both to a very small number (or the minimum possible integer value, or `arr[0]` and then iterate from `arr[1]`). Iterate through the array. For each element `x`:
1. If `x` is greater than `largest`:
   Update `secondLargest = largest`.
   Update `largest = x`.
2. Else if `x` is less than `largest` AND `x` is greater than `secondLargest`:
   Update `secondLargest = x`.
After iterating through all elements, `secondLargest` will hold the second largest distinct element. If `secondLargest` still holds its initial very small value (or `largest` is the only distinct value), it means no distinct second largest element was found, in which case we return -1.

---

## ⏱️ Complexity Analysis
- **Time Complexity:** `O(N) — Single pass scan of the array.`
- **Space Complexity:** `O(1) — Constant extra space for storing two variables.`

---
*Auto-synced via [100 Days of Code Platform](https://challenge.atharvabaodhankar.me)*
