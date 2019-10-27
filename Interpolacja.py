# Temperatura
T = [100.00, 644.00, 1188.00, 1732.00, 2276.00, 2820.00, 3364.00, 3908.00, 4452.00, 5000.00]
# Entropia
f = [25.9914, 54.6359, 59.6281, 62.8990, 65.3650, 67.3605, 69.0447, 70.5066, 71.8018, 72.9762]
# stopień wielomianu
k = len(T) - 1


def interpolation_l(x):
    b = 0
    for j in range(k+1):
        c = 1
        for m in range(k+1):
            if m != j:
                c = c * (x - T[m])/(T[j] - T[m])
                # print(f"c: {c}")
        b = b + f[j] * c
        # print(f"b: {b}")
    return b


print(interpolation_l(100))
print(interpolation_l(4999))
