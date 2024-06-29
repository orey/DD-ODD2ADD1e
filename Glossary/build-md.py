#--------------------------------------------------
# Builds the md file
# Copyleft: Olivier Rey
# Date: August 2023
#--------------------------------------------------
#!/bin/python3
import glob
import json
from datetime import datetime

#GLOBAL
NOM_GLOSSAIRE = "GLOSSAIRE_DONJONS_ET_DRAGONS.md"

# Global grammar
VERSION = "version"
LETTER = "letter"
GLOSSARY = "glossary"

# Record grammar
EN = "en" # array
FR = "fr" # array
TYPE = "type"
SOURCE = "source" #array

STYLE_EN = 1 # string.title() for every word capitalization
STYLE_FR = 2 # no capitalization but could be string.capitalize()

def format_elem(tab, style=STYLE_FR):
    siz = len(tab)
    count = 1
    result = ""
    for e in tab:
        if style == STYLE_EN:
            result = result + e.title()
        else:
            result = result + e
        if siz != count:
            result = result + ", "
        count +=1
    return result


def format_md(parsed,output):
    letter = parsed[LETTER]
    output.write("## " + letter.capitalize() + "\n\n")
    gloss = parsed[GLOSSARY]
    for e in gloss:
        en = e[EN]
        fr = e[FR]
        typ = e[TYPE]
        source = e[SOURCE]
        output.write("**" + format_elem(en, STYLE_EN) + "** : "
                     + format_elem(fr) + ". "
                     + typ.capitalize()
                     + ". Sources : "
                     + format_elem(source)
                     + ".\n\n")


if __name__ == "__main__":
    files = glob.glob('*.json')
    with open(NOM_GLOSSAIRE, "w") as output:
        output.write("# GLOSSAIRE DONJONS & DRAGONS\n\n")
        output.write("Généré le " + str(datetime.now()) + "\n\n")
        for f in sorted(files):
            print("Treating " + str(f))
            with open(f, "r") as user_file:
                file_contents = user_file.read()
                #print(file_contents)
                parsed = json.loads(file_contents)
                format_md(parsed,output)



