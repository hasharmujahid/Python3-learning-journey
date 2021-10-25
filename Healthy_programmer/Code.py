from pygame import mixer
import datetime
from time import time, sleep


def water():
    mixer.init()
    mixer.music.load('water.ogg')
    mixer.music.play(100)
    while mixer.music.get_busy():
        s = str(input("Type 'did it' to stop the song")).lower()
        if s == 'did it':
            mixer.music.stop()

            file = open('water_log.txt', 'a')
            get_date_time = date_time()
            file.write('You drank the water at : ')
            file.write('[ ' + str(get_date_time) + ' ]')
            file.write('\n')
            file.close()
        else:
            print("the song will not stop untill you write 'did it' ")


def eyes():
    mixer.init()
    mixer.music.load('eyes.ogg')
    mixer.music.play(100)
    while mixer.music.get_busy():
        s = str(input("write 'did it' to stop the music ")).lower()
        if s == 'did it':
            mixer.music.stop()
            file = open('Eyes_log.txt', 'a')
            get_date_time = date_time()
            file.write('you perform the eyes relaxation at : ')
            file.write('[ ' + str(get_date_time) + ' ] \n')
            file.close()
        else:
            print("the song will not stop untill you write 'did it'")


def excercise():
    mixer.init()
    mixer.music.load('Excercise.ogg', 'a')
    mixer.music.play(100)
    while mixer.music.get_busy():
        s = str(input("enter 'did it' to stop the music ")).lower()
        if s == 'did it':
            mixer.music.stop()
            file = open('Excercise_log.txt', 'a')
            get_date_time = date_time()
            file.write('You took excercise break at : ')
            file.write('[ ' + str(get_date_time) + ' ] \n')
            file.close()
        else:
            print("music will not stop untill you type 'did it' ")


def date_time():
    return datetime.datetime.now()


def repeater():
    while True:
        sleep(4500 - time() % 60)
        water()
    while True:
        sleep(7200 - time() % 60)
        excercise()
    while True:
        sleep(3600 - time() % 60)
        eyes()


repeater()