def wiezaHanoi(n,pierwsze,drugie,trzecie):
    if n==1:
        print('Przesun dysk 1 z miejsca',pierwsze,"na miejsce",drugie)
        return
    wiezaHanoi(n-1,pierwsze,trzecie,drugie)
    print("Przesun dysk",n,"z miejsca",pierwsze,"na miejsce",drugie)
    wiezaHanoi(n-1,trzecie,drugie,pierwsze)

wiezaHanoi(3,'A','B','C')
