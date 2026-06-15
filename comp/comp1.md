Dabir, Egor, and Arseniy just got on the train and decided to play a game. Dabir has a backpack with an infinite number of cubes. He built 𝑛
 towers from them, where the 𝑖
-th tower has height ℎ𝑖
 cubes.

Egor and Arseniy must choose an integer 𝑥𝑖
 for each tower 𝑖
 and increase its height by 𝑥𝑖
 exactly once. For example, if ℎ
 = [1,3,2,2
], 𝑥
 = [3,2,2,8
], then after increasing ℎ
 it will become [4,5,4,10
]. Their goal is to make the heights of all towers equal.

To make the game more interesting, Dabir wants to choose an integer 𝑘
 and add a restriction: each 𝑥𝑖
 must satisfy 1≤𝑥𝑖≤𝑘
. Help him find the smallest 𝑘
 for which it is possible to finish the game.

Input
The first line contains a single integer 𝑡
 (1≤𝑡≤104
) — the number of test cases.

Then 𝑡
 test cases follow.

The first line of each test case contains a single integer 𝑛
 (1≤𝑛≤5
).

The second line contains 𝑛
 integers ℎ1,ℎ2,…,ℎ𝑛
 (1≤ℎ𝑖≤6
).

Output
For each test case, output a single integer — the minimum value of 𝑘
 such that it is possible to make all towers have equal height.

