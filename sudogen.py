#!/bin/env python3
import sys
import logging

logging.basicConfig(level=logging.DEBUG)
logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
rootLogger = logging.getLogger()

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
rootLogger.addHandler(consoleHandler)

def genHeader():
    header = """// SudoLang v1.0.8

```SudoLang
    """
    return header

def genEnding():
    header = """```
Let's roleplay. You are the game engine. I am the protagonist. 使用中文对话. Start!
    """
    return header


def genCode(entryPath, destPath):
    # Taking "gfg input file.txt" as input file
    # in reading mode
    with open(entryPath, "r") as input:
        
        # Creating "gfg output file.txt" as output
        # file in write mode
        with open(destPath, "w") as output:

            output.write(genHeader())
            
            # Writing each line from input file to
            # output file using loop
            for line in input:
                if line.startswith('<') : # and line.endswith('>') :
                    endIndex = line.rindex('>')
                    referencePath = line[1:endIndex]
                    logging.debug('reference %s is added', referencePath)
                    with open(referencePath, "r") as reference:
                        output.write(reference.read())
                        output.write('\n')
                    continue

                output.write(line)

            output.write(genEnding())



if __name__ == "__main__":
    entryPath = sys.argv[1]

    logging.info('generate sudo code for %s ...', entryPath)
    
    pattenName = entryPath.rsplit(".", 1)[0]
    logging.debug('parse the file name is  %s', pattenName)


    destPath = pattenName + ".sudo.gen"

    logging.debug('the new code will be genrated to %s', destPath)

    genCode(entryPath, destPath)