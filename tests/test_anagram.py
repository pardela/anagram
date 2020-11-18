from anagram.anagram import generate_anagrams
from math import factorial

# to run a test - right click on the test and choose run test

#def test_generate_anagrams_empty_string():
#    assert generate_anagrams("") == ""

def test_generate_anagrams_empty_string():
    assert generate_anagrams("") == set()


#def test_generate_anagrams_onechar_string():
#    assert generate_anagrams("x") == "x"

def test_generate_anagrams_onechar_string():
    assert generate_anagrams("x") == {"x"}


#def test_generate_anagrams_twochars_string():
#    assert generate_anagrams("ab") == "ab ba"

def test_generate_anagrams_twochars_string():
    assert generate_anagrams("ab") == {"ab", "ba"}

#def test_generate_anagrams_threechars_string():
#    assert generate_anagrams("abc") == "abc acb bac bca cab cba"

def test_generate_anagrams_threechars_string():
    assert generate_anagrams("abc") == {"abc", "acb", "bac", "bca", "cab", "cba"}

#def test_generate_anagrams_fourchars_string():
#    assert generate_anagrams("biro") == "biro bior brio broi boir bori " + \
#           "ibro ibor irbo irob iobr iorb " + \
#           "rbio rboi ribo riob robi roib " + \
#           "obir obri oibr oirb orbi orib"

def test_generate_anagrams_fourchars_string():
    assert generate_anagrams("biro") == {"biro", "bior", "brio", "broi", "boir", "bori",
           "ibro", "ibor", "irbo", "irob", "iobr", "iorb",
           "rbio", "rboi", "ribo", "riob", "robi", "roib",
           "obir", "obri", "oibr", "oirb", "orbi", "orib"}

#def test_number_of_anagrams_fivechars_string():
#    assert len(generate_anagrams("abcde").split()) == factorial(5)

def test_number_of_anagrams_fivechars_string():
    assert len(generate_anagrams("abcde")) == factorial(5)