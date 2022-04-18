# -*- coding: utf-8 -*-
"""This module contains a program that behaves as below. 
Client2:
    Reads intergers from the pipe and calculate the Median value of the integers.
"""
from statistics import median


def main():
    """Read data from PIPE and get median"""
    data = input()
    print(f'Median is {median(eval(data))}')


if __name__ == '__main__':
    main()
