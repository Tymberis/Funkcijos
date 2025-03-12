import math
import random
from random import randint

randint(0,5)
arr = [1,5,6,8,9,11,15]
# for i, num in enumerate(arr):
#     print(f"i-{i}, num-{num}")
# for i, num in enumerate(arr):
#     row += f"[{i}/{num}], "
# print(row)
def print_list_col(arr):
    for i, num in enumerate(arr):
        print(f"i-{i}, grade-{num}")

def print_list_row(arr):
    row = ""
    for i, num in enumerate(arr):
        row += f"[{i}/{num}] "
    print(row)
print_list_row(arr)

students_grades = [8,9,10,10,4,8,3,8,5,8]

print_list_row(students_grades)

print_list_col(students_grades)

def say_hi(): # nieko nepriima, nieko negrazina, jei nera - return
    print("hi")
say_hi()

def say_hi_to(name): # priima viena kintamaji, nieko negrazina
    print(f"hi, {name}")
say_hi_to("jonas")
say_hi_to("rolandas")

vardas = "julija"
say_hi_to(vardas)

list = [1,2,5]
say_hi_to(arr)


def sim_pi():
    return 3.14

pi_val = sim_pi()
print(pi_val)
print(sim_pi())

print(math.pi)

def make_initials(name, surname):
    return (name[0] + surname[0].upper())

pavarde = "marozaitis"
initials = make_initials(vardas, pavarde)

print(initials)
print("\====================1=======================/")
def suma(sk1,sk2):
    sums = sk1 + sk2
    print(f"sk1 - {sk1}, sk2- {sk2}, suma -{sums}")
suma(6,15)
print("\====================2=======================/")
def pisq():
    return 9.8596
funkcija = pisq()
print(funkcija)
print("\====================3=======================/")
def sandauga(sk1,sk2):
    daugyba = sk1 * sk2
    print(f"sk1 - {sk1}, sk2- {sk2}, sandauga - {daugyba}")
sandauga(6,15)
print("\====================4=======================/")
def masyv(mas):
    for kk in mas:
        print(kk)
masyvas = [5,8,9,11,25]
print(masyvas)
print("\====================5=======================/")
def kintamieji(minim,maximum):
    return random.randint(minim,maximum)
skaiciai1 = kintamieji(1,25)
print(skaiciai1)
skaiciai2 = kintamieji(5,17)
print(skaiciai2)

print("\====================6=======================/")
def random_int(minimalus,maximalus,length):
    rezultatas = []
    for i in range(length):
        rezultatas.append(random.randint(minimalus,maximalus))
    return rezultatas

masyv_sk = random_int(1,2,5)
print(masyv_sk)
print("\====================7=======================/")
def suma_arr(arr):
    viso = 0
    for i in arr:
        viso += i
    return viso
masyvv = masyv_sk
sumaa = suma_arr(masyvv)
print(f"masyvas: {masyvv}")
print(f"masyvo suma: {sumaa}")
print("\====================8=======================/")
def vid_arr(sss):
  return sum(sss) / len(sss)
masyvaas = masyv_sk
vidurkis = vid_arr(masyvaas)
print(masyvaas)
print(f"vidurkis: {vidurkis}")
print("\====================9=======================/")
def print_staciak(isor,vidin):
    for i in range(isor):
        for v in range(vidin):
            print("*", end=" ")
        print()
print_staciak(5,9)
print("\====================10=======================/")
def print_simb_tarpai(sak):
    viso_simb = len(sak.replace(" ", ""))
    viso_tarpu = 0
    for tarp in sak:
        if tarp == " ":
            viso_tarpu += 1
    print(f"simboliai: {viso_simb}")
    print(f"tarpai: {viso_tarpu}")
sakinys = "Šiandien labai graži diena"
print_simb_tarpai(sakinys)
print("\====================11=======================/")
def apsukimas(sak):
    return sak[::-1]
kodavimas = apsukimas(sakinys)
print(f"sakinys: {kodavimas}")
print("\====================SUNKESNI=======================/")
print("\========================1=======================/")
def print_argument(tekstas):
    return "---" + tekstas + "---"
tekstukas = "Šiandien yra kovo 10"
argumentavimas = print_argument(tekstukas)
print(argumentavimas)
print("\========================2=======================/")
def generateRndStr(length):
    symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ12345678901234567890"
    text = ""
    for i in range(length):
        text += symbols[random.randint(0, len(symbols) - 1)]
    return text
def nextas(txt):
    skaic = ""
    for s in txt:
        if s.isdigit():
            skaic += s
        else:
            if skaic:
                print(f"[{skaic}]")
                skaic = ""
            print(s)
    if skaic:
        print(f"[{skaic}]")
random_stringas = generateRndStr(10)
print(random_stringas)
print("\nSimboliai pagal reikalavimus:")
nextas(random_stringas)
print("\========================3=======================/")
def print_sveiki_sk(n):
    if n <= 1:
        return 0
    count = 0
    for i in range(2, n):
        if n % i == 0:
            count += 1
    return count
print(print_sveiki_sk(10))
print(print_sveiki_sk(20))
print("\========================4=======================/")
def print_sveiki_sk(n):
    if n <= 1:
        return 0
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count
def masyvo_generavimas():
    masyvas = []
    for i in range(100):
        gen_masyv = random.randint(33,77)
        masyvas.append(gen_masyv)
    return masyvas
def rusiavimas(masyvas):
    return sorted(print_sveiki_sk,reverse=True)
masyvas = masyvo_generavimas()
rusiuotas = rusiavimas(masyvas)
print(rusiuotas)
print("\========================5=======================/")
elementai = []
for el in range(100):
    sk = random.randint(333,777)
    elementai.append(sk)
print(elementai)
def pirminis(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
pirminiu_sk = 0
for skaicius in elementai:
    if pirminis(skaicius):
        pirminiu_sk += 1
print(f"Prime number count : {pirminiu_sk}")
print("\========================6=======================/")
# def generate_arr():
#     ilgis = random.randint(10,20)
#     for i in range(ilgis - 1):
#         array = random.randint(0,10)
#     return array
# def generate_multiple_arr():
#     num_arr = random.randint(10,30)
#     rezultatas = []
#     for k in range(num_arr-1):
#         rezultatas.append(generate_arr())
#     paskutinis_masyv = generate_arr()
#     rezultatas.append(paskutinis_masyv)
#     return rezultatas
# pgr_masyv = generate_multiple_arr()
# print(pgr_masyv)
print("\========================7=======================/")
print("\========================8=======================/")
# def prime(p):
#     if p <= 1:
#         return False
#     for i in range(2, p):
#         if p % i == 0:
#             return False
#     return True
# def print_masyv_3():
#     arr = []
#     for i in range(3):
#         randomas = random.randint(1,33)
#         arr.append(randomas)
#     return arr
#     while True:
#     if prime(arr[-1]) and prime(arr[-2]) and prime(arr[-3]):
#         break
#     else:
#         arr.apend(random.randint(1,33))
#     return arr
# print(generate_arr())
print("\========================9=======================/")
# Sugeneruokite masyvą iš 10 elementų, kurie yra masyvai iš 10 elementų, kurie yra atsitiktiniai skaičiai nuo 1 iki 100.
# def pirminis(p):
#     if p <= 1:
#         return False
#     for i in range(2,p):
#         if p % i == 0:
#             return False
#     return True
# def gener_masyv():
#     masyv = []
#     for p in range(10):
#         vid_masyv = []
#         for v in range(10):
#             vid_masyv.append(random.randint(1,100))
#         masyv.append(vid_masyv)
#     return masyv
# def veiksmai(masyv):
# pirminiai = []
# for x in masyv:
#     if pirminis(x):
#         pirminiai.append(x)
#     vidurkis = sum(pirminiai) / len(pirminiai)
#     if vidurkis < 70:
#         maziausias = min(masyvas)
#         indeks = masyv.index(maziausias)
#         masvy[indeks] += 3
#
#
#
# masyvas = gener_masyv()
# print(masyvas)
# Jeigu tokio didelio masyvo (ne atskirai mažesnių) pirminių skaičių vidurkis mažesnis už 70, suraskite masyve mažiausią skaičių (nebūtinai pirminį) ir prie jo pridėkite 3.
