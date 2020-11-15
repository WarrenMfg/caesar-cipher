import os


# initialize characters
characters = [
    'a', 'b', 'c', 'd', 'e', 'f',
    'g', 'h', 'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p', 'q', 'r',
    's', 't', 'u', 'v', 'w', 'x',
    'y', 'z', '0', '1', '2', '3',
    '4', '5', '6', '7', '8', '9'
]


# declare user input type conversion function
def handleUserInput(promptType, prompt):
    # if prompt is for character shift
    if promptType['prompt'] == 'shift':
        # request until valid input is received
        while True:
            try:
                # prompt user
                val = input(prompt)
                # attempt to convert to int
                val = int(val)
                # check if in bounds
                if val >= 1 and val < 36:
                    return val
                else:
                    raise ValueError()

            # not an integer or out of bounds
            except ValueError:
                # provide feedback but continue looping
                print('🚨 Please enter a valid number')

    # if prompt is for message
    if promptType['prompt'] == 'message':
        # return lowercase string
        return input().lower()


# declare character shift function
def shiftCharacter(char, shift):
    try:
        # try to find index of char in characters array
        index = characters.index(char)
        length = len(characters)
        # if shifted index is out of bounds
        if (index + shift) >= length:
            # start from beginning and return shifted char
            newIndex = (index + shift) - length
            return characters[newIndex]
        else:
            # otherwise, return shifted char
            return characters[index + shift]
    except ValueError:
        # if no index of char is found, just return char
        return char


# declare main function
def main(cb):
    # get environment (production or test)
    ENV = os.environ['ENV']

    # welcome user
    if ENV == 'production':
        print('\n👑 Welcome to the Caesar Cipher! 👑\n')

    # prompt for shift integer
    shift = cb({'prompt': 'shift'},
               'Please enter a number between 1 and 35 (inclusive) >>> ')
    # check for 'Invalid Input' (for test cases)
    if shift == 'ValueError' or shift == 'TypeError':
        print(f'Your number is a {shift}')
        return shift

    # prompt for message to cipher and convert to lowercase
    if ENV == 'production':
        print('\nPlease enter a message to cipher:')
    message = cb({'prompt': 'message'}, None)

    # declare result variable and initialize to empty string
    result = ''

    # iterate over message characters
    for char in message:
        # shift each char and build result
        result += shiftCharacter(char, shift)

    # print ciphered message
    if ENV == 'production':
        print('\nYour ciphered message is:')
        print(f'{result}\n')
    else:
        print(
            f"Your message '{message}' with a shift of {shift} has been ciphered to '{result}'")
        # return result for tests
        return result


if __name__ == '__main__':
    # clear console
    print('\033c')
    # set production mode
    os.environ['ENV'] = 'production'
    # invoke main function
    main(handleUserInput)
