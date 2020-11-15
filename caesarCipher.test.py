import os
from caesarCipher import main


# declare and initialize total test count and passing test count
totalTests = 0
passingTests = 0

# declare curried test handler function


def testHandlerCurried(shift, message):

    # declare test handler function
    def testHandler(promptType, prompt):
        # check for valid shift input
        if promptType['prompt'] == 'shift':
            # check if shift is integer
            isInt = type(shift) is int
            if not isInt:
                return 'TypeError'

            # also check if shift is in bounds
            isInBounds = shift >= 1 and shift < 36
            if isInBounds:
                return shift
            else:
                return 'ValueError'

        # return lowercase message
        if promptType['prompt'] == 'message':
            return message.lower()

    return testHandler


# test function
def assertEqual(case, expected, actual):
    global passingTests, totalTests
    if expected == actual:
        print('✅', case, f"'{expected}'", '==', f"'{actual}'")
        passingTests += 1
    else:
        print('🚨', case, f"'{expected}'", '!=', f"'{actual}'")
    print('\n')
    totalTests += 1


# clear console
print('\033c')
# set environment
os.environ['ENV'] = 'development'


# test case 1
# valid number and lowercase message
shift = 1
message = 'hello world'
expected = 'ifmmp xpsme'
actual = main(testHandlerCurried(shift, message))
assertEqual('1. it should handle the lower bound:', expected, actual)

# test case 2
# valid number and lowercase message
shift = 35
message = 'hello world'
expected = 'gdkkn vnqkc'
actual = main(testHandlerCurried(shift, message))
assertEqual('2. it should handle the upper bound:', expected, actual)

# test case 3
# valid number and lowercase message
shift = 3
message = 'hello world'
expected = 'khoor zruog'
actual = main(testHandlerCurried(shift, message))
assertEqual('3. it should shift a message by 3 characters:', expected, actual)

# test case 4
# valid number and lowercase message
shift = 20
message = 'hello world'
expected = '1y558 g8b5x'
actual = main(testHandlerCurried(shift, message))
assertEqual('4. it should shift a message by 20 characters:', expected, actual)

# test case 5
# invalid number and lowercase message
shift = 0
message = 'hello world'
expected = 'ValueError'
actual = main(testHandlerCurried(shift, message))
assertEqual(
    '5. it should handle a shift less than the lower bound:', expected, actual)

# test case 6
# invalid number and lowercase message
shift = -3
message = 'hello world'
expected = 'ValueError'
actual = main(testHandlerCurried(shift, message))
assertEqual('6. it should handle a negative shift:', expected, actual)

# test case 7
# invalid number and lowercase message
shift = 36
message = 'hello world'
expected = 'ValueError'
actual = main(testHandlerCurried(shift, message))
assertEqual(
    '7. it should handle a shift greater than the upper bound:', expected, actual)

# test case 8
# valid number and empty message
shift = 3
message = ''
expected = ''
actual = main(testHandlerCurried(shift, message))
assertEqual('8. it should handle an empty message:', expected, actual)

# test case 9
# valid number and message with unlisted characters
shift = 3
message = "hi! isn't this great?"
expected = "kl! lvq'w wklv juhdw?"
actual = main(testHandlerCurried(shift, message))
assertEqual('9. it should handle unlisted characters:', expected, actual)

# test case 10
# valid number and message with capital letters
shift = 3
message = 'HI THERE'
expected = 'kl wkhuh'
actual = main(testHandlerCurried(shift, message))
assertEqual('10. it should handle capital letters:', expected, actual)

# test case 11
# invalid number and valid message
shift = '3'
message = 'hello world'
expected = 'TypeError'
actual = main(testHandlerCurried(shift, message))
assertEqual('11. it should handle shift of type str:', expected, actual)

# print final test count
if passingTests == totalTests:
    print('====================')
    print('😎 All tests pass 😎')
else:
    print('==============================')
    print(f'😭 Only {passingTests} of {totalTests} tests pass 😭')
print('\n')
