# Find Missing Number — Day 25

- **Topic:** Array
- **Difficulty:** Easy
- **Language:** CPP
- **Live Challenge:** [View on 100 Days of Code Platform](https://challenge.atharvabaodhankar.me/day/25)

---

## 📌 Problem Statement
Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number in the range that is missing from the array.

---

## 💡 Pedagogical Intuition & Approach
The problem states that we have `n` distinct numbers from a range `[0, n]`, meaning one number is missing. If we know the sum of all numbers that *should* be present in this range and the sum of all numbers that *are* present in the array, their difference will reveal the missing number.

### Step-by-Step Logic
The core idea is to leverage the property of arithmetic series. The sum of integers from `0` to `n` can be calculated directly using a formula. By subtracting the sum of the elements actually present in the array from this expected sum, we can find the missing element.

---

## ⏱️ Complexity Analysis
- **Time Complexity:** `O(N) — Single pass to calculate the sum of array elements.`
- **Space Complexity:** `O(1) — Constant extra space for sum variables.`

---
*Auto-synced via [100 Days of Code Platform](https://challenge.atharvabaodhankar.me)*
