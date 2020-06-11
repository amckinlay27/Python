#
#Author: Adam McKinlay
#Student Number: c0656685
#Program: pwc.py
#Description: Produces the number of lines, words, and characters in a file
#

# ---------------------------------------------------------------------------- #
#                                    Imports                                   #
# ---------------------------------------------------------------------------- #
import argparse
import sys

# ---------------------------------------------------------------------------- #
#                                   Main                                       #
# ---------------------------------------------------------------------------- #
def main():
    #Argument Parser
    parser = argparse.ArgumentParser(description="Produces a file's line, word, and character count", epilog="Thanks for choosing pwc")
    parser.add_argument('-f', '--file', dest='files', action='append', help="the file(s) to process")
    args = parser.parse_args()
    
    if(len(sys.argv) < 2):
        print('You must provide an argument')
        exit()
    
    files = args.files
    parseDocument(files)
#main

# ---------------------------------------------------------------------------- #
#                                   Function                                   #
# ---------------------------------------------------------------------------- #
def parseDocument(files):
    #Initialize Variables
    line_count = 0
    word_count = 0
    char_count = 0

    #Process each file
    for file in files:
        try:
            #Read file
            txt_file = open(file, 'r', encoding='utf-8')
            print(f"Results for \'{file}\'")
            txt_file = open(file, 'r', encoding='utf-8')
            
            #Count Lines
            contents = txt_file.readline()
            while(contents != ''):
                line_count += 1
                #print(contents)

                #Count Characters
                for letter in contents:
                    if (letter != '\n'):
                        char_count += 1
                    #print(letter)

                #Count Words
                words = contents.split(' ')
                for word in words:
                    if(word != '\n' and word != ''):
                        word_count += 1
                        #print(word)

                contents = txt_file.readline()

            #Summary
            print(f"{line_count} {word_count} {char_count} \n")

            #Rest Variables
            line_count = 0
            word_count = 0
            char_count = 0

        except OSError:
            print(f'The file \'{file}\' does not exist in current directory or is not acceptable formatting')
#parseDocument

main()
# ---------------------------------------------------------------------------- #
#                                      EOF                                     #
# ---------------------------------------------------------------------------- #