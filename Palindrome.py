
def pal(txt):
    if txt == txt[::-1]:
        return True
    else:
        return False

print(pal('racecar'))
