a = 5
print(a)

a = int(5)
print(a)

a = 7
print(a)

a = 10
print(a)

a = a-4
print(a)

a = 8.56
b = 5
c = a+b
print(c)

a = float(5)
print(a)

a = 5+2
print(a)

b = 5-2
print(b)

c = 5*2
print(c)

d = 5/2
print(d)

a = 5
a += 2
print(a)

b = 12
b /= 3
print(b)

a = 2*2
print(a)

b = 5**3
print(b)

a = 32/6
print(a)

b = 32 // 6
print(b)

c = 32 % 6
print(c)

zodis1= "Labas"
print(zodis1)

zodis2 = str("vakaras")
print(zodis2)

print(zodis1+" " + zodis2)

print("Labas \nvakaras")

zodis = "Code Academy"
print(zodis[5])
print(zodis[-2])
print(zodis[5:12])
print(zodis[5:])

print(zodis[:4])
print(zodis[5:12:1])
print(zodis[5::2])
print(zodis[::-1])

print(zodis.split())
print(zodis.upper())
print(zodis.replace('c','k'))
print(zodis.replace("Code", "Music"))

zodis = "Labas"
dar_vienas= "Sitas zodis"

print("a lygu" + str(a) + ", zodis" + zodis +", dar vienas zodis -"+ dar_vienas)

print(f"a lygu {a}, zodis: {zodis}, dar vienas zodis - {dar_vienas}")

# d = "Zodis"
# e = 5
# print(d+e)

e = str(e)
print(d+e)

# a = "250"
# b = 4
# print(a*b)
# bus eror nes neleidzia str dauginti su int

a = input("Ivesk pirma zodi")
b = input("ivesk antra zodi")
print("jusu zodis ", a+b)

a = int(input("iveksite skaiciu"))
b = int(input("Iveskite antra skaiu"))
print("jusu skaicius", a+b)
h = float(input("ivesk flaota"))
print(h)

if 5>0:
    print("5 yr daugiau nei 0")
if 5<0:
    print("5 yra daugiau uz 0")
print("finished")

skaicius = 25

if skaicius<100:
    print("1: skaicius yra mazesnis uz 100")
if skaicius >10:
    print("2: skaicius yra didesnis uz 10")
if skaicius<10:
    print("3: Skaicius mazesnis uz 10")

skaicius = 60
if skaicius<70:
    print("skaicius mazesnis uz 70")
    if skaicius >15:
        print("Skaicius yra tarp 15 ir 70")
skaicius = 56
if skaicius ==50:
    print("1: skaicius yr lygus 50")
else:
    print("2:skaicius nelygs 50")

skaicius = 0

if skaicius >0 :
    print("teigiams skaicius")
elif skaicius == 0:
    print("Nulis")
else:
    print("Neigiamas skaicus")
