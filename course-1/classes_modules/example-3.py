def find_all(s, sub):
    start_index = 0; indices = []
    while start_index <= len(s): 
        found_index = s.find(sub, start_index)
        if found_index == -1: return indices
        indices.append(found_index)
        start_index = found_index + 1

s = "ababab"
print(find_all(s, "aba"))
print(find_all(s, "ab"))
print(find_all(s, "b"))