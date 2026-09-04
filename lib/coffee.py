#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        self.size = size
        self.price = price

    def __repr__(self):
        return(f"The coffee of size: {self.size} is priced at: {self.price}")

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        sizes = ["small", "medium", "large"]
        if value.lower() in sizes:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")

    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price += 1
            

large_coffee = Coffee("Large", 290)
print(large_coffee)
large_coffee.tip()
print(large_coffee)

