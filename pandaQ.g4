grammar pandaQ ;

root : query ;

query : 'select' camps 'from' taula ';'                         # selectNormal
      | 'select' camps 'from' taula 'order by' order ';'        # selectOrder
      | 'select' camps 'from' taula 'where' conds_where ';'     # selectWhere
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

conds_where : cond ('and' cond)* ;

cond : ID ('<' | '=') ID             # comp_text
     | ID ('<' | '=') NUM            # comp_num
     | ('not')? ID ('<' | '=') ID    # comp_text_not
     | ('not')? ID ('<' | '=') NUM   # comp_num_not
     ;

taula : ID ;

ID : [a-zA-Z_][a-zA-Z0-9_]* ;
NUM : [0-9]+ ;
DECIMAL : [0-9]+ '.' [0-9]+ ;

WS  : [ \t\n\r]+ -> skip ;
