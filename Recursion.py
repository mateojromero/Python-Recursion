
def int_division(num, div):
    if num < div: 
        return 0
    else:
        return 1 + int_division(num - div, div)

def get_even_ints(int_list):
    if len(int_list) == 0:
        return []
    elif int_list[0] % 2 == 0:
        return [int_list[0]] + get_even_ints(int_list[1:])
    else:
        return get_even_ints(int_list[1:])


def count_vowels(text):
    lower_list = text.lower()
    list_vowels = ['a', 'e', 'i', 'o', 'u']
    if len(text) == 0:
        return 0
    elif lower_list[0] in list_vowels:
        return 1 + count_vowels(lower_list[1:])
    else:
        return count_vowels(lower_list[1:])

def reverse_str(text):
    if len(text) < 2:
        return text
    return reverse_str(text[1:]) + text[0]

def remove_seq(text, seq):
    if len(text) < len(seq):
        return text
    if text[:len(seq)] == seq:
        return remove_seq(text[len(seq):], seq)
    else:
        return text[0] + remove_seq(text[1:], seq)
