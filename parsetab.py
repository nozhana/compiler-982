
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASSIGN CHOP COLON COMMA DIVIDE ELSE EQUAL ID IF INPUT LARGER LBRACE LBRACKET LEN LESS LPAR MINUS NUMBER NUMBER_FLOAT PLUS POW PRINT RBRACE RBRACKET RPAR SEMICOLON STR TEXT TEXT_COMMENT TIMES UNEQUAL WHILEstart : statementsstatements : comment statements\n         | comment\n         | statement\n         | statement comment\n    comment : TEXT_COMMENTstatement : LBRACE state RBRACE\n    state : assign_statement state\n        | if_statement state\n        | while_statement state\n        | assign_statement\n        | if_statement\n        | while_statement\n    state : comment state\n            | comment\n        assign_statement : ID ASSIGN E SEMICOLON\n        | ID ASSIGN INPUT LPAR RPAR SEMICOLON\n        | ID ASSIGN INPUT LPAR TEXT RPAR SEMICOLON\n    assign_statement : PRINT LPAR TEXT RPAR SEMICOLON\n    assign_statement : PRINT LPAR ID RPAR SEMICOLON\n    assign_statement : PRINT LPAR NUMBER RPAR SEMICOLON\n        | PRINT LPAR NUMBER_FLOAT RPAR SEMICOLON\n    assign_statement : PRINT LPAR TEXT COMMA ID RPAR SEMICOLON\n    assign_statement : PRINT LPAR E RPAR SEMICOLON\n    if_statement : IF LPAR E LESS E RPAR statement\n            | IF LPAR E LESS E RPAR statement ELSE statement\n            | IF LPAR E LARGER E RPAR statement\n            | IF LPAR E LARGER E RPAR statement ELSE statement\n            | IF LPAR E UNEQUAL E RPAR statement\n            | IF LPAR E UNEQUAL E RPAR statement ELSE statement\n            | IF LPAR E EQUAL E RPAR statement\n            | IF LPAR E EQUAL E RPAR statement ELSE statementwhile_statement : WHILE LPAR E LESS E RPAR statement\n            | WHILE LPAR E LESS E RPAR statement ELSE statement\n            | WHILE LPAR E LARGER E RPAR statement\n            | WHILE LPAR E LARGER E RPAR statement ELSE statement\n            | WHILE LPAR E UNEQUAL E RPAR statement\n            | WHILE LPAR E UNEQUAL E RPAR statement ELSE statement\n            | WHILE LPAR E EQUAL E RPAR statement\n            | WHILE LPAR E EQUAL E RPAR statement ELSE statement\n    E : expressionE : LEN LPAR ID RPARE : STR LPAR ID RPARE : CHOP LPAR ID RPARE : ID LBRACKET NUMBER RBRACKET\n        | ID LBRACKET NUMBER COLON NUMBER RBRACKET\n        | ID LBRACKET COLON NUMBER RBRACKET\n        | ID LBRACKET NUMBER COLON RBRACKET\n        expression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression TIMES expression\n                  | expression DIVIDE expression\n                  | expression POW expressionexpression : LPAR expression RPARexpression : NUMBERexpression : NUMBER_FLOATexpression : IDexpression : TEXT'
    
_lr_action_items = {'TEXT_COMMENT':([0,3,4,5,6,10,11,12,13,18,46,85,87,88,89,90,102,119,120,121,122,123,124,125,126,127,128,138,139,140,141,142,143,144,145,],[5,5,5,-6,5,5,5,5,5,-7,-16,-19,-20,-21,-22,-24,-17,-18,-23,-25,-27,-29,-31,-33,-35,-37,-39,-26,-28,-30,-32,-34,-36,-38,-40,]),'LBRACE':([0,3,5,108,109,110,111,112,113,114,115,130,131,132,133,134,135,136,137,],[6,6,-6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'$end':([1,2,3,4,5,7,8,18,],[0,-1,-3,-4,-6,-2,-5,-7,]),'ID':([5,6,10,11,12,13,18,23,24,25,26,30,46,50,51,52,53,54,55,56,57,59,64,65,66,67,68,69,70,71,85,87,88,89,90,102,119,120,121,122,123,124,125,126,127,128,138,139,140,141,142,143,144,145,],[-6,14,14,14,14,14,-7,27,39,27,27,49,-16,49,49,49,49,49,82,83,84,86,27,27,27,27,27,27,27,27,-19,-20,-21,-22,-24,-17,-18,-23,-25,-27,-29,-31,-33,-35,-37,-39,-26,-28,-30,-32,-34,-36,-38,-40,]),'PRINT':([5,6,10,11,12,13,18,46,85,87,88,89,90,102,119,120,121,122,123,124,125,126,127,128,138,139,140,141,142,143,144,145,],[-6,15,15,15,15,15,-7,-16,-19,-20,-21,-22,-24,-17,-18,-23,-25,-27,-29,-31,-33,-35,-37,-39,-26,-28,-30,-32,-34,-36,-38,-40,]),'IF':([5,6,10,11,12,13,18,46,85,87,88,89,90,102,119,120,121,122,123,124,125,126,127,128,138,139,140,141,142,143,144,145,],[-6,16,16,16,16,16,-7,-16,-19,-20,-21,-22,-24,-17,-18,-23,-25,-27,-29,-31,-33,-35,-37,-39,-26,-28,-30,-32,-34,-36,-38,-40,]),'WHILE':([5,6,10,11,12,13,18,46,85,87,88,89,90,102,119,120,121,122,123,124,125,126,127,128,138,139,140,141,142,143,144,145,],[-6,17,17,17,17,17,-7,-16,-19,-20,-21,-22,-24,-17,-18,-23,-25,-27,-29,-31,-33,-35,-37,-39,-26,-28,-30,-32,-34,-36,-38,-40,]),'RBRACE':([5,9,10,11,12,13,18,19,20,21,22,46,85,87,88,89,90,102,119,120,121,122,123,124,125,126,127,128,138,139,140,141,142,143,144,145,],[-6,18,-11,-12,-13,-15,-7,-8,-9,-10,-14,-16,-19,-20,-21,-22,-24,-17,-18,-23,-25,-27,-29,-31,-33,-35,-37,-39,-26,-28,-30,-32,-34,-36,-38,-40,]),'ASSIGN':([14,],[23,]),'LPAR':([15,16,17,23,24,25,26,29,30,33,34,35,50,51,52,53,54,64,65,66,67,68,69,70,71,],[24,25,26,30,30,30,30,47,30,55,56,57,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'ELSE':([18,121,122,123,124,125,126,127,128,],[-7,130,131,132,133,134,135,136,137,]),'INPUT':([23,],[29,]),'LEN':([23,24,25,26,64,65,66,67,68,69,70,71,],[33,33,33,33,33,33,33,33,33,33,33,33,]),'STR':([23,24,25,26,64,65,66,67,68,69,70,71,],[34,34,34,34,34,34,34,34,34,34,34,34,]),'CHOP':([23,24,25,26,64,65,66,67,68,69,70,71,],[35,35,35,35,35,35,35,35,35,35,35,35,]),'NUMBER':([23,24,25,26,30,45,50,51,52,53,54,64,65,66,67,68,69,70,71,73,100,],[36,40,36,36,36,72,36,36,36,36,36,36,36,36,36,36,36,36,36,101,116,]),'NUMBER_FLOAT':([23,24,25,26,30,50,51,52,53,54,64,65,66,67,68,69,70,71,],[37,41,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'TEXT':([23,24,25,26,30,47,50,51,52,53,54,64,65,66,67,68,69,70,71,],[31,38,31,31,31,75,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'LBRACKET':([27,39,],[45,45,]),'PLUS':([27,31,32,36,37,38,39,40,41,48,49,76,77,78,79,80,81,],[-57,-58,50,-55,-56,-58,-57,-55,-56,50,-57,-54,50,50,50,50,50,]),'MINUS':([27,31,32,36,37,38,39,40,41,48,49,76,77,78,79,80,81,],[-57,-58,51,-55,-56,-58,-57,-55,-56,51,-57,-54,51,51,51,51,51,]),'TIMES':([27,31,32,36,37,38,39,40,41,48,49,76,77,78,79,80,81,],[-57,-58,52,-55,-56,-58,-57,-55,-56,52,-57,-54,52,52,52,52,52,]),'DIVIDE':([27,31,32,36,37,38,39,40,41,48,49,76,77,78,79,80,81,],[-57,-58,53,-55,-56,-58,-57,-55,-56,53,-57,-54,53,53,53,53,53,]),'POW':([27,31,32,36,37,38,39,40,41,48,49,76,77,78,79,80,81,],[-57,-58,54,-55,-56,-58,-57,-55,-56,54,-57,-54,54,54,54,54,54,]),'SEMICOLON':([27,28,31,32,36,37,49,58,60,61,62,63,74,76,77,78,79,80,81,99,103,104,105,106,107,117,118,129,],[-57,46,-58,-41,-55,-56,-57,85,87,88,89,90,102,-54,-49,-50,-51,-52,-53,-45,119,-42,-43,-44,120,-48,-47,-46,]),'LESS':([27,31,32,36,37,43,44,49,76,77,78,79,80,81,99,104,105,106,117,118,129,],[-57,-58,-41,-55,-56,64,68,-57,-54,-49,-50,-51,-52,-53,-45,-42,-43,-44,-48,-47,-46,]),'LARGER':([27,31,32,36,37,43,44,49,76,77,78,79,80,81,99,104,105,106,117,118,129,],[-57,-58,-41,-55,-56,65,69,-57,-54,-49,-50,-51,-52,-53,-45,-42,-43,-44,-48,-47,-46,]),'UNEQUAL':([27,31,32,36,37,43,44,49,76,77,78,79,80,81,99,104,105,106,117,118,129,],[-57,-58,-41,-55,-56,66,70,-57,-54,-49,-50,-51,-52,-53,-45,-42,-43,-44,-48,-47,-46,]),'EQUAL':([27,31,32,36,37,43,44,49,76,77,78,79,80,81,99,104,105,106,117,118,129,],[-57,-58,-41,-55,-56,67,71,-57,-54,-49,-50,-51,-52,-53,-45,-42,-43,-44,-48,-47,-46,]),'RPAR':([27,31,32,36,37,38,39,40,41,42,47,48,49,75,76,77,78,79,80,81,82,83,84,86,91,92,93,94,95,96,97,98,99,104,105,106,117,118,129,],[-57,-58,-41,-55,-56,58,60,61,62,63,74,76,-57,103,-54,-49,-50,-51,-52,-53,104,105,106,107,108,109,110,111,112,113,114,115,-45,-42,-43,-44,-48,-47,-46,]),'COMMA':([38,],[59,]),'COLON':([45,72,],[73,100,]),'RBRACKET':([72,100,101,116,],[99,117,118,129,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'statements':([0,3,],[2,7,]),'comment':([0,3,4,6,10,11,12,13,],[3,3,8,13,13,13,13,13,]),'statement':([0,3,108,109,110,111,112,113,114,115,130,131,132,133,134,135,136,137,],[4,4,121,122,123,124,125,126,127,128,138,139,140,141,142,143,144,145,]),'state':([6,10,11,12,13,],[9,19,20,21,22,]),'assign_statement':([6,10,11,12,13,],[10,10,10,10,10,]),'if_statement':([6,10,11,12,13,],[11,11,11,11,11,]),'while_statement':([6,10,11,12,13,],[12,12,12,12,12,]),'E':([23,24,25,26,64,65,66,67,68,69,70,71,],[28,42,43,44,91,92,93,94,95,96,97,98,]),'expression':([23,24,25,26,30,50,51,52,53,54,64,65,66,67,68,69,70,71,],[32,32,32,32,48,77,78,79,80,81,32,32,32,32,32,32,32,32,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> statements','start',1,'p_Start','main2.py',102),
  ('statements -> comment statements','statements',2,'p_statements','main2.py',105),
  ('statements -> comment','statements',1,'p_statements','main2.py',106),
  ('statements -> statement','statements',1,'p_statements','main2.py',107),
  ('statements -> statement comment','statements',2,'p_statements','main2.py',108),
  ('comment -> TEXT_COMMENT','comment',1,'p_comment','main2.py',113),
  ('statement -> LBRACE state RBRACE','statement',3,'p_statement','main2.py',116),
  ('state -> assign_statement state','state',2,'p_state','main2.py',120),
  ('state -> if_statement state','state',2,'p_state','main2.py',121),
  ('state -> while_statement state','state',2,'p_state','main2.py',122),
  ('state -> assign_statement','state',1,'p_state','main2.py',123),
  ('state -> if_statement','state',1,'p_state','main2.py',124),
  ('state -> while_statement','state',1,'p_state','main2.py',125),
  ('state -> comment state','state',2,'p_state_1','main2.py',130),
  ('state -> comment','state',1,'p_state_1','main2.py',131),
  ('assign_statement -> ID ASSIGN E SEMICOLON','assign_statement',4,'p_assign_statement','main2.py',134),
  ('assign_statement -> ID ASSIGN INPUT LPAR RPAR SEMICOLON','assign_statement',6,'p_assign_statement','main2.py',135),
  ('assign_statement -> ID ASSIGN INPUT LPAR TEXT RPAR SEMICOLON','assign_statement',7,'p_assign_statement','main2.py',136),
  ('assign_statement -> PRINT LPAR TEXT RPAR SEMICOLON','assign_statement',5,'p_assign_statement_1','main2.py',146),
  ('assign_statement -> PRINT LPAR ID RPAR SEMICOLON','assign_statement',5,'p_assign_statement_2','main2.py',154),
  ('assign_statement -> PRINT LPAR NUMBER RPAR SEMICOLON','assign_statement',5,'p_assign_statement_3','main2.py',160),
  ('assign_statement -> PRINT LPAR NUMBER_FLOAT RPAR SEMICOLON','assign_statement',5,'p_assign_statement_3','main2.py',161),
  ('assign_statement -> PRINT LPAR TEXT COMMA ID RPAR SEMICOLON','assign_statement',7,'p_assign_statement_4','main2.py',168),
  ('assign_statement -> PRINT LPAR E RPAR SEMICOLON','assign_statement',5,'p_assign_statement_5','main2.py',174),
  ('if_statement -> IF LPAR E LESS E RPAR statement','if_statement',7,'p_if_statement','main2.py',179),
  ('if_statement -> IF LPAR E LESS E RPAR statement ELSE statement','if_statement',9,'p_if_statement','main2.py',180),
  ('if_statement -> IF LPAR E LARGER E RPAR statement','if_statement',7,'p_if_statement','main2.py',181),
  ('if_statement -> IF LPAR E LARGER E RPAR statement ELSE statement','if_statement',9,'p_if_statement','main2.py',182),
  ('if_statement -> IF LPAR E UNEQUAL E RPAR statement','if_statement',7,'p_if_statement','main2.py',183),
  ('if_statement -> IF LPAR E UNEQUAL E RPAR statement ELSE statement','if_statement',9,'p_if_statement','main2.py',184),
  ('if_statement -> IF LPAR E EQUAL E RPAR statement','if_statement',7,'p_if_statement','main2.py',185),
  ('if_statement -> IF LPAR E EQUAL E RPAR statement ELSE statement','if_statement',9,'p_if_statement','main2.py',186),
  ('while_statement -> WHILE LPAR E LESS E RPAR statement','while_statement',7,'p_while_statement','main2.py',229),
  ('while_statement -> WHILE LPAR E LESS E RPAR statement ELSE statement','while_statement',9,'p_while_statement','main2.py',230),
  ('while_statement -> WHILE LPAR E LARGER E RPAR statement','while_statement',7,'p_while_statement','main2.py',231),
  ('while_statement -> WHILE LPAR E LARGER E RPAR statement ELSE statement','while_statement',9,'p_while_statement','main2.py',232),
  ('while_statement -> WHILE LPAR E UNEQUAL E RPAR statement','while_statement',7,'p_while_statement','main2.py',233),
  ('while_statement -> WHILE LPAR E UNEQUAL E RPAR statement ELSE statement','while_statement',9,'p_while_statement','main2.py',234),
  ('while_statement -> WHILE LPAR E EQUAL E RPAR statement','while_statement',7,'p_while_statement','main2.py',235),
  ('while_statement -> WHILE LPAR E EQUAL E RPAR statement ELSE statement','while_statement',9,'p_while_statement','main2.py',236),
  ('E -> expression','E',1,'p_E','main2.py',241),
  ('E -> LEN LPAR ID RPAR','E',4,'p_E_1','main2.py',246),
  ('E -> STR LPAR ID RPAR','E',4,'p_E_2','main2.py',251),
  ('E -> CHOP LPAR ID RPAR','E',4,'p_E_3','main2.py',256),
  ('E -> ID LBRACKET NUMBER RBRACKET','E',4,'p_E_4','main2.py',261),
  ('E -> ID LBRACKET NUMBER COLON NUMBER RBRACKET','E',6,'p_E_4','main2.py',262),
  ('E -> ID LBRACKET COLON NUMBER RBRACKET','E',5,'p_E_4','main2.py',263),
  ('E -> ID LBRACKET NUMBER COLON RBRACKET','E',5,'p_E_4','main2.py',264),
  ('expression -> expression PLUS expression','expression',3,'p_expression','main2.py',279),
  ('expression -> expression MINUS expression','expression',3,'p_expression','main2.py',280),
  ('expression -> expression TIMES expression','expression',3,'p_expression','main2.py',281),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression','main2.py',282),
  ('expression -> expression POW expression','expression',3,'p_expression','main2.py',283),
  ('expression -> LPAR expression RPAR','expression',3,'p_expression_group','main2.py',297),
  ('expression -> NUMBER','expression',1,'p_expression_number','main2.py',303),
  ('expression -> NUMBER_FLOAT','expression',1,'p_expression_number_float','main2.py',308),
  ('expression -> ID','expression',1,'p_expression_name','main2.py',314),
  ('expression -> TEXT','expression',1,'p_expression_name_str','main2.py',319),
]