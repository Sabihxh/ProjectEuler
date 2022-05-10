def trianglular_numbers(no_of_triangular_numbers):
    tri_num_list = []
    for n in range(1, no_of_triangular_numbers + 1):
        tri_num = 0.5 * n * (n + 1)
        tri_num_list.append(tri_num)

    return list(map(int, tri_num_list))


def convert_words_to_nums(word):
    word_value = 0
    for letter in word:
        letter_value = ord(letter.lower()) - 96
        word_value += letter_value
    return word_value


def main():
    list_of_tri_nums = trianglular_numbers(30)
    no_of_tri_words = 0
    a_file = open("words.txt", "r")
    list_of_words = [word.strip().replace('"', "") for word in a_file.read().split(",")]
    for word in list_of_words:
        word_value = convert_words_to_nums(word)
        if word_value in list_of_tri_nums:
            no_of_tri_words += 1

    print(no_of_tri_words)
    return no_of_tri_words


main()
