# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 14:53:48 2018

@author: AMAN
"""

from statistics import mean
from scipy import stats

Estimates=[1000,1010,1794,574,1475,1548,1489,1569,1585,1438,1585,
           1478,1487,1587,1487,1548,1478,1487,1347,1387,1689,1709,140,189,170,159,168,154,160,149,500,548,436,326,548,448,674,324,464,327,438,833,878,787,873,635,425,
           463,564,564,243,160,326,865,986]

Estimates.sort()
m=stats.trim_mean(Estimates,0.1)
print(m)