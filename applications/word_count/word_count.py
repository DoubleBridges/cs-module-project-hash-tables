from collections import Counter


def word_count(s):
    # Your code here
    cache = {}

    word_list = s.split()

    for word in word_list:
        sanitized_word = "".join(
            list(
                filter(
                    lambda char: (char.isalpha() or char == "'"), list(word.lower()),
                )
            )
        )
        if sanitized_word in cache:
            cache[sanitized_word] += 1
        else:
            cache[sanitized_word] = 1

    return {key: cache[key] for key in cache.keys() if key != ""}

    # return dict(
    #     Counter(
    #         [
    #             "".join(
    #                 list(
    #                     filter(
    #                         lambda char: (char.isalpha() or char == "'"),
    #                         list(word.lower()),
    #                     )
    #                 )
    #             )
    #             for word in s.split(" ")
    #             if word != ""
    #         ]
    #     )
    # )


if __name__ == "__main__":
    print(word_count('":;,.-+=/\\|[]{}()*^&'))
    print(word_count("a a\ra\na\ta \t\r\n"))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(
        word_count(
            "This is a test of the emergency broadcast network. This is only a test."
        )
    )
