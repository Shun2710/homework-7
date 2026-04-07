# Task 7.2

def correct_sentence(text):

    text = text[0].upper() + text[1:]

    if not text.endswith('.'):
        text += '.'

    return text

print(correct_sentence('Hello'))
print(correct_sentence("Greetings. Friends."))