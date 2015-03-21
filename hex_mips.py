import sys

# Hex to MIPS converter. 
# Takes in a hex compiled program and spits out the MIPS equilivant
# Input: Machine Language Compiled File
# Output: TAL MIPS Language
# Author: Kuriakose Sony Theakanath

# Dictionaries: Follows 32 bit MIPS format from Berkeley's MIPS Green Sheet
# r_type_fx : R-Type Funct codes; i_type : I-Type Opcodes; j_type : J-Type Opcodes 
r_type_fx = {32 : 'add', 8 : 'addu', 36 : 'and', 8 : 'jr', 39 : 'nor', 37 : 'or', 42 : 'slt', 43 : 'sltu', 0 : 'sll', 2 : 'srl', 34 : 'sub', 35 : 'subu'}
i_type = {8 : 'addi', 9 : 'addiu', 12 : 'andi', 4 : 'beq', 5 : 'bne', 36 : 'lbu', 37 : 'lhu', 48 : 'll', 15 : 'lui', 35 : 'lw', 13 : 'ori', 10 : 'slti', 11 : 'sltiu', 40 : 'sb', 56 : 'sc', 41 : 'sh', 43 : 'sw'}
j_type = {'j' : 2, 'jal' : 3}
registers = {0: '$0', 1 : '$at', 2 : '$v0', 3 : '$v1', 4 : '$a0', 5 : '$a1', 6 : '$a2', 7 : '$a3', 8 : '$t0', 9 : '$t1', 10 : '$t2', 11 : '$t3', 12 : '$t4', 13 : '$t5', 14 : '$t16', 15 : '$t17', 16: '$s0', 17 : '$s1', 18 : '$s2', 19 : '$s3', 20: '$s4', 21 : '$s5', 22 : '$s6', 23: '$s7', 24 : '$t8', 25 : '$t9', 26 : '$k0', 27 : '$k1', 28 : '$gp', 29 : '$sp', 30 : '$fp', 31 : '$ra'}

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

def check_inst_type(str0):
	"""Takes in a binary string and calls the certain function that returns
	a correct instruciton type.

	"""
	opcode = int(str0[0:6], 2)
	if opcode == 0:
		function = r_type_fx.get(int(str0[26:32], 2))
		rs = int(str0[6:11], 2)
		rt = int(str0[11:16], 2)
		rd = int(str0[16:21], 2)
		shamt = str(int(str0[21:26], 2))
		if function != 'sll' and function != 'srl':
			return function + " " + registers.get(rd) + ", " + registers.get(rs) + ", " + registers.get(rt)
		else:
			return function + " " + registers.get(rd) + ", " + shamt
	elif opcode == 2 or opcode == 3:
		addr = str(int(str0[6:32], 2))
		return j_type.get(opcode) + addr
	else:
		rt = int(str0[6:11], 2)
		rs = int(str0[11:16], 2)
		imm = str(int(str0[16:32], 2))
		return i_type.get(opcode) + " " + registers.get(rs) + ", " + registers.get(rt) +  ", " + imm

def convert(fname):
	l = convert_to_binary(read_file(fname))
	for elem in l:
		print(check_inst_type(elem))
