grammar pandaQ ;

root : (query | assig | plot) ';' ;

assig : ID ':=' query ;

plot : 'plot' taula ;

query : 'select' camps 'from' taula (join_info)* (where)? (orderBy)? ;

camps : '*' | col (',' col)* ;

col : (expr ' as ' ID)   # campCalculat
    | ID                 # camp
    ;

join_info : 'inner join' taula 'on' ID '=' ID ;               

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

where : 'where' cond ('and' cond)* ;

cond : ('not')? ID ('<' | '=') ID      # comp_text
     | ('not')? ID ('<' | '=') NUM     # comp_num
     | ID 'in' '(' subquery ')'        # compSQ
     ;

subquery : 'select' ID 'from' taula (whereSQ)?;

whereSQ : 'where' condSQ ('and' condSQ)* ;

condSQ : ID '=' NUM 
       ;

taula : ID ;

ID : [a-zA-Z_][a-zA-Z0-9_]* ;
NUM : [0-9]+ ;
DECIMAL : [0-9]+ '.' [0-9]+ ;

WS  : [ \t\n\r]+ -> skip ;
