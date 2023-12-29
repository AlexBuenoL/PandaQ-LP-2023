grammar pandaQ ;

root : query ;

query : 'select' camps 'from' taula ';'                         # selectNormal
      | 'select' camps 'from' taula 'order by' order ';'        # selectOrder
      ;

camps : '*' | col (',' col)* ;

col : (expr ' as ' ID)   # campCalculat
    | ID                 # camp
    ;               

expr : expr ('*' | '/') expr
     | expr ('+' | '-') expr
     | '(' expr ')'
     | NUM
     | DECIMAL
     | ID
     ;

order : camp_order (',' camp_order)* ;

camp_order : ID           # asc
           | ID 'asc'     # asc
           | ID 'desc'    # desc
           ;

taula : ID ;

ID : [a-zA-Z_][a-zA-Z0-9_]* ;
NUM : [0-9]+ ;
DECIMAL : [0-9]+ '.' [0-9]+ ;

WS  : [ \t\n\r]+ -> skip ;
