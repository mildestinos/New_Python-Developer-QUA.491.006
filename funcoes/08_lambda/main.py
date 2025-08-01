#lambda


pg = lambda x: x*2
pa = lambda x: x-2

#algoritimo principal

if __name__ == '__main__':
    # lista

    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # map
    print(f"Progressão aritimetica: {list(map(pa, numeros))}")
    print(f"Progressão geométrica: {list(map(pg, numeros))}")

