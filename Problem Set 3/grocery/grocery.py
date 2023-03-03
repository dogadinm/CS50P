grocery ={}
while True:
    try:
        word = input().upper()
        if word in grocery:
            grocery[word] += 1
        else:
            grocery[word] = 1
    except EOFError:
        for key in sorted(grocery):
            print(grocery[key], key)
        break