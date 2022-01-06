def birthDayCandles(limitOfCandles,Candles):
    tallestCandle=0
    for i in range(0, limitOfCandles):
        for j in range(0, limitOfCandles):
            if tallestCandle<Candles[j]:
                tallestCandle=Candles[j]

    count=0
    for k in range(0, limitOfCandles):           
        if tallestCandle==Candles[k]:
            count+=1
    return 'count of tallest Candles are {}'.format(count)

limit=int(input('Enter limit number : '))
Nuber_of_elements=[]
for i in range(0, limit):
    input_numbers=int(input('Enter numbers according to limit : '))
    Nuber_of_elements.append(input_numbers)
birthDayCandles(limit,Nuber_of_elements)