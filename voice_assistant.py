
from speak_and_listen import speak, hear_me
import re

#pythex, pag web util para RE (regular expretions)

def identify_name(text):
    name = None
    patterns = ["me llamo ([A-Za-z]+)", "ni nombre es ([A-Za-z]+)", "^([A-Za-z]+)$"]
    for pattern in patterns:
        try:
            name = re.findall(pattern, text)[0]
        except IndexError:
            pass
    
    return name


def main():
    speak("Hola, como estas")
    text = hear_me()
    #regular expretions
    name = identify_name(text)
    if name:
        speak("Encantado de conocerte, {}".format(name[0]))
    else:
        speak("Pues mira, la verdad que no te entiendo, puedes quitarte la patata de la boca?")


if __name__=="__main__":
    main()