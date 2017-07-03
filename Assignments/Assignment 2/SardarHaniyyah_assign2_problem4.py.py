"""
Name: Haniyyah Sardar
Date Due: 2/8/17
Class Section: 05
Name: "Data Size Converter"
"""

#ask user for filze size input
kb = input("Enter a file size, in kilobytes (KB): ")

#line break
print()

#print out the size they gave in KB again
print(kb, "KB ...")

#line break
print()

fkb = float(kb)
bits = fkb * 1024 * 8
byt = fkb * 1024
mb = fkb / 1024
gb = mb / 1024

#format to two decimal places and spacing
fbits = format(bits,",.2f")
fbyt = format(byt,",.2f")
fmb = format(mb, ".2f")
fgb = format(gb,".2f")
#output these all to the user
print("... in bits\t",str(fbits),"\tbits")
print("... in bytes\t",str(fbyt), "\tbytes")
print("... in megabytes\t",str(fmb),"\tMB")
print("... in gigabytes\t",str(fgb),"\tGB")



