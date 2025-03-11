# Disseny de blocs numèrics Montessori amb Inkscape: Una guia pas a pas

Aquesta guia us guiarà pel procés de creació dels fitxers de disseny per als blocs numèrics Montessori (també coneguts com a barres numèriques o maons numèrics) utilitzant Inkscape, un editor de gràfics vectorials gratuït i de codi obert. Aquests blocs són un material fonamental en l'educació Montessori per ensenyar conceptes matemàtics bàsics.

## Requisits previs

* **Inkscape:** Assegureu-vos de tenir Inkscape instal·lat al vostre ordinador. Podeu descarregar-lo gratuïtament des de [https://inkscape.org/](https://inkscape.org/).
* **Coneixements bàsics d'Inkscape:** Aquesta guia suposa que teniu una comprensió bàsica de la interfície i les eines d'Inkscape (per exemple, crear formes, utilitzar l'eina d'alineació).
* **Mesures:** Necessiteu conèixer les dimensions desitjades per als vostres blocs numèrics. Les dimensions comunes són:
  * **Amplada i profunditat:** Normalment quadrades, per exemple, 2 cm x 2 cm.
  * **Longitud:** Varia de 2 cm (per al bloc 1) a 20 cm (per al bloc 10) si s'utilitza una base de 2 cm, o de 2,5 cm (per al bloc 1) a 25 cm (per al bloc 10) si s'utilitza una base de 2,5 cm.
* **Gruix del material:** Decidiu el gruix del material que utilitzareu (per exemple, 3 mm, 6 mm, 15 mm). Utilitzeu fusta gruixuda si voleu apilar-los.

## Instruccions pas a pas

### Pas 1: Configuració del document

1. **Obre Inkscape:** Inicieu Inkscape al vostre ordinador.
2. **Document nou:** Creeu un document nou (Fitxer > Nou).
3. **Propietats del document:**
    * Aneu a Fitxer > Propietats del document (o premeu `Maj + Ctrl + D`).
    * **Unitats:** Definiu les "Unitats de visualització" a centímetres (cm).
    * **Mida de la pàgina:** Trieu una mida de pàgina que sigui prou gran per a tots els blocs, per exemple, A3.
    * **Escala** Assegureu-vos que l'escala sigui 1.
4. **Afegeix guies:** Afegeix guies verticals i horitzontals al llenç, per ajudar-vos a organitzar els blocs. Podeu afegir les guies fent clic a la regla esquerra i arrossegant-la al llenç. Feu el mateix amb la regla superior per afegir guies horitzontals.

### Pas 2: Creació del bloc base (Bloc 1)

1. **Eina Rectangle:** Seleccioneu l'eina Rectangle (tecla `R`).
2. **Dibuixa el rectangle:** Dibuixa un rectangle al llenç. No us preocupeu encara per la mida exacta.
3. **Estableix les dimensions:**
    * Seleccioneu el rectangle.
    * A la barra de control de l'eina a la part superior, configureu el següent:
        * **Amplada (W):** 2 cm (o 2,5 cm)
        * **Alçada (H):** 2 cm (o 2,5 cm)
    * També hauríeu d'omplir el bloc amb un color.

### Pas 3: Creació dels blocs 2-10 i afegir números

Aquest pas combina la creació dels blocs restants i l'addició dels números a cada bloc.

1. **Crea el número:**
    * **Eina Text:** Seleccioneu l'eina Text (tecla `T`).
    * **Afegeix text:** Feu clic al llenç i escriviu `2`. Aquest serà el número per al bloc 2.
    * **Font i estil:** Trieu la font i l'estil del número.
    * **Converteix a camí:** Seleccioneu el número i aneu a Camí > Objecte a camí (`Ctrl + Maj + C`).
2. **Crea el bloc 2:**
    * **Seleccioneu el número:** Seleccioneu el número 2, ara convertit a camí.
    * **Duplica el bloc 1:** Seleccioneu el bloc base (Bloc 1) i dupliqueu-lo amb `Ctrl + D`.
    * **Ajusta l'amplada:** Seleccioneu el bloc duplicat. Ara seleccioneu el número 2 i el bloc duplicat. Feu clic a "alinea i distribueix" (`Ctrl + Maj + A`). Seleccioneu "Alinea les vores esquerres" i "Alinea les vores superiors". Ara, canvieu la mida del bloc duplicat fins que tingui la mateixa longitud que el número 2 i el final del número estigui al final del bloc.
    * Podeu canviar el color del bloc.
    * **Col·loca el número:** Seleccioneu el número i el bloc. Aneu a Objecte > Alinea i distribueix (o `Ctrl + Maj + A`). Al panell "Alinea i distribueix", seleccioneu tant "Centre a l'eix vertical" com "Centre a l'eix horitzontal".
3. **Repetiu per als blocs 3-10:**
    * Repetiu els passos 1 i 2 per als blocs del 3 al 10.
    * Cada vegada, creeu el número i utilitzeu-lo com a referència per a la mida del bloc.
    * Creeu cada bloc en ordre.
    * Heu de canviar el color per a cada bloc.
4. **Organitza:** Organitzeu els blocs al llenç. Podeu utilitzar les guies per fer-ho.

### Pas 4: Línies de tall

1. **Seleccioneu tots els blocs:** Seleccioneu tots els blocs.
2. **Estil de traç:** Al panell Ompliment i traç (`Ctrl+Maj+F`), aneu a "Estil de traç". Seleccioneu l'amplada correcta. Això pot canviar segons el gruix del material (si el vostre material té 3 mm de gruix, la línia ha de ser de 0,3 mm).
3. **Canvia el color:** Ara, canvieu el color del traç al color que la vostra màquina utilitza per tallar.

### Pas 5: Organització i disposició

1. **Disposa al llenç:** Disposa els blocs al llenç d'Inkscape d'una manera que maximitzi l'espai i l'eficiència per al tall per làser o el fresat CNC.
2. **Espaiat:** Deixeu una petita quantitat d'espai entre els blocs per permetre l'eliminació del material i evitar les vores cremades, depenent de la màquina que utilitzeu.

### Pas 6: Desa el fitxer

1. **Desa com a SVG:** Aneu a Fitxer > Desa com a.
2. **Tipus de fitxer:** Trieu "SVG senzill" com a tipus de fitxer.
3. **Nom del fitxer:** Doneu al vostre fitxer un nom descriptiu (per exemple, `blocs-numerics-maons.svg`).
4. **Desa:** Feu clic a "Desa".
5. **Desa com a DXF:** Aneu a Fitxer > Desa una còpia.
6. **Tipus de fitxer:** Trieu "Plotter de tall d'escriptori (AutoCAD DXF R14) (*.dxf)".
7. **Nom del fitxer:** Doneu al vostre fitxer un nom descriptiu (per exemple, `blocs-numerics-maons.dxf`).
8. **Desa:** Feu clic a "Desa".

## Consells i consideracions

* **Kerf:** Si esteu tallant amb làser, tingueu en compte el kerf (l'amplada del material eliminat pel làser). Pot ser que hàgiu d'ajustar lleugerament les dimensions per tenir-ho en compte.
* **Gruix del material:** Heu d'adaptar el disseny en funció del gruix del material que utilitzeu.
* **Prova:** Proveu sempre un petit tall de mostra amb el vostre material i la configuració de la màquina específics abans de tallar tot el conjunt de blocs.
* **Gravat:** Si voleu gravar els números, haureu de crear una capa o un color separats per als números que indiquin a la màquina que gravi en lloc de tallar.
* **Optimització:** Podeu aprofitar al màxim l'espai de la màquina, duplicant tots els dissenys.

## Conclusió

Seguint aquests passos, podeu dissenyar els vostres propis blocs numèrics Montessori utilitzant Inkscape. Aquests blocs són una eina fantàstica per ensenyar als nens sobre números i matemàtiques. Recordeu que heu de prendre-us el vostre temps, provar els vostres dissenys i divertir-vos!