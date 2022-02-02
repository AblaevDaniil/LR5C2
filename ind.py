#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def summ(*args):
    if args:
        total = 0
        count = 0

        values = [int(arg) for arg in args]

        for idx in values:
            if idx == 0:
                count += 1
            if count == 1:
                total += idx
            if count == 2:
                return total
    else:
        return None


if __name__ == "__main__":
    print(summ(3, 8, 3, 0, 7, 15, 0, 30,))
    print(summ(1, 0, 8, 4, 0, 9))
    print(summ(3, 0, 5, 8, 7, 0))