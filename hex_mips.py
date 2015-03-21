# Hex to MIPS converter. 
# Takes in a hex compiled program and spits out the MIPS equilivant
# Input: Machine Language Compiled File
# Output: TAL MIPS Language
# Author: Kuriakose Sony Theakanath

# Dictionaries: Follows 32 bit MIPS format from Berkeley's MIPS Green Sheet
# r_type_fx : R-Type Funct codes; i_type : I-Type Opcodes; j_type : J-Type Opcodes 
r_type_fx = {'add' : 32, 'addu' : 8, 'and' : 36, 'jr' : 8, 'nor' : 39, 'or' : 37, 'slt' : 42, 'sltu' : 43, 'sll': 0, 'srl' : 2, 'sub' : 34, 'subu' : 35}
i_type = {'addi' : 8, 'addiu' : 9, 'andi' : 12, 'beq' : 4, 'bne' : 5, 'lbu' : 36, 'lhu' : 37, 'll' : 48, 'lui' : 15, 'lw' : 35, 'ori' : 13, 'slti' : 10, 'sltiu' : 11, 'sb' : 40, 'sc' : 56, 'sh' : 41, 'sw' : 43}
j_type = {'j' : 2, 'jal' : 3}

def read_file(fname):
	lines = open(fname).read().splitlines()
	return lines

def convert_to_binary(list):
	"""Converts hex line to binary, takes in a list of hex commands
	and returns a list of those lines converted to binary.

	>>> hex = read_file("doctests/add.hex")
	>>> bin = convert_to_binary(hex)
	>>> bin[0]
	'00111100000010000000000000110101'
	>>> bin[3]
	'00000001001010000101000000100000'
	"""
	to_return = []
	for elem in list:
		converted = ''.join('{0:04b}'.format(int(c, 16)) for c in elem)
		f = converted.zfill(32)
		to_return.append(f)
	return to_return