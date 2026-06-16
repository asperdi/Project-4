def deduce_type(value: str):
    
    if value == "True":
        return True
    if value == "False":
        return False

    if value.isdigit():
        return int(value)

    try:
        return float(value)
    except ValueError:
        pass

    return value


def decompose(text: str):
    return [deduce_type(v) for v in text.split()]


if __name__ == "__main__":
    text = input("Write a string: ")

    result = decompose(text)

    print("Recognized and converted elements:", result)
