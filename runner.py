from sly_parser import CalcParser
from sly_lexer import CalcLexer
from asmRunner import assemblyRunner
import sys

def readFile(fileName) :
    import os.path
    fileExist = os.path.isfile(fileName)
    if fileExist :
        return open(fileName,'r').read()
    else :
        raise BaseException("File not found")

def writeFile(string) :
    with open(resultFileName, mode='w') as file:
        file.write( string )

if __name__ == '__main__':
    lexer = CalcLexer()
    parser = CalcParser()

    if not len(sys.argv) > 1 :
        raise BaseException('Enter filename/cli as command line argument.')
    else:
        code = sys.argv[1]

        if len(sys.argv) > 2:
            asm_file = sys.argv[2]
        else:
            asm_file = 'asm_text.txt'

        if code == 'cli':
            inp = input('>> ')
            for tok in lexer.tokenize(inp):
                print('type = %r, value = %r' % (tok.type, tok.value))
            result = parser.parse(lexer.tokenize(inp))
        else:
            for tok in lexer.tokenize(readFile(code)):
                print('type = %r, value = %r' % (tok.type, tok.value))
            result = parser.parse(lexer.tokenize(readFile(code)))

        print(parser.temp)
        print('Result: ', result)

        asm_code = '\n'.join(parser.temp)
        print(asm_code)
        # asmRunnerObj = assemblyRunner()
        # asmRunnerObj.main()
