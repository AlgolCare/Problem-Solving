def find_location(idx, tile, x, y):
    global d
    if idx == d:
        return x, y

    if tile % 10 == 1:
        return find_location(idx + 1, tile//10, x + 2 ** idx, y)
    elif tile % 10 == 2:
        return find_location(idx + 1, tile//10, x, y)
    elif tile % 10 == 3:
        return find_location(idx + 1, tile//10, x, y + 2 ** idx)
    elif tile % 10 == 4:
        return find_location(idx + 1, tile//10, x + 2 ** idx, y + 2 ** idx)


def find_tile(idx, tile, x, y):
    global d
    if idx == d:
        return tile
    
    temp = 2 ** (d - (idx + 1))
    if x >= temp and y < temp:
        tile += 1 * 10 ** (d - (idx + 1))
        return find_tile(idx + 1, tile, x - temp, y)
    elif x < temp and y < temp:
        tile += 2 * 10 ** (d - (idx + 1))
        return find_tile(idx + 1, tile, x, y)
    elif x < temp and y >= temp:
        tile += 3 * 10 ** (d - (idx + 1))
        return find_tile(idx + 1, tile, x, y - temp)
    elif x >= temp and y >= temp:
        tile += 4 * 10 ** (d - (idx + 1))
        return find_tile(idx + 1, tile, x - temp, y - temp)

d, tile = map(int, input().split())
x, y = map(int, input().split())

l_x, l_y = find_location(0, tile, 0, 0)
if not (0 <= l_x + x < 2 ** d and 0 <= l_y - y < 2 ** d):
    print(-1)
else:
    print(find_tile(0, 0, l_x + x, l_y - y))
