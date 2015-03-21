'''
This is a hex to MIPS converter. Handles binary converstion and the stuff.
Takes in a text file and outputs the likes

Prereqs: HEX file must be in TAL MIPS (Total Assembly Language), not Pseudo
Language
Output: TAL MIPS in readable format
For CS 61C.
'''

'''
The key values signify OPCODE, which are in decimal format, not hex
which are given by MIPS green sheet. 
'''

r_type_fx = {'add' : 32, 'addu' : 8, 'and' : 36, 'jr' : 8, 'nor' : 39, 'or' : 37, 'slt' : 42, 'sltu' : 43, 'sll': 0, 'srl' : 2, 'sub' : 34, 'subu' : 35}
i_type = {'addi' : 8, 'addiu' : 9, 'andi' : 12, 'beq' : 4, 'bne' : 5, 'lbu' : 36, 'lhu' : 37, 'll' : 48, 'lui' : 15, 'lw' : 35, 'ori' : 13, 'slti' : 10, 'sltiu' : 11, 'sb' : 40, 'sc' : 56, 'sh' : 41, 'sw' : 43}
j_type = {'j' : 2, 'jal' : 3}