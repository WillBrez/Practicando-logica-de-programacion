def anagrama(p1, p2):
    p1 = set(p1)
    p2 = set(p2)
    return p1 == p2


resultado = anagrama("amor", "roma")
print("Esta palabra es anagrama: ", resultado) 