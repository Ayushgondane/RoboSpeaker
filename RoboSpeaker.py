import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboSpeaker Created by Ayush")
    
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    
    while True:
        x = input("Enter what you want to speak (type 'q' to quit): ")
        if x.lower() == "q":
            print("Goodbye!")
            break
        engine.say(x)
        engine.runAndWait()
