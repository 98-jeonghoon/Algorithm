x, y, w, h = map(int, input().split())

x_value = min(x, abs(x - w))
y_value = min(y, abs(y - h))

print(min(x_value, y_value))