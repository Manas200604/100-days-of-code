# Best Time To Buy And Sell Stock — Day 29

- **Topic:** Arrays, Greedy
- **Difficulty:** Medium
- **Language:** PYTHON
- **Live Challenge:** [View on 100 Days of Code Platform](https://challenge.atharvabaodhankar.me/day/29)

---

## 📌 Problem Statement
You are given an array `prices` where `prices[i]` is the price of a given stock on the `i`-th day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

---

## 💡 Pedagogical Intuition & Approach
To maximize profit, we need to find the largest difference between a selling price and a buying price, where the buying day must occur before the selling day. This means for any given selling day, we should have bought the stock at the minimum price encountered *before or on* that day. We can iterate through the prices once, keeping track of the minimum price seen so far and updating the maximum profit based on the current price and that minimum.

### Step-by-Step Logic
We want to maximize `sell_price - buy_price` where `sell_day > buy_day`. As we iterate through the `prices` array day by day, we can maintain a variable `min_price_so_far` which stores the lowest stock price encountered up to the current day. For each `current_price` on the current day, we can calculate a potential profit: `current_price - min_price_so_far`. We then update our `max_profit` if this potential profit is greater. The `min_price_so_far` is continuously updated to ensure we always have the best possible buying point up to the current day.

---

## ⏱️ Complexity Analysis
- **Time Complexity:** `O(N) — Single pass through the array.`
- **Space Complexity:** `O(1) — Only a few constant extra variables are used.`

---
*Auto-synced via [100 Days of Code Platform](https://challenge.atharvabaodhankar.me)*
