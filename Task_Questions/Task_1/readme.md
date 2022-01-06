#  Question 
```
4

3213
```
## Simple output
``` 
2
```
---

## Explaintion


1. First I created a function birthDayCandles, in this I passed two parameter's arguments first for limit and second for elements list for this I took two user input.

```python
def birthDayCandles(limitOfCandles,Candles):

//body of code

birthDayCandles(limit,Nuber_of_elements)
```

2. After this I took a loop for list's element indexing, the indexing will be constant till the second loop will iterate.


3. Then in if condition I am comparing the tallestCandle variable with the second loop indexing elements.

```python
if tallestCandle<Candles[j]:
    tallestCandle=Candles[j]

```

4. When all values are sorted we got the highest value.


5. I took one more **for** loop for comparing that highest value with all the elements of the list.


6. Then check which are equal with that highest number, we will count that number.

```python
if tallestCandle==Candles[k]:
    
```


7. In the last it will return counting of Tallest Candles. 
