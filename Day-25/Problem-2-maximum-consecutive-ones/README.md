# Maximum Consecutive Ones — Day 25

- **Topic:** Array
- **Difficulty:** Easy
- **Language:** PYTHON
- **Live Challenge:** [View on 100 Days of Code Platform](https://challenge.atharvabaodhankar.me/day/25)

---

## 📌 Problem Statement
Given a binary array `nums`, return the maximum number of consecutive `1`s in the array.

---

## 💡 Pedagogical Intuition & Approach
We need to count consecutive `1`s. When we encounter a `1`, we extend the current sequence. When we encounter a `0`, the current sequence of `1`s is broken, and we must reset our count for the current sequence. Throughout this process, we need to keep track of the highest count observed so far.

### Step-by-Step Logic
The problem can be solved by iterating through the array once. We maintain a counter for the current sequence of ones. When a `0` is encountered, the current sequence ends, and we compare its length with the maximum length found so far. The counter is then reset. If the array ends with ones, a final comparison is needed.

---

## ⏱️ Complexity Analysis
- **Time Complexity:** `O(N) — Single pass through the array.`
- **Space Complexity:** `O(1) — Constant extra space for two integer variables.`

---
*Auto-synced via [100 Days of Code Platform](https://challenge.atharvabaodhankar.me)*
