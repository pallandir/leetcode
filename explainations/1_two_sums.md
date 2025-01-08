<a id="readme-top"></a>

<br />
<div align="center">
  <a href="https://leetcode.com/problems/two-sum/description/">
    <img src="../assets/gear.svg" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">1. Two sums</h3>

  <p align="center">
    Problem details and solution(s)
    <br />
    <a href="https://leetcode.com/problems/two-sum/description/"><strong>View it on leetcode »</strong></a>
    <br />
    <br />
    <!-- <a href="https://github.com/othneildrew/Best-README-Template/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a> -->
  </p>
</div>

## About The Problem

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

## Case examples

- Given `nums = [3,2,4]` and `target = 6`, the expected output is `[1,2]`

- Given `nums = [3,3]` and `target = 6`, the expected output is `[0,1]`

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Intuition

A straightforward approach to solving this problem involves checking every pair in the list to see if their sum matches the target. However, this requires two nested loops, leading to a time complexity of O(n²).

A more efficient solution reduces the time complexity to O(n) by using a simple technique. The idea is to iterate through the list and, for each number, check if the difference
`(target - number)` is in the list. If so, we return the indices of the two numbers.

To implement this solution, we can take one of two approaches:

the first one is to make this check on the fly and return the indices of both numbers as soon as we match this case. For each number, check if its complement
`(target - number)` exists in the hash map. If it does, return the indices immediately.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Code

```py
def two_sums(nums, target):
    for index, item in enumerate(nums): # Using enumerate is more elegant than range as it returns both index and value
        if target - item in nums and nums.index(target - item) is not index:
            return [index, nums.index(target - item)]
    return -1
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Why does it work

In order for this solution to be implemented this way we had to make multiple assumptions that were hopefully covered by the problem statement.

For example if we had to return multiple solutions this logic would not work and we would have to track each solution in a data structure rather than reutrning everything once we found a solution.

Note also that if we exit the for loop the function returns -1 as a default value for all edge cases like empty list or no solutions (even if the problem statement assures that there is at least one solution).

<p align="right">(<a href="#readme-top">back to top</a>)</p>
