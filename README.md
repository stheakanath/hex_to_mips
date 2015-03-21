# hex_to_mips

Converts hex assembly code to TAL MIPS. Useful when testing Single Cycle CPU processing for 32 bit MIPS. 

# How to Use

Run In the Current Directory
  python3 -i hex_to_mips.py
  
Now that you have access to the files, you can test out the example code given in the doctests folder. To run these you would type in the interactive output:

  convert("doctests/add.hex")
  
And it would print out your TAL MIPS code! Happy Pipelining! 
