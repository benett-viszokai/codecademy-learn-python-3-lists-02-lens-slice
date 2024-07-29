# Len's Slice

# Creating an initial list of toppings & prices
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]

# Counting the 2$ prices
num_two_dollar_slices = prices.count(2)

# Toppings' length
num_pizzas = len(toppings)

# Printing out a message
print('We sell ' + str(num_pizzas) + ' different kinds of pizza!')

# Creating a new two dimensional list from prices and toppings
pizza_and_prices = [
  [prices[0], toppings[0]],
  [prices[1], toppings[1]],
  [prices[2], toppings[2]],
  [prices[3], toppings[3]],
  [prices[4], toppings[4]],
  [prices[5], toppings[5]],
  [prices[6], toppings[6]],
]

# Sorting and slicing

# Sorting pizza_and_prices in increasing price
pizza_and_prices.sort()

# First element
cheapest_pizza = pizza_and_prices[0]

# Last element
priciest_pizza = pizza_and_prices[-1]

# Removing the last element
pizza_and_prices.pop()

# Adding a new topping
pizza_and_prices.insert(4, [2.5, "peppers"])

# Three cheapest pizza
three_cheapest = pizza_and_prices[:3]

print(three_cheapest)
