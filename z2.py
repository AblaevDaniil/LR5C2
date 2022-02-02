#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def garmonich(*args):
    if args:
        values = [float(arg) for arg in args]
        values.sort()

        n = len(values)
        a = 1
        for item in args:
            a += 1 / item
        return n / a
    else:
        return None


if __name__ == "__main__":
    print(garmonich())
    print(garmonich(3, 8, 3, 5, 7))
    print(garmonich(1, 3, 8, 4, 3, 9))
    print(garmonich(3, 6, 5, 8, 7, 4))