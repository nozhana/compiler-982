from sly import Lexer

class CalcLexer(Lexer):
    tokens = {NUMBER, PLUS, MINUS, DIV, MUL, LPAR, RPAR, POW, LBRACE,
              RBRACE, GREATER, LESS, EQUAL, NOTEQUAL,
              ID, STRING, ASSIGN, SEMICOLON, COMMA,
              PRINT,
              IF, WHILE, ELSE}

    ignore = r' \t'
    ignore_COMMENT = r'\/\*(.|\n)*?\*\/'

    PLUS = r'\+'
    MINUS = r'\-'
    DIV = r'\/'
    MUL = r'\*'
    POW = r'\^'
    LBRACE = r'\{'
    RBRACE = r'\}'
    GREATER = r'\>'
    LESS = r'\<'
    EQUAL = r'\='
    NOTEQUAL = r'\<\>'
    ASSIGN = r'\:='
    SEMICOLON = r'\;'
    COMMA = r'\,'
    LPAR = r'\('
    RPAR = r'\)'

    ID['if'] = IF
    ID['else'] = ELSE
    ID['while'] = WHILE
    ID['print'] = PRINT

    @_(r'[a-zA-Z_][a-zA-Z0-9_]*')
    def ID(self, t):
        return t

    @_(r'[0-9]+(\.[0-9]+)?')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    # @_(r'''[\"|\'][\w= ]+[\"|\']''')
    @_(r'''("[^"]*")|('[^']*')''')
    def STRING(self, t):
        temp = t.value[1:-1].replace('"', '\\"')
        t.value = ''.join(('"', temp, '"'))
        return t

    @_(r'\n+')
    def newline(self, t):
        self.lineno += t.value.count('\n')

    def error(t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)
