from googletrans import Translator
translator = Translator()

EnterText = input("Enter Text(Hindi to English): ")
output = translator.translate(EnterText, dest='en')
print(output.text)

EnterText = input("Enter Text(English to Hindi): ")
output = translator.translate(EnterText, dest='hi')
print(output.text)