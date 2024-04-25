
def test_int_division():
    from lab03 import int_division
    
    assert int_division(20, 4) == 5
    assert int_division (4, 16) == 0
    assert int_division (35,7) == 5
    assert int_division (56, 7) == 8
    assert int_division (64, 8) == 8

def test_get_even_ints():
    from lab03 import get_even_ints

    assert get_even_ints([]) == []
    assert get_even_ints([1,2,3,4,5]) == [2, 4]
    assert get_even_ints([22, 33, 44, 55]) == [22, 44]

def test_count_vowels():
    from lab03 import count_vowels
    
    assert count_vowels('house') == 3
    assert count_vowels('Thursday') == 2
    assert count_vowels('Strawberry') == 2
    assert count_vowels('Due') == 2
    assert count_vowels('Later') == 2

def test_reverse_string():
    from lab03 import reverse_str
    
    assert reverse_str('a') == 'a'
    assert reverse_str('hello') == 'olleh'
    assert reverse_str('today') == 'yadot'
    assert reverse_str('house') == 'esuoh'

def test_remove_seq():
    from lab03 import remove_seq
    
    assert remove_seq('a', 'red') == 'a'
    assert remove_seq('strawberry', 'berry') == 'straw'
    assert remove_seq('watermelon', 'ter') == 'wamelon'
