grammar pandaQ;

root : query ;

query : 'select * from' TABLE ';' 
      ;

TABLE : [a-zA-Z_][a-zA-Z0-9_]* 
      ;

WS  : [ \t\n\r]+ -> skip ;
