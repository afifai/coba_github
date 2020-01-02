def sambutan():
    print("Halo apa kabar")
    print("Selamat malam")
    print("Selamat beristirahat")

def penjumlahan(a,b):
    return a+b

def kalkulator(a, b, op):
    if op == "+":
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
    else:
        print("Operasi tidak dikenal")

def cek_palindrom(kata):
    return kata == kata[::-1]
