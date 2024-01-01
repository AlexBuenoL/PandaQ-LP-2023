grammar pandaQ ;

root : query ;

query : 'select' camps 'from' taula (where)? (orderBy)? ';' ;


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

orderBy : 'order by' order ;

order : camp_order (',' camp_order)* ;

camp_order : ID           # asc
           | ID 'asc'     # asc
           | ID 'desc'    # desc
           ;

where : 'where' conds_where ;

conds_where : cond ('and' cond)* ;

cond : ('not')? ID ('<' | '=') ID      # comp_text
     | ('not')? ID ('<' | '=') NUM     # comp_num
     ;

taula : ID ;

ID : [a-zA-Z_][a-zA-Z0-9_]* ;
NUM : [0-9]+ ;
DECIMAL : [0-9]+ '.' [0-9]+ ;

WS  : [ \t\n\r]+ -> skip ;
