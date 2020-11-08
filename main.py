import pyttsx3
import pdfplumber 
import os
import time
import uuid
import pathlib

def text_to_speech(text, gender):
    """
    Function to convert text to speech
    :param text: text
    :param gender: gender
    :return: None
    """
    # Opening pdf and reading text
    raw_str = ""
    u = ""
    with pdfplumber.open(text) as pdf:
        total_pages = pdf.pages  # getting total pages in pdf

        # iterating over all pages in pdf to read text
        for itr in range(len(total_pages)):
            first_page = pdf.pages[itr]

            # Applying exception due to some content (Images)
            # creating Object in extract_text function,
            # which is not required
            try:
                raw_str = raw_str + "" + first_page.extract_text()
            except Exception as e:
                print(e)

    # Printing text which will going to converted into audio
    print(f"Text we fetch from {text} ->" + raw_str)

    voice_dict = {'Male': 0, 'Female': 1}
    code = voice_dict[gender]

    engine = pyttsx3.init()

    # Setting up voice rate
    engine.setProperty('rate', 120)

    # Setting up volume level  between 0 and 1
    engine.setProperty('volume', 0.9)

    # Change voices: 0 for male and 1 for female
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[code].id)

    unique = uuid.uuid1()

    uni = str(unique)

    un = uni[:-9]
    u = un+'.mp3'

    engine.save_to_file(raw_str , u)
    time.sleep(5)
    engine.say("Download Complete!")
    
    # time.sleep(5)
    # os.startfile(u)
    #     os.startfile("913c9629-2191-11eb-8a99-a0b3cc.mp3")
    # else:
    #     print ("!exist")
    
    # cwd = os.path.abspath(os.getcwd())
    # abpath = cwd + '\\' + u
    
    # print (cwd)
    engine.runAndWait()
    os.startfile(u)
