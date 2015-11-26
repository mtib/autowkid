#!/usr/bin/env python3
import time
import random
import library

enableDebug = True


class Eintrag:

    def __init__(self, vorname, name, klasse):
        self.vorname = vorname
        self.name = name[:1].upper() + "."
        self.klasse = klasse

    def __str__(self):
        return "{} {} {}".format(self.vorname, self.name, self.klasse)


class Tag:

    def __init__(self, unixt):
        self.unixt = unixt
        self.title = time.strftime("%a. %d. %b", time.localtime(unixt))
        self.monat = time.strftime("%-m", time.localtime(unixt))
        self.tag = time.strftime("%-d", time.localtime(unixt))
        self.stag = time.strftime("%a", time.localtime(unixt))
        self.eintraege = []

    def addEintrag(self, eintrag):
        self.eintraege.append(eintrag)

    def __str__(self):
        return str(self.title) + " hat {} Eintraege".format(len(self.eintraege))


def sevenDayArray(now):
    tdiff = 60 * 60 * 24
    days = []
    for x in range(0, tdiff * 7, tdiff):
        days.append(Tag(now + x))
        if enableDebug:
            import testing
            print("day in list: ", days[int(x / tdiff)].title)
            for x in range(0, int(random.random() * 5)):
                days[len(days) - 1].addEintrag(testing.getRandomEintrag())
    return days


def printDayArray(da):
    for tag in da:
        print(str(tag))
        for eintrag in tag.eintraege:
            print("\t", str(eintrag))


def main(args):
    days = sevenDayArray(time.time())
    if enableDebug:
        printDayArray(days)
        library.genImage(days)


if __name__ == '__main__':
    from sys import argv
    main(argv)