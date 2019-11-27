def dec_to_bin(dec):
    bin = ""
    while(dec > 0):
        bin = bin + str(dec % 2)
        dec = dec // 2
    return bin[::-1]
def bin_to_dec(binstr):
    mul = 1
    dec = 0
    for x in binstr[::-1]:
        dec = dec + int(x) * mul
        mul = mul * 2
    return dec