# Majority Element I — Day 28

- **Topic:** Arrays
- **Difficulty:** Easy
- **Language:** PYTHON
- **Live Challenge:** [View on 100 Days of Code Platform](https://challenge.atharvabaodhankar.me/day/28)

---

## 📌 Problem Statement
Given an array `nums` of size `n`, return the majority element. The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.

---

## 💡 Pedagogical Intuition & Approach
The core property of a majority element (appearing more than n/2 times) is that its count is strictly greater than the sum of counts of all other elements. This property allows for a clever linear-time, constant-space solution known as Boyer-Moore Voting Algorithm.

### Step-by-Step Logic
The Boyer-Moore Voting Algorithm works by maintaining a `candidate` element and a `count`. When iterating through the array, if the `count` is 0, we set the current element as the new `candidate`. If the current element matches the `candidate`, we increment `count`. Otherwise, we decrement `count`. The intuition is that if we pair up each occurrence of the majority element with an occurrence of any other element, the majority element will still be left over after all such pairings. The `count` essentially tracks the 'net' occurrences of the current `candidate` against other elements.

---

## ⏱️ Complexity Analysis
- **Time Complexity:** `O(N) — Single pass through the array.`
- **Space Complexity:** `O(1) — Constant extra space for `candidate` and `count` variables.`

---
*Auto-synced via [100 Days of Code Platform](https://challenge.atharvabaodhankar.me)*
