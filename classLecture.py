# import speech_recognition as sr

# lecture = []
# recognized = ''
# listening = False
# recognizer = None
# stop_listening = None


# def callback(recognizer, source):

#     try:
#         global recognized
#         recognized = recognizer.recognize_google(source)
#         global lecture
#         lecture.append(recognized)
#         print("you said ", lecture)

#     except sr.RequestError as exc:
#         print(exc)

#     except sr.UnknownValueError:
#         print("unable to recognize")


# def toggle_listening(txt_field):
#     global listening
#     global recognizer
#     global stop_listening

#     if listening:
#         txt_field.config(state='normal')
#         stop_listening()  # Stop the listening loop
#         listening = False
#         print("Microphone listening stopped")
#     else:
#         txt_field.config(state='disabled')
#         recognizer = sr.Recognizer()
#         mic = sr.Microphone()
#         with mic:
#             recognizer.adjust_for_ambient_noise(mic, duration=0.1)
#         print('Talk')
#         stop_listening = recognizer.listen_in_background(mic, callback)
#         listening = True
#         print("Microphone listening started")


# def reset_lecture():
#     global lecture
#     lecture = []


import speech_recognition as sr

lecture = []
recognized = ''
listening = False
recognizer = None
stop_listening = None


def callback(recognizer, source):
    global recognized
    global lecture

    try:
        recognized = recognizer.recognize_google(source)
        lecture.append(recognized)
        print("You said:", recognized)

    except sr.RequestError as exc:
        print(exc)

    except sr.UnknownValueError:
        print("Unable to recognize")


def toggle_listening(self):
# def toggle_listening(txt_field=None):  # Accept an argument, but don't use it
    global listening
    global recognizer
    global stop_listening

    if listening:
        stop_listening()  # Stop the listening loop
        listening = False
        print("Microphone listening stopped")
    else:
        recognizer = sr.Recognizer()
        mic = sr.Microphone()
        with mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.1)
        print('Talk')
        stop_listening = recognizer.listen_in_background(mic, callback)
        listening = True
        print("Microphone listening started")


def reset_lecture():
    global lecture
    lecture = []

# Example usage
#  # Start listening
# You can add a mechanism to stop listening after some time or based on some condition
