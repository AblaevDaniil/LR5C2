#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def geom(*args):
    if args:
        values = [float(arg) for arg in args]
        values.sort()

        n = len(values)
        a = 1
        for item in args:
            a *= item
        return pow(a, (1/n))
    else:
        return None


if __name__ == "__main__":
    print(geom())
    print(geom(3, 8, 3, 5, 7))
    print(geom(1, 3, 8, 4, 3, 9))
    print(geom(3, 6, 5, 8, 7, 4))