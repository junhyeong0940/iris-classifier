from __future__ import annotations
import collections
from dataclasses import dataclass, asdict
from typing import Optional, Counter, List
import weakref
import sys



test_sample
x = Sample(3,5,4,9)
print(x)
Sample(sepal_length = 3, sepal_width = 5 ,petal_length = 4, petal_width = 9)

test_TrainingKnownSample
s1 = TrainingKnownSample(sepal_length=5.4, sepal_width=3.3, petal_length=1.9, petal_width=1.5, species="Iris-setosa")
print(s1)
TrainingKnownSample(sepal_length=5.4, sepal_width=3.3, petal_length=1.9, petal_width=1.5, species='Iris-setosa')

#바람직하지 않은 테스트
s1.sepal_length = 0 
print(s1)
TrainingKnownSample(sepal_length=0, sepal_width=3.5, petal_length=1.4, petal_width=0.2, species='Iris-setosa')

test_TestingKnownSample = 
s2 = TestingKnownSample(
sepal_length=3.2, sepal_width=5.6, petal_length=4.1, petal_width=0.9, species="Iris-setosa")
print(s2)
TestingKnownSample(sepal_length=3.2, sepal_width=5.6, petal_length=4.1, petal_width=0.9, species='Iris-setosa', classification=None)

test_UnknownSample =
u = UnknownSample(sepal_length=3.2, sepal_width=7.2, petal_length=6.1, petal_width=0.4, classification=None)
print(u)
UnknownSample(sepal_length=3.2, sepal_width=7.2, petal_length=6.1, petal_width=0.4, classification=None)

__test__ = {name: case for name, case in globals().items() if name.startswith("test_")}
