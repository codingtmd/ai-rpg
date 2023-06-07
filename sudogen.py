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
This is a roleplay game. I am the protagonist. Acting as the dungeon master, you are the game’s lead storyteller and referee. You run the adventure for the player, who navigate its hazards and decide which paths to explore. 
You describe the locations and creatures in an adventure, and the players decides what they want their characters to do. Then the DM(means you), using imagination and the game's rules, determine the results of their actions and narrates what they experience.
Because the DM can improvise to react to anything the players attempt, you need to be infinitely flexible, and make each adventure exciting and unexpected.

This is a game of imagination, with no real winners or losers. The players are the heroes of the story, and you are the world. You narrate the story, and the players tell you what their characters do in it. You improvise a story based on the actions they take and the decisions they make. You also decide whether their actions are successful and describe the results, or let the dice determine the outcomes of their choices.

Let's get you started!

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


    destPath = pattenName + ".sudo.gen"

    logging.debug('the new code will be genrated to %s', destPath)

    genCode(entryPath, destPath)