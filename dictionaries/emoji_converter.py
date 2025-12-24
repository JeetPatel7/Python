message = input("> ")

words = message.split()
# this converts all individual words from message into list 

# print(words) 
# > hello i am
# ['hello', 'i', 'am']


emoji = {

    ":)" : "😊",
    ":(" : "😒"
}
output = ""

for word in words:
    output += emoji.get(word,word) + " "

print(output)
