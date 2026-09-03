# Sort An Array Of 0'S 1'S And 2'S — Day 27

- **Topic:** Arrays, Sorting, Three Pointers
- **Difficulty:** Medium
- **Language:** PYTHON
- **Live Challenge:** [View on 100 Days of Code Platform](https://challenge.atharvabaodhankar.me/day/27)

---

## 📌 Problem Statement
Given an array `nums` with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue. We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively. You must solve this problem without using the library's sort function.

---

## 💡 Pedagogical Intuition & Approach
A naive approach would be to count the occurrences of 0s, 1s, and 2s, then overwrite the array. This takes two passes (one for counting, one for writing) and O(1) extra space. However, we can achieve this in a single pass and in-place using a three-pointer approach, often called the Dutch National Flag algorithm. The key insight is to maintain three sections in the array: 0s at the beginning, 2s at the end, and 1s in the middle, while processing the unsorted elements.

### Step-by-Step Logic
The Dutch National Flag algorithm uses three pointers: `low`, `mid`, and `high`.
- `low` points to the end of the '0s' section (elements from `0` to `low-1` are 0s).
- `high` points to the beginning of the '2s' section (elements from `high+1` to `N-1` are 2s).
- `mid` is the current element being examined (elements from `low` to `mid-1` are 1s).

The algorithm iterates while `mid <= high`:
1. If `nums[mid]` is `0`: Swap `nums[mid]` with `nums[low]`. Increment both `low` and `mid`.
2. If `nums[mid]` is `1`: Increment `mid` (it's already in its correct '1s' section).
3. If `nums[mid]` is `2`: Swap `nums[mid]` with `nums[high]`. Decrement `high`. *Crucially, `mid` is not incremented here* because the element swapped into `nums[mid]` could be a 0, 1, or 2, and needs to be re-evaluated.

---

## ⏱️ Complexity Analysis
- **Time Complexity:** `O(N) — Single pass through the array. Each element is visited and potentially swapped at most a constant number of times.`
- **Space Complexity:** `O(1) — Constant extra space used for pointers.`

---
*Auto-synced via [100 Days of Code Platform](https://challenge.atharvabaodhankar.me)*
