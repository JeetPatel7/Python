phone = input("Phone : ")
digit_to_letter = {

    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine",
    "0":"zero"
    
}

output = ""

for digit in phone:
     output += digit_to_letter.get(digit,"!") + " "

print(output)

''' What happens in each iteration?
First iteration:
digit = "1" → digit_to_letter.get("1", "!") returns "one"
output = "one "

Second iteration:
digit = "2" → digit_to_letter.get("2", "!") returns "two"
output = "one two "

Third iteration:
digit = "3" → digit_to_letter.get("3", "!") returns "three"
output = "one two three '''
