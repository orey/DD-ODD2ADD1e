# Glossaire anglais-français D&D

## Introduction

Ce glossaire est une tentative de concentrer des traductions glanées ici et là. Il se peut qu'il serve un jour à quelque chose (notamment dans l'initiative de passer D&D en données structurées comme [Open5e](https://github.com/open5e), le jour où le multilingue sera possible.

Quand plusieurs traductions ont été employées, le but est de les proposer toutes avec leurs commentaires.

## JSON data

La structure des données est la suivante :

```
{
    "version" : 1,
    "letter" : "a",
    "glossary" :
    [
        {
            "en" : [ "animal telepathy" ],
            "fr" : [ "télépathie avec les animaux", "télépathie animale" ],
            "type" : "pouvoir psionique",
            "source" : [ "OD&D Eldritch Wizardry" ]
        }
    ]
}
```

Cela pour chaque lettre.

A noter que tout doit être en minuscule (anglais et français), cela pour permettre aux robots d'inclure facilement les textes et de faire la capitalisation qui leur convient. En effet, en français, si l'on capitalise trop vite, on risque de faire disparaître les accents.

Un programme python simple de conversion convertit tout cela en .md.

## Glossaire

[GLOSSAIRE DONJONS & DRAGONS](GLOSSAIRE_DONJONS_ET_DRAGONS.md)

