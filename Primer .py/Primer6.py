#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


fruits = ["apple", "peach", "orange", "banana", "melon"]
counts = [34, 25, 43, 31, 17]

plt.bar(fruits, counts)
plt.title("Fruits!")
plt.xlabel("Fruit")
plt.ylabel("Count")
plt.show()


