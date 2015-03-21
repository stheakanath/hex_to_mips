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
i_type = {'addi' : 8, 'addiu' : 9, 'andi' : 12, }