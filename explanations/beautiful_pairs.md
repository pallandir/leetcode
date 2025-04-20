<a id="readme-top"></a>

<br />
<div align="center">
  <a href="https://www.hackerrank.com/challenges/beautiful-pairs/problem?isFullScreen=true">
    <img src="../assets/gear.svg" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Beatiful pairs (easy)</h3>

  <p align="center">
    Problem details and solution(s)
    <br />
    <a href="https://www.hackerrank.com/domains/algorithms?filters%5Bsubdomains%5D%5B%5D=greedy"><strong>View it on HackerRank »</strong></a>
    <br />
    <br />
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a> -->
  </p>
</div>

## About The Problem

You are given two arrays, A and B, both of the same length n. You can change exactly one element in B to any other integer (not necessarily from the array). A beautiful pair is defined as a pair of indices (i, j) such that A[i] == B[j] and each element in B and A can be used at most once in such a pairing.

Your goal is to maximize the number of beautiful pairs after changing exactly one element in B.

## Case examples

Given `A = [1, 2, 3, 4]` and `B = [1, 2, 3, 3]`, the expected output is `4` <br/>

Without any change, the arrays share three values: 1, 2, and 3. After pairing those, we are left with 4 in A and an extra 3 in B. If we change the unmatched 3 in B to 4, we can pair it with the remaining 4 in A.

So, we can get a total of 4 beautiful pairs.
<p align="right">(<a href="#readme-top">back to top</a>)</p>

