import sys
sys.path.append('../OSproject')
from Architecture.Memory import flagRegister

# 1) This file contains set, clear, get functions for carry, zero, sign and overflow flags
# 2) It also has the Arithmetic, Logical, Shift tests for operations that affect the flag

#set flags
def setCF():
    flagRegister.setInt(flagRegister.getInt() | 0x1)

def setZF():
    flagRegister.setInt(flagRegister.getInt() | 0x2)

def setSF():
    flagRegister.setInt(flagRegister.getInt() | 0x4)

def setOF():
    flagRegister.setInt(flagRegister.getInt() | 0x8)

#clear flags
def clearCF():
    flagRegister.setInt(flagRegister.getInt() & 0xFFFE)

def clearZF():
    flagRegister.setInt(flagRegister.getInt() & 0xFFFD)

def clearSF():
    flagRegister.setInt(flagRegister.getInt() & 0xFFFB)

def clearOF():
    flagRegister.setInt(flagRegister.getInt() & 0xFFF7)


def ArithmeticLogicalFlagTest(sum: int, num1: int, num2: int):
    if(sum == 0): setZF() #when the results is 0
    if(sum > 0x8000): setSF() #when the most significant bit is 1
    if((num1^sum)&(num2^sum)&0x8000): setOF() #when sign of both inputs is different from the sign of the result

def shiftRotateFlagTest(before: int, after: int): 
    if(after == 0): setZF() #when the results is 0
    if(before > 0x8000): setCF() #when the most significant bit is 1 before operation
    if(after > 0x8000): setSF() #when the most significant bit is 1 after operation
    pass



