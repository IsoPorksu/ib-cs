def last_dot_kept(s):
    t = s
    count = t.count(".")
    return t.replace(".", "-dot-", count-1)