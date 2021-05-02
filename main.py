
# Task 1
"""
Make a program that has some sentence (a string) on 
input and returns a dict containing all unique words
 as keys and the number of occurrences as values. 
"""
# 'hello world and hello world but hello world is'
# Так и не понял как можно сделать эту программу с вводом от пользователя.
def count_word(str):
    count = dict()
    word = str.split()
    for words in word:
        if words in count:
            count[words] += 1
        else:
            count[words] = 1
    return count
print(count_word('hello world and hello world but hello world is'))



# Task 2
"""
Create a function which takes as input two dicts with structure
mentioned above, then computes and returns the total price of stock.
"""

def stok(stock_shop):
    sum = 0
    for a in stock_shop:
        sum = sum + stock_shop[a]
    return sum


stock_shop = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}

def kart(price):
    sum = 0
    for b in price:
        sum = sum + price[b]
    return sum

price = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}

def total_price(price, cost):
    sum = 0
    for o in price:
        for c in cost:
            sum = sum + price[o] + cost[c]
    return sum
print('Sum: ', total_price(price, stock_shop))
print('Sum:', stok(stock_shop))
print('Sum:', kart(price))


#Task 3


