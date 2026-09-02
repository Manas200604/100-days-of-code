# Check If The Array Is Sorted Ii — Day 23

- **Topic:** Arrays
- **Difficulty:** Medium
- **Language:** PYTHON
- **Live Challenge:** [View on 100 Days of Code Platform](https://challenge.atharvabaodhankar.me/day/23)

---

## 📌 Problem Statement
Given an array `nums`, return `true` if the array was originally sorted in non-decreasing order and then rotated some number of positions (including zero). Otherwise, return `false`.
There may be duplicates in the array.

---

## 💡 Pedagogical Intuition & Approach
A sorted array (even with duplicates) will have elements in non-decreasing order. If it's rotated, there will be at most one 'break point' where `arr[i] > arr[i+1]`. For example, in `[3, 4, 5, 1, 2]`, the break is between 5 and 1. If there are zero break points, the array is already sorted. If there is one break point, say at index `i`, then `arr[i] > arr[i+1]`. For the array to be sorted and rotated, the elements before the break (`arr[0]` to `arr[i]`) must be sorted, and the elements after the break (`arr[i+1]` to `arr[N-1]`) must also be sorted. Additionally, the last element `arr[N-1]` must be less than or equal to the first element `arr[0]` to maintain the cyclic sorted property.

### Step-by-Step Logic
1. Initialize a counter, `disorderCount`, to 0.
2. Iterate through the array from `i = 0` to `N-2` (where `N` is the length of the array).
3. In each iteration, check if `arr[i] > arr[i+1]`. If this condition is true, it indicates a 'disorder' or a 'break point' in the non-decreasing order. Increment `disorderCount`.
4. After the loop, analyze `disorderCount`:
   a. If `disorderCount == 0`: The array is perfectly sorted (no rotations or 0 rotations). Return `true`.
   b. If `disorderCount == 1`: There is exactly one break point. For the array to be sorted and rotated, the element at the end of the array (`arr[N-1]`) must be less than or equal to the element at the beginning of the array (`arr[0]`). This condition ensures that the 'wrap-around' part of the rotation maintains the sorted order. Return `true` if `arr[N-1] <= arr[0]`, otherwise `false`.
   c. If `disorderCount > 1`: There are multiple break points, which means the array cannot be formed by rotating a single sorted array. Return `false`.

---

## ⏱️ Complexity Analysis
- **Time Complexity:** `O(N) — Single pass through the array.`
- **Space Complexity:** `O(1) — Constant extra space for the counter variable.`

---
*Auto-synced via [100 Days of Code Platform](https://challenge.atharvabaodhankar.me)*
