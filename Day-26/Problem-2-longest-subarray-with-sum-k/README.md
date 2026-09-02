# Longest Subarray With Sum K — Day 26

- **Topic:** Hash Map, Prefix Sums
- **Difficulty:** Medium
- **Language:** PYTHON
- **Live Challenge:** [View on 100 Days of Code Platform](https://challenge.atharvabaodhankar.me/day/26)

---

## 📌 Problem Statement
Given an array `nums` and an integer `k`, find the length of the longest subarray whose elements sum up to `k`.

---

## 💡 Pedagogical Intuition & Approach
A brute-force approach checking all possible subarrays would be O(N^2) or O(N^3), which is too slow for larger inputs. We need a more efficient way to find subarray sums. Prefix sums are a common technique for subarray sum problems. If we know the sum of elements from index 0 to `i` (let's call it `current_sum`), and we are looking for a subarray that sums to `k`, then we need to find if there was a previous prefix sum `P` such that `current_sum - P = k`. This means `P = current_sum - k`. If such a `P` exists at an earlier index `j`, then the subarray from `j+1` to `i` sums to `k`.

### Step-by-Step Logic
We can use a hash map (or dictionary) to store the first occurrence of each prefix sum encountered so far. The map will store `(prefix_sum, index)`. 

1.  Initialize `max_len = 0` to store the maximum length found.
2.  Initialize `current_sum = 0` to keep track of the sum of elements from the beginning of the array up to the current index.
3.  Initialize a hash map, `prefix_sums`, and add an entry `(0, -1)`. This entry is crucial: it handles cases where the subarray summing to `k` starts from index 0 itself (e.g., if `current_sum` becomes `k`, then `current_sum - k = 0`, and `prefix_sums[0]` gives us `-1`, making the length `i - (-1) = i + 1`).
4.  Iterate through the array `nums` from `i = 0` to `n-1`:
    a.  Add `nums[i]` to `current_sum`.
    b.  Check if `current_sum - k` exists as a key in `prefix_sums`. If it does, it means we found a subarray ending at `i` that sums to `k`. The length of this subarray would be `i - prefix_sums[current_sum - k]`. Update `max_len = max(max_len, i - prefix_sums[current_sum - k])`.
    c.  If `current_sum` is not already a key in `prefix_sums`, add `(current_sum, i)` to the map. We only store the *first* occurrence of a prefix sum because we want the *longest* subarray. Storing the earliest index for a given prefix sum ensures that `i - prefix_sums[current_sum - k]` yields the maximum possible length.

---

## ⏱️ Complexity Analysis
- **Time Complexity:** `O(N) — We iterate through the array once. Hash map operations (insertion and lookup) take O(1) on average.`
- **Space Complexity:** `O(N) — In the worst case, all prefix sums are unique, and we store N entries in the hash map.`

---
*Auto-synced via [100 Days of Code Platform](https://challenge.atharvabaodhankar.me)*
