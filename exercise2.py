def filter_letters(ascii_code):
    return [
        chr(k).upper()
        for i, k in enumerate(ascii_code, start=1)
        if i % 2 == 1 and k > ord('M')
    ]
    
    


if __name__ == "__main__":
    # Przykładowe dane wejściowe
    ascii_code = list(range(65, 91)) + list(range(97, 123)) 
    result = filter_letters(ascii_code)
    print(result)
