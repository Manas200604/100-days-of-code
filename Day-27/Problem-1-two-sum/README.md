# Two Sum — Day 27

- **Topic:** Arrays, Hash Maps
- **Difficulty:** Easy
- **Language:** PYTHON
- **Live Challenge:** [View on 100 Days of Code Platform](https://challenge.atharvabaodhankar.me/day/27)

---

## 📌 Problem Statement
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`. You may assume that each input would have exactly one solution, and you may not use the same element twice.

---

## 💡 Pedagogical Intuition & Approach
A brute-force approach would involve checking every possible pair, leading to O(N^2) time complexity. To optimize, we need a faster way to find the 'complement' of a number (i.e., `target - current_number`). If we iterate through the array, for each number, we can calculate its complement. If this complement has been seen before, we have found our pair. A hash map (or dictionary) is ideal for storing numbers and their indices, allowing for O(1) average-time lookups.

### Step-by-Step Logic
The core idea is to iterate through the array once. For each number `num` at index `i`, we calculate the `complement` needed to reach the `target` (i.e., `complement = target - num`). We then check if this `complement` already exists as a key in our hash map. If it does, it means we've previously encountered the number that, when added to `num`, equals `target`. We can then return the index stored with the `complement` and the current index `i`. If the `complement` is not in the hash map, we add the current `num` and its index `i` to the hash map for future lookups.

---

## ⏱️ Complexity Analysis
- **Time Complexity:** `O(N) — Single pass scan. Hash map operations (insertion and lookup) take O(1) on average.`
- **Space Complexity:** `O(N) — In the worst case, all N elements might be stored in the hash map if no pair is found until the last element.`

---
*Auto-synced via [100 Days of Code Platform](https://challenge.atharvabaodhankar.me)*
