from sly_parser import CalcParser
from sly_lexer import CalcLexer

if __name__ == '__main__':
    lexer = CalcLexer()
    parser = CalcParser()
    while True:
        try:
            _input = input(">> ")
            # f = open("input.txt", "r")
            # _input = str(f.read())
            _input.replace("'"," ")
            _input.replace("["," ")
            _input.replace("]"," ")
            print(_input)
            result = parser.parse(lexer.tokenize(_input))
            print (result)
            for t in parser.temp:
                if t != "":
                    print(t)
            break
        except EOFError:
            break
