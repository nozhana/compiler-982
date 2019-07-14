class Assembly:
    def __init__(self):    
        self.registers = [None for i in range(1000)]
        self.label = 0
    
    def getLabel(self):
        labelStr = "Label%s" % (self.label)
        self.label += 1
        return labelStr

    def mov(self , y):
        firstNoneIndex = self.registers.index(None)
        self.registers[firstNoneIndex] = 1
        move = "MOV R"+str(firstNoneIndex)+"," + str(y)+"\n";
        return firstNoneIndex,move

    def movAddr(self, address):
        firstNoneIndex = self.registers.index(None)
        self.registers[firstNoneIndex] = 1
        move = "MOV R"+str(firstNoneIndex)+",R" + str(address)+"\n";
        return firstNoneIndex,move
    
    def movToOther(self, address1, address2):
        move = "MOV R"+str(address1)+",R" + str(address2)+"\n";
        return move

    def sub(self ,x ,y):
        return "SUB R"+str(x)+",R"+str(y)+"\n";

    def add(self ,x ,y):
        return "ADD R"+str(x)+",R"+str(y)+"\n";
    
    def addpr(self ,x ,y):
        return "ADDPRINT R"+str(x)+",R"+str(y)+"\n";

    def mul(self ,x ,y):
        return "MUL R"+str(x)+",R"+str(y)+"\n";

    def div(self ,x ,y):
        return "DIV R"+str(x)+",R"+str(y)+"\n";

    def power(self ,x ,y):
        return "POWER R"+str(x)+",R"+str(y)+"\n";

    def cmp(self, x, y):
        return "CMP R"+str(x)+",R"+str(y)+"\n";
    
    def jmp(self, label):
        return "JMP %s\n" % (label)

    def je(self, label):
        return "JE %s\n" % (label)

    def jne(self, label):
        return "JNE %s\n" % (label)

    def jgt(self, label):
        return "JGT %s\n" % (label)

    def jgte(self, label):
        return "JGTE %s\n" % (label)

    def jlt(self, label):
        return "JLT %s\n" % (label)

    def jlte(self, label):
        return "JLTE %s\n" % (label)

    def substr(self, variableAddr, sub):
        firstNoneIndex = self.registers.index(None)
        self.registers[firstNoneIndex] = 1
        code = "SUBSTR R%s,R%s,%s\n" % (firstNoneIndex, variableAddr, sub)
        return firstNoneIndex,code
    
    def inputf(self, messageAddr):
        firstNoneIndex = self.registers.index(None)
        self.registers[firstNoneIndex] = 1
        code = "INPUT R%s,R%s\n" % (firstNoneIndex, messageAddr)
        return firstNoneIndex,code

    def printf(self, messageAddr):
        code = "PRINT R%s\n" % (messageAddr)
        return code

    def strf(self, stringAddr):
        firstNoneIndex = self.registers.index(None)
        self.registers[firstNoneIndex] = 1
        code = "STR R%s,R%s\n" % (firstNoneIndex, stringAddr)
        return firstNoneIndex,code

    def lenf(self, stringAddr):
        firstNoneIndex = self.registers.index(None)
        self.registers[firstNoneIndex] = 1
        code = "LEN R%s,R%s\n" % (firstNoneIndex, stringAddr)
        return firstNoneIndex,code
    
    def chopf(self, stringAddr):
        firstNoneIndex = self.registers.index(None)
        self.registers[firstNoneIndex] = 1
        code = "CHOP R%s,R%s\n" % (firstNoneIndex, stringAddr)
        return firstNoneIndex,code