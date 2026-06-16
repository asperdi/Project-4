import random

def function(input):
    return ''.join(chr(c).upper() for c in sorted(input, reverse=True))
    
    

if __name__ == "__main__":
    input = random.sample(range(97, 123), 26)
    
    output = function(input)
    
    print(output)
