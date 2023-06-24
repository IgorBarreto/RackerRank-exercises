There is a collection of input strings and a collection of query strings. For each query string, determine how many times it occurs in the list of input strings. Return an array of the results.

**Example**

$strings=['ab','ab','abc']$

$queries = ['ab','abc','bc']$

There are $2$ instances of $ab$, $1$ of $abc$ and $0$ of $bc$. For each query, add an element to the return array, $results=[2,1,0]$.

**Function Description**

Complete the function *matchingStrings* in the editor below. The function must return an array of integers representing the frequency of occurrence of each query string in *strings* .

matchingStrings has the following parameters:

* *string strings[n]* - an array of strings to search
* *string queries[q]* - an arrayss of query strings

**Returns**

* *int[q]:* an array of results for each query

**Input Format**

The first line contains and integer $n$, the size of  $strings[]$.

Each of the next $n$ lines contains a string $strings[i]$.

The next line contains $q$, the size of  $queries[]$.
Each of the next $n$ lines contains a string  $queries[i]$.

**Constraints**

$ 1 \le n \le 1000$

$1 \le q \le 100$

$ 1 \le |strings[i],|queries[i]| \le20$

| Input                                                                                                                                                                                                 |            Output            |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------: |
| 4<br />aba<br />baba<br />aba<br />xzxvb<br />3<br />aba<br />xzxb<br />ab                                                                                                                            |        2<br />1<br />0        |
| 3<br />def<br />de<br />fgh<br />3<br />de<br />lmn<br />fgh                                                                                                                                          |        1<br />0<br />1        |
| 13<br />abcde<br />sdaklfj<br />asdjf<br />na<br />basdn<br />sdaklfj<br />asdjf<br />naasdjf<br />na<br />basdn<br />sdaklfj<br />asdjf<br />5<br />abcde<br />sdaklfj<br />asdjf<br />na<br />basdn | 1<br />3<br />4<br />3<br />2 |

**Simple output 1**

2
1
0

**Simple input 2**

3
def
de
fgh
3
de
lmn
fgh

**Simple output 2**

1
0
1

Simple input 3

13
abcde
sdaklfj
asdjf
na
basdn
sdaklfj
asdjf
na
asdjf
na
basdn
sdaklfj
asdjf
5
abcde
sdaklfj
asdjf
na
basdn

**Simple output 3**

1
3
4
3
2
