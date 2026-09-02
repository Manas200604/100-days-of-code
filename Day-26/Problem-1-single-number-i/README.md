# Single Number I — Day 26

- **Topic:** Bit Manipulation
- **Difficulty:** Easy
- **Language:** PYTHON
- **Live Challenge:** [View on 100 Days of Code Platform](https://challenge.atharvabaodhankar.me/day/26)

---

## 📌 Problem Statement
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

---

## 💡 Pedagogical Intuition & Approach
The problem asks us to find a unique number in an array where all other numbers appear exactly twice. This pattern immediately suggests using the properties of the bitwise XOR operation. The key properties of XOR are:
1.  `x ^ x = 0` (XORing a number with itself results in zero).
2.  `x ^ 0 = x` (XORing a number with zero results in the number itself).
3.  XOR is commutative (`a ^ b = b ^ a`) and associative (`a ^ (b ^ c) = (a ^ b) ^ c`).

### Step-by-Step Logic
Given the properties of XOR, if we XOR all the elements in the array together, the numbers that appear twice will effectively cancel each other out (e.g., `A ^ B ^ A = (A ^ A) ^ B = 0 ^ B = B`). The single number, which appears only once, will be XORed with zero (the result of all paired numbers cancelling out) and thus will remain as the final result.

---

## ⏱️ Complexity Analysis
- **Time Complexity:** `O(N) — We iterate through the array once, performing a constant time XOR operation for each element.`
- **Space Complexity:** `O(1) — We use a single variable to store the XOR sum, requiring no additional space proportional to the input size.`

---
*Auto-synced via [100 Days of Code Platform](https://challenge.atharvabaodhankar.me)*
