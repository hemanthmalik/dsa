def is_anagram(s1, s2):
    s1, s2 = str(s1), str(s2)
    s1_len, s2_len = len(s1), len(s2)
    s1_chars, s2_chars = {}, {}

    if s1_len != s2_len: return False

    curr_index = 0
    while curr_index < s1_len:
        curr_s1_val, curr_s2_val = s1[curr_index], s2[curr_index]
        s1_chars[curr_s1_val], s2_chars[curr_s2_val] = s1_chars.get(curr_s1_val, 0) + 1, s1_chars.get(curr_s1_val, 0) + 1
        curr_index += 1

    return s1_chars == s2_chars

print(is_anagram('ether', 'earth'))
        