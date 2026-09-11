def dashify_substring(s, sub):
    new = f"-{sub}-"
    t = s.replace(sub, new, 1)
    return(t)