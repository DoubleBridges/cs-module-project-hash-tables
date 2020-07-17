from collections import Counter


def word_count(s):
    # # Your code here
    # curr_idx = 0
    # len_of_curr_word = 0
    # cache = {}
    # len_input = len(s)

    # # Helper function to dry up the code
    # def add_to_cache(offset):
    #     curr_word = s[curr_idx : curr_idx + (len_of_curr_word - offset)]
    #     print(
    #         "cache",
    #         cache,
    #         "ci",
    #         curr_idx,
    #         "locw",
    #         len_of_curr_word,
    #         "offset",
    #         offset,
    #         "cw",
    #         curr_word,
    #     )
    #     if curr_word in cache:
    #         cache[curr_word] = +1
    #     else:
    #         cache[curr_word] = 1

    # # Iterate through input string one character at a time
    # for i, char in enumerate(s):
    #     print(i, char)
    #     # If the last character of the string is a letter, add the word to the cache
    #     if i == len_input - 1 and char.isalpha():
    #         print("end", i, char)
    #         len_of_curr_word = +1
    #         add_to_cache(0)
    #         break
    #     # If the character is a letter or an apostrophe, add it to the word
    #     elif char.isalpha() or char == "'":
    #         print("hit", i, char)
    #         len_of_curr_word += 1
    #         # print(len_of_curr_word)
    #     # If the character is not a letter or apostrophe,
    #     # and the word length is not zero, the word is done,
    #     # add it to the cache and reset the word length
    #     else:
    #         if len_of_curr_word > 0:
    #             add_to_cache(1)
    #         len_of_curr_word = 0
    #     curr_idx += 1

    # return cache

    return dict(
        Counter(
            [
                "".join(
                    list(
                        filter(
                            lambda char: (char.isalpha() or char == "'"),
                            list(word.lower()),
                        )
                    )
                )
                for word in s.split(" ")
                if word != ""
            ]
        )
    )


if __name__ == "__main__":
    print(word_count('":;,.-+=/\\|[]{}()*^&'))
    print(word_count("a a\ra\na\ta \t\r\n"))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    # print(
    #     word_count(
    #         "This is a test of the emergency broadcast network. This is only a test."
    #     )
    # )
