translations = {
  "hello":"hola",
  "thank you":"gracias",
  "sorry":"lo siento",
  "goodbye":"adios",
  "yes":"si",
  "no":"no",
  "dog":"perro",
  "cat":"gato"
}
done = False

print('Type "done" at any time to exit')

while not done:
  word = input("Please enter an English word to Translate. ")
  word = word.lower()
  
  if word == "done":
    done = True
  elif word in translations:
    print(translations[word])
  else:
    print("Error, word is not in Dictionary.")