

def generate_meeting_link(input_str):
    if len(input_str) != 10:
        raise
    first = input_str[:3]
    second = input_str[3:7]
    third = input_str[7:]
    return f"meet.google.com/{first}-{second}-{third}"


def shift_input(input_str, distance):
    """
        Used ord() to get an integer representation of char
        Substracted distance from this number
        Used chr() to convert it back to a character
        Alphabet  has 26 letters
        97 to 122 are the ASCII number equivalent to 'a' to and 'z'
        Example:
            a = 97
            97 - 97 - 1 = -1
            -1 % 26 = 25
            25 + 97 = 122
            122 = z
    """
    return ''.join(chr((ord(char) - 97 - distance) % 26 + 97) for char in input_str)


def kor2eng(input_str):
    kor2eng_dict = {
        'ㅂ': 'q', 'ㅈ': 'w', 'ㄷ': 'e', 'ㄱ': 'r', 'ㅅ': 't',
        'ㅛ': 'y', 'ㅕ': 'u', 'ㅑ': 'i', 'ㅐ': 'o', 'ㅔ': 'p',
        'ㅁ': 'a', 'ㄴ': 's', 'ㅇ': 'd', 'ㄹ': 'f', 'ㅎ': 'g',
        'ㅗ': 'h', 'ㅓ': 'j', 'ㅏ': 'k', 'ㅣ': 'l', 'ㅋ': 'z',
        'ㅌ': 'x', 'ㅊ': 'c', 'ㅍ': 'v', 'ㅠ': 'b', 'ㅜ': 'n',
        'ㅡ': 'm',

    }

    return ''.join(kor2eng_dict[char] if char in kor2eng_dict.keys() else char for char in input_str)


def clean_input(input_str):
    # Lowercase
    input_str = input_str.lower()

    # Replace korean letter to english letter
    input_str = kor2eng(input_str)

    return input_str


def main():
    input_str = input("Enter encoded string: ")
    distance = int(input("Enter distance: "))

    cleaned_input_str = clean_input(input_str)
    shifted_input_str = shift_input(cleaned_input_str, distance)
    meeting_link = generate_meeting_link(shifted_input_str)
    print("Your meeting link is https://" + meeting_link)


if __name__ == "__main__":
    main()
