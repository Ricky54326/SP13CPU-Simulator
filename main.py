#!/usr/bin/python
__author__ = 'Riccardo Mutschlechner'


from instruction import *  # locals
import argparse


# CPU State
pc = 0x0000
register_file = []


# Opcodes
i1_type = ["01000", "01001", "01010", "01011", "10100",
           "10101", "10110", "10111", "10000", "10001", "10011"]

i2_type = ["01100", "01101", "01110", "01111", "11000", "10010", "00101", "00111"]

j_type = ["00100", "00110"]

r_type = ["11001", "11011", "11010", "11100", "11101", "11110", "11111"]

special_type = ["00000", "00001", "00010", "00011"]

# Initializes the CPU
def init_cpu():
    pc = 0x0000
    register_file = [0 for i in range(8)]

# Returns instruction type ("I1", "I2", "J", "R", "SPECIAL", "INVALID")
def handle_instruction(instruction):

    if len(instruction) is not 16:
        print "Invalid Instruction Length (!16), exiting..."
        exit(-1)

    opcode = instruction[0:5]

    if opcode in i1_type:
        print "I-type 1"
        return Instruction_I1(instruction)

    elif opcode in i2_type:
        print "I-type 2"
        return Instruction_I2(instruction)

    elif opcode in j_type:
        print "J-type"
        return Instruction_J(instruction)

    elif opcode in r_type:
        print "R-type"
        return Instruction_R(instruction)

    elif opcode in special_type:
        print "SPECIAL-type"
        return Instruction_SPECIAL(instruction)

    else:
        print "INVALID OPCODE: ", opcode
        exit(-1)

def parse(instruction):
    return handle_instruction(instruction)

def main():
    print "Welcome to the WISC-SP13 Simulator!"

    # initialize CPU
    init_cpu()

    parser = argparse.ArgumentParser(description="WISC-SP13 CPU Simulator")
    parser.add_argument("-f", "--file", help="The file that contains the machine code to be read")

    #  Change to a loop obviously later, this is just proof of concept

    instruction = raw_input("Enter a machine code line (with or without spaces): ").replace(" ", "")
    print "Read: ", instruction
    instruction_obj = parse(instruction)



if __name__ == "__main__":
    main()