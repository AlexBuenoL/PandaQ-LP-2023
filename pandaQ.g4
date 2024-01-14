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

orderBy : 'order by' camp_order (',' camp_order)* ;

camp_order : ID           # asc
           | ID 'asc'     # asc
           | ID 'desc'    # desc
           ;

where : 'where' cond ('and' cond)* ;

cond : ID ('<' | '=') NUM           # comp_num
     | 'not' ID ('<' | '=') NUM     # comp_num_neg
     | ID ('<' | '=') ID            # comp_text
     | 'not' ID ('<' | '=') ID      # comp_text_neg
     | ID 'in' '(' subquery ')'     # compSQ
     ;

subquery : 'select' ID 'from' taula (whereSQ)?;

whereSQ : 'where' condSQ ('and' condSQ)* ;

condSQ : ID ('<' | '=') NUM         # comp_numSQ
       | ID ('<' | '=') ID          # comp_textSQ
       | 'not' ID ('<' | '=') NUM   # comp_numSQ_neg
       | 'not' ID ('<' | '=') ID    # comp_textSQ_neg
       ;

taula : ID ;

ID : [a-zA-Z_][a-zA-Z0-9_]* ;
NUM : [0-9]+ ;
DECIMAL : [0-9]+ '.' [0-9]+ ;

WS  : [ \t\n\r]+ -> skip ;
