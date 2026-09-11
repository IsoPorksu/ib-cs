while (phrase := input("my-calc: ")) != "":
    [a_str, op, b_str] = phrase.split()
    if op == "-": print(float(a_str)-float(b_str))
    if op == "+": print(float(a_str)+float(b_str))
    if op == "*": print(float(a_str)*float(b_str))
