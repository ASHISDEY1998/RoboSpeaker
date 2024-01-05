import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()

    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    while True:
        text_input = input("Enter the text you want to convert to speech: ")
        if text_input == 'q':
            text_to_speech("Bye bye Friends")
            break

        text_to_speech(text_input)
