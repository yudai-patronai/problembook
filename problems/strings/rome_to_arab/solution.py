roman_arab_map = [
    ('M', 1000),
    ('CM', 900),
    ('D', 500),
    ('CD', 400),
    ('C', 100),
    ('XC', 90),
    ('L', 50),
    ('XL', 40),
    ('X', 10),
    ('IX', 9),
    ('V', 5),
    ('IV', 4),
    ('I', 1),
]


def convert_to_arab(roman_str):

    if not roman_str:
        return 0
        
    for char, value in roman_arab_map:
        if roman_str.startswith(char):
            return value + convert_to_arab(roman_str[len(char):])
            
            
if __name__ == '__main__':
    
    print(str(convert_to_arab(input())))
