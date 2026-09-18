def max_char_rep(s):
    # Return the length of the longest substring of repetitive characters
    """ Idea:
    * set longest to 1
    * get the first char of the string
    * check against the previous char of the string (or "" if it's the first char)
    * if it's the same, increment counter and keep going
    * if counter is bigger than longest, set longest to counter
    * repeat with the next char of the string
    * keep going until the end of the string
    * return longest
    """
    longest_chain = 0
    counter = 1
    prev_char = ""
    for i in range(len(s)):
        current_char = s[i]
        if current_char == prev_char: counter += 1
        if counter > longest_chain: longest_chain = counter
        if current_char != prev_char: counter = 1
        prev_char = current_char
    return longest_chain

s = "ababab"
print(max_char_rep("abcd")) # 1
print(max_char_rep("abbbcdd")) # 3
print(max_char_rep("abbbcddddd")) # 5
print(max_char_rep("")) # 0