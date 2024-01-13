PandaQ - LP 2023
Alex Bueno


Petit intèrpret de consultes SQL implementat en Python.
Per utilitzar-ho, primer s'han de generar els fichers corresponents amb les comandes 1 i 2, i després es pot executar l'intèrpret amb la comanda 3 o 4.


Si vols introduir les dades desde la pàgina de streamlit, executa la comanda 3 i prem el botó "Executa" després de introduir la teva consulta SQL.
Si vols introduir les dades desde terminal, executa la comanda 4 i escriu la teva consulta a la terminal

** Les consultes han d'acabar amb ';' i el nom de les taules ha de ser el nom de la taula sense el ".csv" **


Per generar els archius necessaris per executar:

    1: antlr4 -Dlanguage=Python3 -no-listener pandaQ.g4

    2: antlr4 -Dlanguage=Python3 -no-listener -visitor pandaQ.g4


Per executar l'intèrpret:

    3: streamlit run pandaQ.py (llegir querys desde streamlit)

    4: streamlit run pandaQ2.py (llegir querys desde terminal)



* where : la sintaxi de la condició del where ha de ser primer el 'not' si es vol negar la condició, després el nom de la columna per la que es vol filtrar, després l'operador ('<' o '=') i per últim el valor a comparar. Per combinar varies condicions: 'and'

q := select first_name, last_name, job_title, department_name from employees inner join departments on department_id = department_id inner join jobs on job_id = job_id;