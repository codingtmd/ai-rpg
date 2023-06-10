#!/bin/env python3
import os
import sys
import logging
from datetime import datetime
import time  

logging.basicConfig(level=logging.DEBUG)
logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
rootLogger = logging.getLogger()

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
rootLogger.addHandler(consoleHandler)

def genHeader():

    timestamp = time.time()
    date_time = datetime.fromtimestamp(timestamp)
    str_date_time = date_time.strftime("%d-%m-%Y, %H:%M:%S")
    
    header = """// SudoLang v0.4.0-{timestamp}
    """.format( timestamp = str_date_time)

    return header

def genEnding():
    header = """

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
                        for line2 in reference:
                            if not line2.startswith('#') : 
                                output.write(line2)
                    
                    output.write('\n')           
                    continue
                elif line.startswith('#') :
                    continue
                else:
                    output.write(line)

            output.write(genEnding())



if __name__ == "__main__":
    entryPath = sys.argv[1]

    logging.info('generate sudo code for %s ...', entryPath)
    
    pattenName = entryPath.rsplit(".", 1)[0]
    logging.debug('parse the file name is  %s', pattenName)

    file_name = os.path.basename(entryPath) 

    destPath = "./Exports/" + file_name + ".gen"

    logging.debug('the new code will be genrated to %s', destPath)

    genCode(entryPath, destPath)