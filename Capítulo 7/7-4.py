def media_final(p1, p2, p3, p4, rec = ''):
    
    if rec != '':
        rec += (p1 * 3 + p2 * 4 + p3 * 5 + p4 * 6) / (3 + 4 + 5 + 6)
        return round(rec / 2, 1)
    else:
        return round((p1 * 3 + p2 * 4 + p3 * 5 + p4 * 6) / (3 + 4 + 5 + 6), 1)

print(media_final(3, 2, 7, 6, 8))
print(media_final(6, 4, 9, 8))
print(media_final(8, 2, 1, 2, 7))