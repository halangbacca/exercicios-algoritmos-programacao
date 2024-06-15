def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)

print(mdc(2, 12))
print(mdc(6, 12))
print(mdc(9, 12))
print(mdc(17, 12))
print(mdc(36, 12))
print(mdc(12, 12))