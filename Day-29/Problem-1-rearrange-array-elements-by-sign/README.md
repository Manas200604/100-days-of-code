# Rearrange Array Elements By Sign — Day 29

- **Topic:** Arrays
- **Difficulty:** Easy
- **Language:** PYTHON
- **Live Challenge:** [View on 100 Days of Code Platform](https://challenge.atharvabaodhankar.me/day/29)

---

## 📌 Problem Statement
You are given a 0-indexed integer array `nums` of even length consisting of an equal number of positive and negative integers. You should rearrange the elements of `nums` such that the modified array follows the given conditions:
1. Every consecutive pair of integers has opposite signs.
2. For all integers with the same sign, the order in which they were present in `nums` is preserved.
3. The rearranged array begins with a positive integer.
Return the modified array.

---

## 💡 Pedagogical Intuition & Approach
The problem guarantees an equal number of positive and negative integers and an even length array. The output array must strictly alternate signs, starting with a positive number. This implies positive numbers will occupy even indices (0, 2, 4, ...) and negative numbers will occupy odd indices (1, 3, 5, ...). The crucial part is preserving the relative order of elements with the same sign.

### Step-by-Step Logic
Since we need to preserve the relative order of positive numbers among themselves and negative numbers among themselves, a simple two-pointer swap approach might not work directly without extra complexity. A more straightforward approach is to create a new result array. We can iterate through the original array once. We'll maintain two separate pointers for the `result` array: one for the next available even index for positive numbers (`pos_idx`) and one for the next available odd index for negative numbers (`neg_idx`). When we encounter a positive number in the input, we place it at `result[pos_idx]` and increment `pos_idx` by 2. Similarly, for a negative number, we place it at `result[neg_idx]` and increment `neg_idx` by 2.

---

## ⏱️ Complexity Analysis
- **Time Complexity:** `O(N) — Single pass through the input array.`
- **Space Complexity:** `O(N) — For storing the rearranged elements in a new array.`

---
*Auto-synced via [100 Days of Code Platform](https://challenge.atharvabaodhankar.me)*
