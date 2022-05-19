# Import data from https://www.w3schools.com/xml/cd_catalog.xml
# and store data in array
# then display the menu items
# educba.com/python-ioerror
# stackoverflow.com/questions/18962166/python-os-statfile-
# name-st-size-versus-os-path-getsizefile-name
# stackoverflow.com/questions/736043/checking-if-a-string
# -can-be-converted-to-float-in-python
# youtube.com/watch?v=r6dyk68gymk


import xml.etree.ElementTree as ET
import os
from os import path


def get_root(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    return root


def get_arrays(name, root):
    music_array = []
    for index in root.findall("CD"):
        for T in index.findall(name):
            T = index.find(name).text
            if T is None:
                print("Missing or bad data")
            else:
                music_array.append(T)
    return music_array


def get_float(root):
    price = []
    for index in root.findall("CD"):
        for T in index.findall("TITLE"):
            T = index.find("PRICE").text
            if T is None:
                print("Missing or bad data")
            else:
                try:
                    T = float(T)
                    price.append(T)
                except:
                    print("Missing numbers")
                    continue
    return price


def get_total(price):
    total = 0
    count = 0
    while count < len(price):
        total = total + (price[count])
        count = count + 1
    return total


def get_average(price, total):
    average = total/len(price)
    return average


def display_array(title, artist, country, price, year, average):
    try:
        for index in range(0, len(title)):
            print(title[index] + " - " + artist[index] + " - " +
                  country[index] + " - " + f"{price[index]:.2f}" + " - " +
                  year[index])
        print(str(len(artist)) + " items - $" +
              f"{average:.2f}" + " Average Price")
    except IndexError:
        print("Missing data")


def main():
    filename = "cd_catalog.xml"
    if path.exists(filename):
        try:
            if os.stat(filename).st_size > 0:
                if os.stat(filename).st_size <= 53:
                    print("No record was found")
                else:
                    root = get_root(filename)
                    title = get_arrays("TITLE", root)
                    artist = get_arrays("ARTIST", root)
                    country = get_arrays("COUNTRY", root)
                    price = get_float(root)
                    year = get_arrays("YEAR", root)
                    total = get_total(price)
                    average = get_average(price, total)
                    display_array(title, artist, country, price, year, average)
            else:
                print("The file is empty")
        except IOError:
            print("The file is missing")
    else:
        print("The file is missing")


main()
