#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or len(str) <= n or str is None:
        return str

    get_char = str[n]
    new_str = str.replace(get_char, '')
    return new_str
