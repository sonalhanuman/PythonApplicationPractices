def generate_sentence(phrase):
    capitalized = phrase.capitalize()
    interogatives = ('how', 'what', 'why')
    if phrase.startswith(interogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)
finalList = []
while True:
    user_input = input('Please key in your phrase.')
    if user_input == "\end":
        break
    else:
        finalList.append(generate_sentence(user_input))
print(" ".join(finalList))