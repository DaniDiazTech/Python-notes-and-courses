def first_letter(my_list):
    the_list = []
    
    for word in my_list:
        assert type(word), f"{word} is not a string"
        assert len(word) > 0, "an empty string is not allowed"

        the_list.append(word[0])
    return the_list

print(first_letter(["ha", "k", "nothing"]))
