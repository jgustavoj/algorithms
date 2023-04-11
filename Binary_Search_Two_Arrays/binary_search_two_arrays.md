# Binary Search: Array Pairs

You are given two arrays of lengths N and M, respectively. You are also given an integer K.
You need to find the total count of pairs such that the first element belongs to the first array and the second element belongs to the second array, and their sum is strictly less than K.

## Function Description

In the provided code snippet, implement the provided countPairs(...) method using the variables to print the total count of pairs such that the first element belongs to the first array and the second element belongs to the second array, and their sum is strictly less than K. You can write your code in the space below the phrase

“WRITE YOUR LOGIC HERE”.

There will be multiple test cases running, so the Input and Output should match exactly as provided.

The base Output variable result is set to a default value of -404, which can be modified. Additionally, you can add or remove these output variables.

## Input Format

The provided code handles the input and stores them in variables for you. The first line contains the size of the first array N.
The next N lines contain elements of array A.
The next line contains the size of the second array M. The next M lines contain elements of array B.
The next line contains an integer K.

## Sample Input

3 -- denotes N <br>
1 -- <br>
2 -- denotes elements of array A of size N <br>
3 -- <br>
2 -- denotes M <br>
1 -- <br>
2 -- denotes elements of array B of size M 4 -- denotes K <br>

## Constraints

1 <= N, M <= 105
1 <= A[i], B[i] <= 105 1 <= K <= 105

## Output Format

The output contains a single integer denoting the count of pairs, containing an element from array A and an element from array B with a sum strictly less than K.

## Sample Output

3

## Explanation

Array A = [1,2,3]. <br>
Array B = [1,2]. <br>
K = 4.<br>
The pairs where the first element belongs to array A and the second element belongs to array B, and their sum is strictly less than 4 are:<br><br>
{1,1}, {1, 2}, {2,1}.<br><br>

Hence, the <u>output</u> is

```
3
```
