import random

def tebak(x):
    
    #kita nebak angka komputer
    
    angka_acak = random.randint(1,x) # dimasukkan sebuah angka acak dengan range antara 1 dan x kedalam variabel angka_acak. 
    tebak=0 #store value before using its contain
    while tebak != angka_acak :
        tebak = int(input(f'Tebak angka antara 1 dan {x}: '))
        if tebak < angka_acak :
            print('Maaf, coba lagi. Tebakan terlalu rendah')
        elif tebak> angka_acak :
            print('Maaf, coba lagi. Tebakan terlalu tinggi')
    
    print(f'Selamat, anda berhasil menebak angka {angka_acak} dengan benar !')
    
    #komputer nebak angka kita

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c' :
        if low != high :
            guess = random.randint(low,high)
        else :
            guess = low 
        feedback = input(f'apakah {guess} terlalu tinggi (H), terlalu rendah (L), atau benar (C) ?? ').lower()
        if feedback == 'h' :
            high = guess - 1
        elif feedback == 'l' :
            low = guess + 1
    
    print(f'Selamat, komputer berhasil menebak angka {guess} dengan benar !')
    
x=int(input('Masukkan batas atas angka : '))    
computer_guess(x)
    