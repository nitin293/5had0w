#!/usr/bin/env python

def get_key(password):
    sum_ascii = 0
    sum_ = ""
    key = 0
    for element in password:
        sum_ascii += ord(element)

    for digit in str(sum_ascii):
        key += int(digit)

    return key


def algo(input_text, key):
    space = " "
    space_indices = []

    if space in input_text:
        for index in range(0,len(input_text)):
            if input_text[index]==space:
                space_indices.append(index)

    modified_text = input_text.replace(space, "")

    output_list = []

    for letter in modified_text:
        letter_index = letter_list.index(letter)
        output_index_algo = 2 * key - letter_index
        output_list.append(letter_list[output_index_algo])

    for space_index in space_indices:
        output_list.insert(space_index, space)

    return "".join(output_list)
