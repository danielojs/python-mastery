"""
Week 1 / Day 1 — Comprehensions
Exercises from the Python Mastery roadmap.
"""


# Exercise 1: Numbers divisible by 3 or 5
divisible = [n for n in range(1, 21) if n % 3 == 0 or n % 5 == 0]


# Exercise 2: Filter and uppercase filename
files = ["report.pdf", "notes.txt", "data.csv", "image.png"]

filtered = [file for file in files if file[-3:] == "csv" or file[-3:] == "txt"]


# Exercise 3: Build a dict from two lists using zip()
keys = ["name", "age", "city"]
values = ["Danielo", 27, "Bintaro"]

data = {k: v for k, v in zip(keys, values)}


# Exercise 4: Yields the first 5 squares
start = 1
stop = 20
threshold = 50
count = 5

squares = (n * n for n in range(start, stop + 1) if n * n > 50)

next(squares)
next(squares)
next(squares)
next(squares)
next(squares)


# Exercise 5: Build a multiplication table
mul = {(i, j): i * j for i in range(1, 4) for j in range(1, 4)}
