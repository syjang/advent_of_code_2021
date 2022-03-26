x1, x2, y1, y2 = 179, 201, -109, -63

maxY =0 
count = 0
for vvx in range(1, x2 + 1): 
    for vvy in range(y1, 300):
        vx, vy = vvx, vvy
        x =0 
        y =0
        max_y = y1

        while x <= x2 and y >= y1:

            max_y = max(max_y, y)
            if x1 <= x <= x2 and y1 <= y <= y2:
                count += 1
                maxY = max(maxY, max_y)
                break
            x += vx
            y += vy
            vx = max(0, vx - 1)
            vy -= 1

print(maxY)
print(count)