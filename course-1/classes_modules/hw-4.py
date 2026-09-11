def file_type(s):
    index = s.rfind(".")
    return s[index+1:] if index != -1 else ""