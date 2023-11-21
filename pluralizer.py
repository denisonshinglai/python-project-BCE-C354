def pluralize_word(number, word):
    if number == 1:
        return f"{number} {word}"
    elif word.endswith("fe"):
        return f"{number} {word[:-2]}ves"
    elif word.endswith("y") and not (word.endswith("ay") or word.endswith("oy") or word.endswith("ey") or word.endswith("uy")):
        return f"{number} {word[:-1]}ies"
    elif word.endswith("sh") or word.endswith("ch"):
        return f"{number} {word}es"
    elif word.endswith("us"):
        return f"{number} {word[:-2]}i"
    elif word.endswith("ay") or word.endswith("oy") or word.endswith("ey") or word.endswith("uy"):
        return f"{number} {word}s"
    else:
        return f"{number} {word}s"

if __name__ == "__main__":
    # Example usage
    number_input = int(input("Enter a non-negative number: "))
    word_input = input("Enter a singular noun: ")

    result = pluralize_word(number_input, word_input)
    print(f"The pluralized form is: {result}")

