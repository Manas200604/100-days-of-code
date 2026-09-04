# Kadane'S Algorithm — Day 28

- **Topic:** Arrays, Dynamic Programming
- **Difficulty:** Medium
- **Language:** PYTHON
- **Live Challenge:** [View on 100 Days of Code Platform](https://challenge.atharvabaodhankar.me/day/28)

---

## 📌 Problem Statement
Given an integer array `nums`, find the subarray with the largest sum, and return its sum.
A subarray is a contiguous non-empty sequence of elements within an array.

---

## 💡 Pedagogical Intuition & Approach
The key insight for Kadane's algorithm is that if the sum of a subarray becomes negative, it's always better to discard that subarray and start a new one from the next element. A negative prefix will only decrease the sum of any future subarray it's part of. We need to keep track of the maximum sum found so far and the current sum of the subarray ending at the current position.

### Step-by-Step Logic
Kadane's algorithm is a dynamic programming approach. Let `current_max` be the maximum sum of a subarray ending at the current position, and `max_so_far` be the overall maximum subarray sum found anywhere in the array. When iterating through the array, for each element `num`:
1. The `current_max` can either be `num` itself (starting a new subarray) or `num` added to the `current_max` from the previous position (extending the current subarray). We choose the larger of these two: `current_max = max(num, current_max + num)`.
2. The `max_so_far` is updated by comparing it with the `current_max`: `max_so_far = max(max_so_far, current_max)`.
This ensures that `max_so_far` always holds the largest sum encountered.

---

## ⏱️ Complexity Analysis
- **Time Complexity:** `O(N) — Single pass through the array.`
- **Space Complexity:** `O(1) — Constant extra space for `max_so_far` and `current_max` variables.`

---
*Auto-synced via [100 Days of Code Platform](https://challenge.atharvabaodhankar.me)*
