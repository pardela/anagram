"""def generate_anagrams(input_string):
    len_string = len(input_string);
    if len_string == 0:
        return "";
    elif len_string == 1:
        return input_string;
    else:
        index_char = 0;
        anagrams_string = "";
        space = "";
        for char in input_string:
            substring = input_string[0:index_char] + \
                        input_string[index_char + 1:len_string];
            substring_anagram = generate_anagrams(substring);
            for string in substring_anagram.split():
                anagrams_string = anagrams_string + space + char + string;
                space = " ";
            index_char += 1;
        return anagrams_string;"""

def generate_anagrams(input_string):
    len_string = len(input_string);
    anagrams = set();
    if len_string == 1:
        anagrams.add(input_string);
    elif len_string > 1:
        index_char = 0;
        for char in input_string:
            substring = input_string[0:index_char] + \
                        input_string[index_char + 1:len_string];
            subset_anagram = generate_anagrams(substring);
            for string in subset_anagram:
                anagrams.add(char + string);
            index_char += 1;
    return anagrams;


