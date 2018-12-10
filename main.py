print("Hello World!")

# ini komentar single line

"""
    Ini komentar multi line
"""
gedung = "Gd. Menara Tujuh"
tinggi = 7
pi = 3.14
is_alive = True  #tipe variable bisa berubah2

print(gedung)
print(tinggi)
print(pi,is_alive)

#list
hari = ['ahad','senin','selasa','rabu','kamis','jumat', 'sabtu', 'minggu']
print(hari)
print(hari[0])
print(hari[len(hari)-1])

#dictionary
antonim = {}
antonim['tinggi']='rendah'
antonim['gelap']='terang'
antonim['jauh']='deket'
print('Antonim jauh =',antonim['jauh'])

#CONTROL FLOW/IF
if is_alive == True:
    print('Its alive..........!')
elif is_alive == False:
    print('Its not alive..........!')
else:
    print('Its complicated!')
if is_alive and tinggi > 6 :
    print('Its high five!')

#LOOP
print('#LOOP:FOR')
for i in range(0,3):
    print(i)

print('#LOOP:FOR list')
for h in hari:
    print(h)

print('#LOOP:FOR list(2)')
for h in range(0, len(hari)-1):
    print(hari[h])

print('#LOOP:WHILE')
i = 0
while is_alive:
    print('Alive!')
    i = i + 1
    if i == 10:
        is_alive = False
