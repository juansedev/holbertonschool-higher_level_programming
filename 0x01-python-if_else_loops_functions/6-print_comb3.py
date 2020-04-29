#!/usr/bin/python3
for i in range(0, 100):
        decena = i / 10
        unidad = i % 10
        if unidad > decena:
                print('{:02d}, '.format(i), end='')
print()
