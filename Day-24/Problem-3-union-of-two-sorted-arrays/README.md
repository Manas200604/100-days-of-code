# Union Of Two Sorted Arrays — Day 24

- **Topic:** Array Manipulation
- **Difficulty:** Hard
- **Language:** PYTHON
- **Live Challenge:** [View on 100 Days of Code Platform](https://challenge.atharvabaodhankar.me/day/24)

---

## 📌 Problem Statement
Given two sorted arrays `arr1` and `arr2`, return a new sorted array containing all distinct elements from both arrays. The resulting array should also be sorted.

---

## 💡 Pedagogical Intuition & Approach
A naive approach would be to combine both arrays into a single list, convert it to a `Set` to remove duplicates, and then convert it back to a `List` and sort it. This would take O((N+M) log(N+M)) time due to sorting and O(N+M) space for the combined list and set. However, since both input arrays are already sorted, we can leverage this property to find the union in a single pass using a two-pointer approach, similar to the merge step in merge sort, but with an added check for distinctness.

### Step-by-Step Logic
We can use two pointers, `i` for `arr1` and `j` for `arr2`, starting at the beginning of each array. We iterate through both arrays simultaneously:
1. Before comparing elements, we skip any consecutive duplicates in `arr1` using pointer `i` and in `arr2` using pointer `j`.
2. Then, we compare `arr1[i]` and `arr2[j]`:
   a. If `arr1[i] <= arr2[j]`:
      i. Add `arr1[i]` to our `unionList` if it's not already the last element added (to ensure distinctness).
      ii. Increment `i`.
   b. Else (`arr2[j] < arr1[i]`):
      i. Add `arr2[j]` to our `unionList` if it's not already the last element added.
      ii. Increment `j`.
3. After the main loop, one array might still have remaining elements. We iterate through the remaining elements of that array, adding them to `unionList` if they are distinct from the last element added, also skipping consecutive duplicates.

---

## ⏱️ Complexity Analysis
- **Time Complexity:** `O(N + M) — Single pass through both arrays using two pointers, where N and M are lengths of arr1 and arr2.`
- **Space Complexity:** `O(N + M) — To store the `unionList` in the worst case (no common elements).`

---
*Auto-synced via [100 Days of Code Platform](https://challenge.atharvabaodhankar.me)*
