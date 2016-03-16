#!/usr/bin/python
__author__ = 'Riccardo Mutschlechner'


# I-format 1 instruction
# 5 bits  3-bits  3-bits 5-bits
# Opcode  Rs      Rd     Immediate
class Instruction_I1:
    def __init__(self, instruction):
        self.opcode = instruction[0:5]
        self.rs = instruction[5:8]
        self.rd = instruction[8:11]
        self.immediate = instruction[11:16]


# I-format 2 instruction
# 5 bits  3-bits  8-bits
# Opcode  Rs      Immediate
class Instruction_I2:
    def __init__(self, instruction):
        self.opcode = instruction[0:5]
        self.rs = instruction[5:8]
        self.immediate = instruction[8:16]


# J-format instruction
# 5 bits    11-bits
# Opcode    Displacement
class Instruction_J:
    def __init__(self, instruction):
        self.opcode = instruction[0:5]
        self.displacement = instruction[5:16]


# R-format instruction
# 5 bits  3-bits  3-bits  3-bits   2-bits
# Opcode  Rs      Rt      Rd       OpcodeExtension
class Instruction_R:
    def __init__(self, instruction):
        self.opcode = instruction[0:5]
        self.rs = instruction[5:8]
        self.rt = instruction[8:11]
        self.rd = instruction[11:14]
        self.opcode_ext = instruction[14:16]


# SPECIAL Instruction
# 5 bits  10-bits Don't Care (X)
# Opcode  XXXXXXXXXX
class Instruction_SPECIAL:
    def __init__(self, instruction):
        self.opcode = instruction[0:5]