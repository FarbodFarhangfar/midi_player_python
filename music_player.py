import os
import pygame
from pygame import mixer
from mutagen.mp3 import MP3
import queue
import time
import threading
from random import shuffle
from tkinter import *


class tree:
    t = []

    def insert_adress(self, adress):
        file = os.listdir(adress)
        temp = []
        for files in file:
            if os.path.isdir(adress + '/' + files):
                temp.append(self.insert_adress(adress + '/' + files))
            temp.append(adress + '/' + files)
        return temp

    def get_files(self, tem):
        self.t.append(self.insert_adress(tem))
        return self.t

    def show(self):
        print(self.t)


# class tree
# colecting files and folders and put them in a tree


def mp3_recognize(ls):
    result = []
    for file in ls:
        temp = []
        aa = -1
        if (os.path.isfile(file)):
            st = ""
            while (file[aa] != "."):
                temp.append(file[aa])
                aa = aa - 1
            temp.reverse()
            for i in temp:
                st = st + i
            if (st == "mp3"):
                result.append(file)
    return result


# its recognize a file is mp3 or not


mixer.init()  # install mixer from pygame


def music_length(f):
    audio = MP3(f)
    l = int(audio.info.length) + 1
    return l


# mp3 files length


music_l = []
ttemp = []


def making_list(file):
    for i in file:

        if type(i) == list:

            making_list(i)
        else:
            ttemp.append(i)
    return ttemp


# make list out of tree


def making_queue(mq, ml):
    for i in ml:
        mq.put(i)


# make a queue out of list


def play(file):
    mixer.music.load(file)
    mixer.music.play()


# play mp3 file

def play_p(file):
    global n
    audio = MP3(file)
    n = audio.info.length
    return n


# get length for threads

def po():
    global n
    time.sleep(n)
    mixer.music.stop()


# sleep for pygame playing

def plat_by_thread(file):
    n = play_p(file)
    t = threading.Thread(target=po)
    t.start()


# play pygame mixer in background so you can have a input

def clear():
    for i in range(20):
        print()


def sclear():
    for i in range(2):
        print()


# pycharm doesnt have cls
# get some lines to feel like cls


music_q = queue.Queue()
music_temp = queue.Queue()
# define 2 queue

file_adress = input("enter your directory :  ")
while not os.path.exists(file_adress):
    print("invalid adress")
    print("please enter valid adress")
    file_adress = input("enter your directory :  ")
# getting directory and know if its exist or not


# use functions
a = []
mml = []
y = tree()
a = y.get_files(file_adress)[:]
mml = a[0]
tmml = making_list(mml)
nmml = mp3_recognize(tmml)
music_l = nmml[:]


# sort functions
def alphabetical(temp):
    return sorted(temp, key=lambda v: (v.upper(), v[0].islower()))


mm = alphabetical(nmml)
making_queue(music_q, mm)
singer_list = []


def singer_name():
    temp_l = []
    for i in music_l:
        temp = []
        for j in range(len(i)):
            if i[j] == "–":
                break
        temp = i[j + 2:-1]
        temp_l.append(temp)
    mm = sorted(temp_l, key=lambda v: (v.upper(), v[0].islower()))
    for i in mm:
        for j in music_l:
            if i in j:
                singer_list.append(j)
                break


singer_name()

# clear()

con = "0"
ncom = None
clear()


def printing1():
    print("1.play")
    print("2.next")
    print("3.previous")
    print("4.personalized")
    print("5.repeat")
    print("6.showfile")
    print("7.search")
    print("8.exit")
    print("9.show tree")


def printing2():
    print("1.stop")
    print("2.next")
    print("3.previous")
    print("4.personalized")
    print("5.repeat")
    print("6.showfile")
    print("7.search")
    print("8.exit")
    print("9.show tree")


# out puts
printing1()

x = 0
inget = True
rra = False
stack = []  # STACK HERE
fl = 2
tempstack = []
reap = False

# play a music file
# if you change input or wiat untill the end it will be stop
while True:
    print(con)
    if (inget):
        if con != "2":
            clear()
        printing1()
        print("enter a number :")
        print("enterd")
        print()
        print(music_q)
        con = input()
    if con == "1":  # play
        print("yeah")
        if mixer.music.get_busy():
            mixer.music.stop()
            con = input()
            inget = True
        else:
            while not music_q.empty():
                file = music_q.get()
                print(file)
                play(file)
                plat_by_thread(file)
                savet = file
                x = x + 1
                clear()
                print("now playing :" + file)
                printing2()
                print("enter a number :")
                con = input()
                inget = False
                savet = file
                fl = 2
                if con == "1":  # FOR STOP get a item from queue and again put it back in front by using temp queue
                    mixer.music.stop()
                    music_temp.put(file)
                    while not music_q.empty():
                        a = music_q.get()
                        music_temp.put(a)
                    while not music_temp.empty():
                        a = music_temp.get()
                        music_q.put(a)
                    inget = True
                    break
                elif con == "3":
                    music_temp.put(file)
                    while not music_q.empty():
                        a = music_q.get()
                        music_temp.put(a)
                    while not music_temp.empty():
                        a = music_temp.get()
                        music_q.put(a)
                    break
                elif con == "4" or con == "5" or con == "6" or con == "7" or con == "8":
                    mixer.music.stop()
                    inget = True
                    break
                elif con == "2":
                    stack.append(file)
                    if music_q.empty():
                        break
                    con = 1

    if con == "2":
        sclear()
        print("nothing is playing")

    if con == "3":
        print(stack)
        if mixer.music.get_busy():
            nn = len(stack)
            if nn != 0:
                if nn == 1:
                    file = stack[0]
                    print("saaaaaa")
                else:
                    file = stack.pop()
                    print("ssssssss")
                play(file)
                plat_by_thread(file)
                # clear()
                print("now playing :" + file)
                printing2()
                print("enter a number :")
                stack.append(file)
                con = input()
                con = "1"
                inget = False
            mixer.music.stop()

        else:
            print("nothing is playing")

    # personlize
    if con == "4":
        print("1.alphabetical")
        print("2.singer name")
        print("3.shuffle")
        ncon = input()
        if ncon == "1":
            mm = alphabetical(nmml)
            making_queue(music_q, mm)
        elif ncom == "2":
            making_queue(music_q, singer_list)
        elif ncom == "3":
            mtemp = shuffle(music_l)
            making_queue(music_q, mtemp)

    # repeat
    if con == "5":
        ncom == input()
        if ncom == "2":
            making_queue(music_q, music_l)
            con = 1
            inget = False
        if ncom == "1":
            while TRUE:
                play(i)
                plat_by_thread(savet)
                m = input()
                if m != ".":
                    break
        if ncom == "3":
            while True:
                print("type exit")
                file = music_q.get()
                play(i)
                plat_by_thread(savet)
                m = input()
                music_q.put(file)
                if m != "exit":
                    break

    # search
    if con == "7":

        search = input(" enter ")
        for i in music_l:
            if search in i:
                print("do you want to play this (y) or (n)")
                an = input()
                if an == "y":
                    play(i)
                    plat_by_thread(i)
                    break
                else:
                    pass

    if con == "8":
        break
    if con == "9":
        t = tree()
        t.show()
