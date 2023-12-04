grammar pandaQ;

root : query ;

query : 'select' camps 'from' taula ';' 
      ;

camps : '*' | cols
      ;

cols : ID (',' ID)*
     ;

taula : ID 
      ;

ID : [a-zA-Z_][a-zA-Z0-9_]* 
   ;

WS  : [ \t\n\r]+ -> skip ;
