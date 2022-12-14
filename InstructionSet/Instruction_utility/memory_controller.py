import sys
sys.path.append('../OSproject')
from Utilities.base_conversions import twoBytesToInt
from Architecture.Memory import R, memory, pc, zeroRegister


# PC/memory operations

def fetchRegister(): #fetches the register in memory currently and updates Pc
    error = False
    register_number =memory[pc.getInt()]

    if(register_number > 15 and register_number < 32):
        error = "Error: Cannot change to special purpose register R[" +str(register_number-16) +"]"
        return [zeroRegister, error] #register unchanged because error 

    elif(register_number >= 32):
        error = "Error: No such register R[" +str(register_number-16) +"]"
        return [zeroRegister, error] #register unchanged because error

    R1 = R[register_number]
    pc.inc()
    return [R1, error]

def fetchImmediate(): #fetches the 2 byte immediate value in memory currently and updates PC
    error = False
    temp = bytearray(2)
    temp[0] = memory[pc.getInt()]
    pc.inc()
    temp[1] =  memory[pc.getInt()]
    immediate = twoBytesToInt(temp)
    pc.inc()
    return [immediate]