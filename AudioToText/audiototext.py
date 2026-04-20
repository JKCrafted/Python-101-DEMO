import speech_recognition

file_path = input("File Path: ")

for i in range(5):
    try:
        recogniser = speech_recognition.Recognizer()

        recognised_audio=speech_recognition.AudioFile(file_path)
        with recognised_audio as source:
            audio = recogniser.record(source)

        recognised_text = recogniser.recognize_google(audio)
        print("Text: "+recognised_text)
    except Exception as error:
        recognised_text = "Error No Text"
    if recognised_text != "Error No Text": break