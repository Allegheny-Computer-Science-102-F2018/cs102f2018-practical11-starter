#!/usr/bin/env python3

__author__      = "Oliver Bonham-Carter"
__date__        = "6 November 2018"

# program to find word freqs in a text.

def openAndCleanData(inFile):
    """ loads a text file and returns a string of contents"""
    data_str = open(inFile,"r").read().lower() #return a string in lowercase
    #print("type :",type(data_str))
    punct_str = "!.,'\""
    for i in punct_str:
        data_str = data_str.replace(i,"") #remove the punctuation
    return data_str
#end of openFile()


def help():
    """ online help function"""
    print("  ",__author__,"::",__date__)
    print("   Program to load a text file of text and to return a frequency plot of the word freqs")
    print("   Usage: program <wordFile.txt>")
#end of help()


def collectFreqs(data_str):
    """collect the numbers of words and return a dictionary of freqs"""
    print("  collectFreqs()")
    data_list = sorted(data_str.split()) # return an abc-sorted list
    freq_list = [] # we will store the freqs in a list
    count_dic = {} # store words and counts
    for i in data_list:  
        if i not in count_dic: count_dic[i] = 1
        else: count_dic[i] = count_dic[i] + 1
    #print("  Count_dic :",count_dic)

    # place freqs in the list
    for i in count_dic:
        freq_list.append(count_dic[i]/len(data_list))
    #print("  freq_list :",freq_list)

    return freq_list
#end of collectFreqs()


def plotter(in_list, inFile_str):
    """ plots the freq data"""
    y = in_list
    x = [i for i in range(len(in_list))]
    plot(x,y, linestyle="", marker = 'v')
    title("Frequency of words used")
    xlabel("Words")
    ylabel("Magnitude of Frequency")

    fname_str = inFile_str.replace(".txt",".png")
    fname_str = "out_" + fname_str

    print(" Saving new filename:", fname_str)
    savefig(fname_str) #save in root directory
    show()

#end of plotter()


def begin(inFile):
    """ Driver function """
    print(" Loading file :", inFile)
    data = openAndCleanData(inFile)
    #print("  Contents :",data)
    collectedFreqs_list = collectFreqs(data)
    #print(" collectedFreqs_list :",collectedFreqs_list)
    plotter(collectedFreqs_list,inFile)
    print("  Program finished")
#end of begin()


# command line paramters code
###################################
import itertools, sys
from pylab import plot, show, title, savefig, xlabel, ylabel, legend
if __name__ == '__main__':

    if len(sys.argv) == 2: #one option added to command line
       begin(sys.argv[1])
    else:
       help()
       sys.exit(0)


