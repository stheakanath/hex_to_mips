# hex_to_mips

Converts hex assembly code to TAL MIPS. Useful when testing Single Cycle CPU processing for 32 bit MIPS. 

# How to Use

Make sure you're in the current directory. Within that directory you have files, doctests. Place your .hex files there and call:

    python3 hex_to_mips.py <your file name>
  
An example of this is with the example code given in the doctests folder. To run these you would type in the interactive output:

     python3 hex_to_mips.py doctests/add.hex
  
And it would print out your TAL MIPS code! Happy Pipelining! 
