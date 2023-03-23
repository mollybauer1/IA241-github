"""
lab 9 instance
"""
from lab9_class import my_stat
import numpy as np

my_cal_instance = my_stat()

print(my_cal_instance.cal_sigma(5,3))
print(my_cal_instance.cal_pi(5,3))
print(my_cal_instance.cal_fact(5))
print(my_cal_instance.cal_perm(5,2))

print(np.math.factorial(999))
print(my_cal_instance.cal_fact(999))




