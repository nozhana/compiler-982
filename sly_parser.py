from sly import Parser
from sly_lexer import CalcLexer

class CalcParser(Parser):
    tokens = CalcLexer.tokens
    temp = []
    stack = []
    in_pow = 0
    in_mul = 0
    in_min = 0
    in_add = 0
    in_dev = 0
    in_no = 0
    in_eq = 0
    in_lt = 0
    in_gt = 0
    in_lab = 0

    @_('LBRACE BODY RBRACE')
    def S(self, p):
        self.temp.append("")

    @_('CODE BODY')
    def BODY(self, p):
        self.temp.append("")

    @_('CODE')
    def BODY(self, p):
        self.temp.append("")

    @_('EXPR SEMICOLON')
    def CODE(self, p):
        self.temp.append("")

    # @_('ID ASSIGN E SEMICOLON')
    # def CODE(self, p):
    #     self.temp.append("MOV " + str(p.E) + ",," + str(p.ID))

    @_('WHILE LPAR CON RPAR LBRACE BODY RBRACE')
    def CODE(self, p):
        p2 = self.stack.pop()
        p1 = self.stack.pop()
        self.temp.append("JMP " + str(p1))
        self.temp.append(str(p2) + ":")

    @_('IF LPAR CON RPAR LBRACE BODY1 RBRACE ELSE LBRACE BODY RBRACE')
    def CODE(self, p):
        p3 = self.stack.pop()
        self.temp.append(str(p3) + ":")

    @_('CODE BODY1')
    def BODY1(self, p):
        self.temp.append("")

    @_('CODE')
    def BODY1(self, p):
        p2 = self.stack.pop()
        p1 = self.stack.pop()
        LAB = "lab" + str(self.in_lab)
        self.stack.append(LAB)
        self.in_lab = self.in_lab + 1
        self.temp.append("JMP " + str(LAB))
        self.temp.append(str(p2) + ":")

    @_('ID ASSIGN E')
    def EXPR(self, p):
        self.temp.append("MOV " + str(p.E) + ",," + str(p.ID))

    @_('E NOTEQUAL E')
    def CON(self, p):
        f5 = "no" + str(self.in_no)
        LAB = "lab" + str(self.in_lab)
        self.stack.append(LAB)
        self.in_lab = self.in_lab + 1
        self.temp.append(str(LAB) + ":" + "NOTEQUAL " + str(p[0]) + "," + str(p[1]) + "," + str(f5))

        LAB = "lab" + str(self.in_lab)
        self.stack.append(LAB)
        self.temp.append("JMPF " + str(f5) + ",," + str(LAB))
        self.in_lab = self.in_lab + 1
        self.in_no = self.in_no + 1
        return f5

    @_('E EQUAL E')
    def CON(self, p):
        f6 = "eq" + str(self.in_eq)

        LAB = "lab" + str(self.in_lab)
        self.stack.append(LAB)
        self.in_lab = self.in_lab + 1
        self.temp.append(str(LAB) + ":" + "EQ " + str(p[0]) + "," + str(p[1]) + "," + str(f6))

        LAB = "lab" + str(self.in_lab)
        self.stack.append(LAB)
        self.temp.append("JMPF " + str(f6) + ",," + str(LAB))
        self.in_lab = self.in_lab + 1
        self.in_eq = self.in_eq + 1
        return f6

    @_('E LESS E')
    def CON(self, p):
        f7 = "" + str(self.in_lt)
        self.in_lt = self.in_lt + 1

        LAB = "lab" + str(self.in_lab)
        self.stack.append(LAB)
        self.in_lab = self.in_lab + 1
        self.temp.append(str(LAB) + ":" + "LT " + str(p[0]) + "," + str(p[1]) + "," + str(f7))

        LAB = "lab" + str(self.in_lab)
        self.stack.append(LAB)
        self.temp.append("JMPF " + str(f7) + ",," + str(LAB))
        self.in_lab = self.in_lab + 1
        return f7

    @_('E GREATER E')
    def CON(self, p):
        f8 = "no" + str(self.in_gt)

        LAB = "lab" + str(self.in_lab)
        self.stack.append(LAB)
        self.in_lab = self.in_lab + 1
        self.temp.append(str(LAB) + ":" + "GT " + str(p[0]) + "," + str(p[1]) + "," + str(f8))

        LAB = "lab" + str(self.in_lab)
        self.stack.append(LAB)
        self.temp.append("JMPF " + str(f8) + ",," + str(LAB))
        self.in_lab = self.in_lab + 1
        self.in_gt = self.in_gt + 1
        return f8

    @_('E MINUS T')
    def E(self, p):
        f3 = "min" + str(self.in_min)
        self.temp.append("SUB " + str(p[0]) + "," + str(p[1]) + "," + str(f3))
        self.in_min = self.in_min + 1
        return f3

    @_('E PLUS T')
    def E(self, p):
        f4 = "add" + str(self.in_add)
        self.temp.append("ADD " + str(p.E) + "," + str(p.T) + "," + str(f4))
        self.in_add = self.in_add + 1
        return f4

    @_('T')
    def E(self, p):
        return p.T

    @_('T DIV F')
    def T(self, p):
        f1 = "div" + str(self.in_dev)
        self.temp.append("DIV " + str(p.T) + "," + str(p.F) + "," + str(f1))
        self.in_dev = self.in_dev + 1
        return f1

    @_('T MUL F')
    def T(self, p):
        f2 = "mul" + str(self.in_mul)
        self.temp.append("MUL " + str(p.T) + "," + str(p.F) + "," + str(f2))
        self.in_mul = self.in_mul + 1
        return f2

    @_('F')
    def T(self, p):
        return p.F

    @_('LPAR E RPAR')
    def D(self, p):
        self.temp.append("")

    @_('F POW D')
    def F(self, p):
        f0 = "pow" + str(self.in_pow)
        self.temp.append("POW " + str(p.F) + "," + str(p.D) + "," + str(f0))
        self.in_pow = self.in_pow + 1
        return f0

    @_('D')
    def F(self, p):
        return p.D

    @_('NUMBER')
    def D(self, p):
        return p.NUMBER

    @_('ID')
    def D(self, p):
        return p.ID
