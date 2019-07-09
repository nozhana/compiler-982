reserved = ('INPUT', 'PRINT', 'ELSE', 'WHILE', 'IF' ,'STR', 'LEN' , 'CHOP'
)

tokens = reserved + (
    'ID',
    'ASSIGN', 'NUMBER', 'NUMBER_FLOAT', 'TEXT',
    'LPAR', 'RPAR', 'RBRACKET','LBRACKET', 'LBRACE', 'RBRACE',
    'EQUAL', 'UNEQUAL', 'LARGER', 'LESS',
    'PLUS','MINUS','TIMES','DIVIDE','POW',
    'SEMICOLON', 'COLON', 'COMMA',
    'TEXT_COMMENT'
    # , 'NLINE'
)

precedence = (

    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'POW'),
)


# fix
t_ASSIGN        = r':='
t_EQUAL         = r'='
t_UNEQUAL       = r'<>'
t_LARGER        = r'>'
t_LESS          = r'<'
t_PLUS          = r'\+'
t_MINUS         = r'-'
t_TIMES         = r'\*'
t_DIVIDE        = r'/'
t_POW  = r'\^'
t_LPAR          = r'\('
t_RPAR          = r'\)'
t_LBRACKET = '\['
t_RBRACKET = '\]'
t_LBRACE = '\{'
t_RBRACE = '\}'
t_COMMA = r','
t_SEMICOLON = r';'
t_COLON = r':'
t_ignore        = " \t\n"



def t_NUMBER_FLOAT(t):
    r'\d+(\.\d+)'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t


def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t


def t_TEXT_COMMENT(t):
    '''\/\*([^(\/\*)(\*\/)])+\*\/'''
    return t

def t_TEXT(t):
    r'\".*\"'
    t.value = t.value[1:-1]
    return t



# def t_NLINE(t):
#     r'\n'
#     t.lexer.lineno += 1
#     return t


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

reserved_map = {}
for r in reserved:
    reserved_map[r.lower()] = r


def t_ID(t):
    r'[_a-zA-Z][_a-zA-Z\d]*'
    t.type = reserved_map.get(t.value,"ID")
    return t

# Build the lexer
import ply.lex as lex
lexer = lex.lex()

id_table = {}

stack = []
stack.append(True)


def p_Start(t):
    'start : statements'

def p_statements(t):
    '''statements : comment statements
         | comment
         | statement
         | statement comment
    '''


def p_comment(t):
    '''comment : TEXT_COMMENT'''

def p_statement(t):
    '''statement : LBRACE state RBRACE
    '''

def p_state(t):
    '''state : assign_statement state
        | if_statement state
        | while_statement state
        | assign_statement
        | if_statement
        | while_statement
    '''


def p_state_1(t):
    '''state : comment state
            | comment
        '''
def p_assign_statement(t):
    '''assign_statement : ID ASSIGN E SEMICOLON
        | ID ASSIGN INPUT LPAR RPAR SEMICOLON
        | ID ASSIGN INPUT LPAR TEXT RPAR SEMICOLON
    '''
    if len(t) == 5:
        id_table[t[1]] = t[3]
    elif len(t) == 7:
        id_table[t[1]] = input()
    elif len(t) == 8:
        id_table[t[1]] = input(t[5])

def p_assign_statement_1(t):
    '''assign_statement : PRINT LPAR TEXT RPAR SEMICOLON
    '''
    print(t[3])




def p_assign_statement_2(t):
    '''assign_statement : PRINT LPAR ID RPAR SEMICOLON
    '''
    print(id_table[t[3]])


def p_assign_statement_3(t):
    '''assign_statement : PRINT LPAR NUMBER RPAR SEMICOLON
        | PRINT LPAR NUMBER_FLOAT RPAR SEMICOLON
    '''
    print(t[3])



def p_assign_statement_4(t):
    '''assign_statement : PRINT LPAR TEXT COMMA ID RPAR SEMICOLON
    '''
    print(t[3], id_table[t[5]])


def p_assign_statement_5(t):
    '''assign_statement : PRINT LPAR E RPAR SEMICOLON
    '''
    print(t[3])

def p_condition(t):
    '''condition    : E LESS E
                    | E LARGER E
                    | E UNEQUAL E
                    | E EQUAL E
    '''

    if t[2] == '<':
        t[0] = True if t[1] < t[3] else False
    elif t[2] == '>':
        t[0] = True if t[1] > t[3] else False
    elif t[2] == '=':
        t[0] = True if t[1] == t[3] else False
    elif t[2] == '<>':
        t[0] = True if t[1] != t[3] else False
    else:
        print ('UNSUPPORTED LOGICAL OPERATOR')
        t[0] = False

def p_else_statement(t):
    '''else_statement   : ELSE statement
                        | ELSE if_statement
                        | empty
    '''

    t[0] = t[-1]

def p_if_statement(t):
        '''if_statement : IF LPAR condition RPAR statement else_statement
        '''

        if t[3]:
            t[0] = t[5]
        else:
            t[0] = t[6]



def p_while_statement(t):
        '''while_statement : WHILE LPAR condition RPAR statement else_statement
        '''

        pass


def p_E(t):
    '''E : expression'''
    t[0] = t[1]


def p_E_1(t):
    '''E : LEN LPAR ID RPAR'''
    t[0] = len(id_table[t[3]])


def p_E_2(t):
    '''E : STR LPAR ID RPAR'''
    t[0] = str(id_table[t[3]])


def p_E_3(t):
    '''E : CHOP LPAR ID RPAR'''
    t[0] = int(id_table[t[3]])


def p_E_4(t):
    '''E : ID LBRACKET NUMBER RBRACKET
        | ID LBRACKET NUMBER COLON NUMBER RBRACKET
        | ID LBRACKET COLON NUMBER RBRACKET
        | ID LBRACKET NUMBER COLON RBRACKET
        '''
    if len(t) == 5:
        t[0] = id_table[t[1]][t[3]]

    elif len(t) == 7:
        t[0] = id_table[t[1]][t[3]:t[5]]

    elif len(t) == 6:
        if t[3] == ':':
            t[0] = id_table[t[1]][:t[4]]
        elif t[4] == ':':
            t[0] = id_table[t[1]][t[3]:]

def p_expression(t):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression POW expression'''
    if t[2] =='+':
        t[0] = t[1] + t[3]
    elif t[2] =='-':
        t[0] = t[1] - t[3]
    elif t[2] == '*':
        t[0] = t[1] * t[3]
    elif t[2] == '/':
        t[0] = t[1] / t[3]
    elif t[2] == '^':
        t[0] = t[1] ** t[3]


def p_expression_group(t):
    'expression : LPAR expression RPAR'
    t[0] = t[2]



def p_expression_number(t):
    'expression : NUMBER'
    t[0] = int(t[1])


def p_expression_number_float(t):
    'expression : NUMBER_FLOAT'
    t[0] = float(t[1])



def p_expression_name(t):
    'expression : ID'
    t[0] = id_table[t[1]]


def p_expression_name_str(t):
    'expression : TEXT'
    t[0] = t[1]


def p_error(t):
    print("Syntax error at '%s'" % t.value)


test = '''
/* comment block */
{
    print(2+3*5);
    c:= "hello";
    o:= len(c);
    print(o);
    f:=2;
    b:=5;
    a:= b-(f*0.25);
    c:= chop(a);
    print("hello" , a);
    print(c);
    if(f<b){
    print("enter if");
}
else{
    print("enter else");

}
}
/* comment block */
'''


# lexer.input(test)
# while True:
#     tok = lex.token()
#     print(tok)
#     if not tok: break

import ply.yacc as yacc
parser = yacc.yacc()

address = input(">> File name: ")
if(address==''):address = 'input.txt'
try:
    input_file = open(address,'r')
except (FileNotFoundError, IOError):
    print('ERROR: FILE NOT FOUND!')

input_lines = input_file.readlines()

input_file.close()
input_str = ''
for line in input_lines:
    input_str += line

parser.parse(input_str)

print(id_table)
