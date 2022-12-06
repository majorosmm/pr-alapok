'''print("Hello")

print('Hello')

a = "Hello"

print(a)
# ----------------------------------------------------------
a = """Lorem ipsum dolor sit amet,

consectetur adipiscing elit,

sed do eiusmod tempor incididunt

ut labore et dolore magna aliqua."""

print(a)

# ----------------------------------------------------------

a = "Hello, World!"

print(a[1])

print(a[4])

# ----------------------------------------------------------

for x in "banana":

  print(x, end='-')
# ----------------------------------------------------------
  
a = "hello world.asd2212dddada"
print(len(a))
print(a[11])
print(a[len(a)-1])
# ----------------------------------------------------------
a = 'hello world'
szamlalo = 1
for x in a:
    if szamlalo %2 == 0:
        print(a[szamlalo -1], end="")
    szamlalo = szamlalo + 
# ----------------------------------------------------------
    txt = "The best things in life are frese!"
print("free" in txt) 

b = "Hello, World!"
print(b[7:14]) # llo

c = "B"+b[1:8]
print(c)
# ----------------------------------------------------------
b= "Hello, world"
print (b[2:])
# ----------------------------------------------------------
a = "Hello, World!"
print(a.upper())
nagybetu = a.upper()
print(nagybetu)
# ----------------------------------------------------------
a = "   Hello, World!    "
print(a.strip())
b = a.strip()
print (len(a.strip()))
# ----------------------------------------------------------
a = "Jello, Jorld!"
print(a)
print(a.replace("J", "H"))
a = "Hello, world!"
print (a.split(","))
lista = a.split(",")
print (lista[1])
b = "44;341;223;333;54544"
print(b.split(";"))
lista1 = b.split(";")
print(lista1[3])
# ----------------------------------------------------------
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
# ----------------------------------------------------------
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
# ----------------------------------------------------------
a = "hello"
b = "world"
c = a +" "+  b 
print(c)
# ----------------------------------------------------------
print("ez \"egy\" string")


# ----------------------------------------------------------
print("ez \"egy\" string \n ez mar regy uj sor \t <---itt egy tabulator van ")

# ----------------------------------------------------------

print("sdafdsggsfa", end="\n\n\n")
print("sfsdfdasfa", end="\t")
print("sdasasdaswfa")
# ----------------------------------------------------------

szam = 0
while szam != 100:
  szam = szam +1
  print(szam)
print ("program vege")
# ----------------------------------------------------------
szam = 0
while szam != 100:
  print(szam)
  szam = szam +1
print ("program vege")
# ----------------------------------------------------------
szam = 1
while szam != 101:
  print(szam)
  szam = szam +1
print ("program vege")
# ----------------------------------------------------------
szam = 1
while True:
  print(szam)
  szam = szam +1
print ("program vege")'''
# ----------------------------------------------------------
szam = 0 
while szam < 100:
  szam = szam + 1 
  print(szam)