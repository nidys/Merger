import os
import sys
import re
from Merger import Merger
from LiteralParser import LiteralParser


def getLiteralParser(fileName):
    print(fileName)
    fd = open(fileName, "r")
    parser = LiteralParser(fd.read())
    fd.close()
    return parser


def test(fileName1, fileName2):
    try:
        parser1 = getLiteralParser(fileName1)
        parser2 = getLiteralParser(fileName2)

        # print(len(parser1.lines))
        # print(len(parser2.lines))
    except Exception as e:
        print "Failure:" + str(e)
    print "Good byte..."


def merge_test(fileName1, fileName2):
    merger = Merger()
    file1 = open(fileName1, "r")
    file2 = open(fileName2, "r")
    merger.parseFirst(file1.read())
    merger.parserSecond(file2.read())
    file1.close()
    file2.close()

    while merger.hasBothNextBlock():
        if merger.isBlockConflict():
            print(r'Conflict=#%s#%s#' % (merger.getBlockOfFirst(), merger.getBlockOfSecond()))
        else:
            print('Merged  =#%s#' % merger.getBlockOfThird())
    print('First rest=' + merger.getRestOfFirstBlock())
    print('Second rest=' + merger.getRestOfSecondBlock())


if __name__ == '__main__':
    fileName1 = os.getcwd()[:-6] + 'inputs' + os.sep + '1_1.c'
    fileName2 = os.getcwd()[:-6] + 'inputs' + os.sep + '1_2.c'
    # test(fileName1, fileName2)
    merge_test(fileName1, fileName2)