INTÈRPRET SQL: PandaQ
LP 2023/2024 - Q1
Alex Bueno


Petit intèrpret de consultes SQL implementat en Python amb totes les funcionalitats incloses en l'enunciat de la pràctica. 
A més, compta amb control de errors per si l'usuari s'equivoca introduint el nom de les taules, columnes, etc.
En aquest document es pot trobar informació sobre el funcionament de l'intèrpret i una breu explicació de la seva implementació.



1) Instruccions bàsiques d'ús:

    1: Abans de poder executar, s'han de generar els arxius necessaris a partir de la gramàtica

        antlr4 -Dlanguage=Python3 -no-listener pandaQ.g4

        antlr4 -Dlanguage=Python3 -no-listener -visitor pandaQ.g4
    
    2: Un cop s'han generat els arxius necessaris es pot executar l'intèrpret amb la següent comanda:

        streamlit run pandaQ.py
    
    3: Un cop s'hagi executat, s'obrira una aplicació 'streamlit' al navegador on es podran introduir les diferents consultes SQL.

    
    * Cal tenir en compte també que totes les consultes han d'acabar en ';'.



2) Breu explicació de la implementació:

    El codi està bastant comentat i entenc que és prou clarificador, tot i així donaré una breu descripció de la seva implementació. 

    He definit a la classe TreeVisitor tres taules com atributs de la classe per poder tenir més llibertat a l'hora de manipular-les en els visitors. La taula 'data' és una de les taules originals (ja sigui de les .csv o de les guardades per l'usuari), i aquesta taula és la que es filtra amb el 'where' i les subconsultes, la que s'ordena amb el 'order by' o la que es fusiona amb altres taules amb els 'inner joins'. 
    Un cop s'han visitat els visitors d'aquestes parts, es crea una taula buida 'new_data' on es van afegint les columnes de la taula 'data' o els nous camps calculats, segons la consulta de l'usuari. Aquestes columnes de 'data' que s'afegeixen ja estan correctament filtrades i ordenades ja que s'han visitat els visitors corresponents prèviament.
    També he definit la taula 'taulaSQ' que serveix per la implementació de les subconsultes.

    Si l'usuari decideix guardar-se la consulta a una taula de símbols, simplement es visita la query com ja he explicat, i s'afegeix a un diccionari de taules de símbols per poder ser consultat posteriorment amb la funció 'state' de streamlit.

    I si decideix fer un plot d'alguna de les taules guardades, simplement s'obté la taula del diccionari 'taules_simbols' i es fa el plot amb la funció 'line_chart' de streamlit.