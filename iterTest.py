it = iter(list(range(10)))
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break
