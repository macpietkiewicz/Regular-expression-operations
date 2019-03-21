"""-----------------------BIBLIOTEKI-------------------------------------------"""
import re

"""-------------------------FUNKCJE--------------------------------------------"""
def czytaj_plik(name_file):
    try:
        file = open(name_file, 'r')
        text = file.readlines() 
    except IOError:
        print("Blad odczytu pliku")
        text = {}
        
    file.close()
    return text

def Searching(pattern,DNA,file_name):
    wyniki = open(file_name,'w')
    for dna in DNA:
        wystepowanie = re.search(pattern,dna)
        pozycja = re.finditer(pattern,dna)
        if wystepowanie:
            wyniki.write('\n')
            wyniki.write('\nsekwencja:\n')
            wyniki.write(dna)
            wyniki.write('\n')
            wyniki.write('jest ')
            wyniki.write(pattern)
            wyniki.write(' ')
        
            
            for i in pozycja:
                wyniki.write(str(i.span()) + ' , ')
                wyniki.write('\n')
                
                #dopasowanie = i.span()
                #wyniki.write(' na')
                #wyniki.write('\n')
                #wyniki.write(str(dopasowanie))
                
                
        else:
           wyniki.write("sekwencja: " + str(dna) + "\nbrak\n")

    
    
"""-----------------OTWIERANIE--PLIKÓW-WEJŚCIOWYCH/WYJŚCIOWYCH-----------------"""

          
"""----------------------DEKLARACJA--ZMIENNYCH---------------------------------"""
pattern1 = r"(GC)"
pattern2 = r"G.C|C.G"
pattern3 = r"GC[ACTG]{1,6}CG"
pattern4 = r"CA+C"
            
"""-----------------------WYWOŁANIE--FUNKCJI-----------------------------------"""

DNA = czytaj_plik('file.txt')
search1 = Searching(pattern1,DNA,'1.txt')
search2 = Searching(pattern2,DNA,"2.txt")
search3 = Searching(pattern3, DNA,"3.txt")
search4 = Searching(pattern4, DNA,"4.txt")

"""---------------------WYŚWIETLENIE--WYNIKÓW----------------------------------"""


"""----------------------ASSERTY-----------------------------------------------"""


"""-----------------ZAMYKANIE--PLIKÓW-WEJŚCIOWYCH/WYJŚCIOWYCH------------------"""

