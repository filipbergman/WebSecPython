import sys
import os
import hashlib
# Assignment 0
#1
s = "0123456789abcdef"
value = int(s, 16)

print (value)

#2
b = bytearray().fromhex(s)
hash = hashlib.sha1(b)
pbHash = int(hash.hexdigest(), 16)
print(pbHash)

#3
i = 2897
int_byte = i.to_bytes(4, "big")
stringOfByte = int_byte.hex()
print(stringOfByte)

#4
int_hash = hashlib.sha1(int_byte)
hashDigest = int_hash.hexdigest()
print(hashDigest)

# Assignment 1B1
def luhn(card_number):
  lastDigit = card_number[len(card_number)-1]
  x_index = card_number.index('X')
    
  for i in range(10):
    card_list = list(card_number)

    if x_index != 15: # not really needed
      card_list[x_index] = str(i)

    for half_i in range(1, 9):
      change_index = len(card_number) - (2 * half_i)
      card_list[change_index] = int(card_list[change_index]) * 2
      if int(card_list[change_index]) >= 10:
        card_list[change_index] = int(str(card_list[change_index])[0]) + int(str(card_list[change_index])[1])
    
    sum = 0
    for k in range(0, 15):
      sum = sum + int(card_list[k])

    if x_index == 15:
      return (sum*9)%10

    if (sum*9)%10 == int(lastDigit):
      return i

long_card_list = "545703082263897XX069501594439909373X056473954904995416921652X782618765150324258X657739065780782X112966X6992142407191297798X662103479047159212X17924242132118X482887044195509333X779110X33746244241507695216769X4735042691063608X43111385653X47961647806024585X12852003588032826X9209261619684X93X3776456519537809863491787X578202930X17028577343301814721571317XX305696073949320552790127X521507X286148807493830369480670X919924317X7547408784062972049X8827068895892486596X387474970800629807X442166953839318X44X8578760742684105795443X3783990975852471198X4951X36372231360240X10844557657241254203626X550911631098X6562408762393778575X9740954284141768075X097X656341630030954735375X559039917785329X5910122017X448693528739319241X5826948397025X22679866253557188672486X16500083470456294X4845143877X311165395952910X4941670382X7947589846223138348X89727605448344112X9902645918413430626X333369070X1131507410174527X0969592053055X86024297518155543661X1014764431311756822X33589137746867X5X8001514270012298959006872X310120481998X88623862932040812X65985245534395367665X8X165168544234952404X536815702887060X2816552959021606184553X8231112952X178593412275183839309552X96119356127478X4068698101X17948861995X86951862219299X1225314712094182X43771396697691X334648653806981935828326937X2867324932660X58580X5036374501431326585822X4134126979X521093340475345X3839443029716672004X47664838799X924389406242X161203801444444X38072351989204532775255X2102261151196X36620816215169713X461284697X155414842946X786659263098444641798X123772744630401X8787534498288X3176861710X587516684357064806659728589216X6454X306754750551426X203704211967665984X38618374"
length = 16
cards = [long_card_list[i:i+length] for i in range(0, len(long_card_list), length)]

values = ""
for c in range(len(cards)):
  values = values + str(luhn(cards[c]))

print(values)

#Test
card1 = "12774212857X4109"
card2 = "586604X108627571"
card3 = "7473X86953606632"
card4 = "4026467X45830632"
card5 = "20X3092648604969"

print("CARD 1: ", luhn(card1))
print("CARD 2: ", luhn(card2))
print("CARD 3: ", luhn(card3))
print("CARD 4: ", luhn(card4))
print("CARD 5: ", luhn(card5))
#Test end

#Assignment 1B2
#Part 1
leaf = "2354cf006ef4eeefeddf29b9e68d5cb1918ed589"
node_str = "R69968f8d734080390646bd0f3afff78baadebd2bLed64e17870e63f55b71542f0818ff7639b1f9985L7a6ba60c80a893b7a02999b6415c6ec67d5883b4L64b64c7760e5559aefe701790ee0564af6458cb4L53f1eab7ccd09600908bc49044669cd8fc996171Rc5684eb22d8745a777037c19ff3eff85be800334L058e2c0d7d103a7b45b2a4408ac3389eb10048fe"
node_length = 41
node_list = [node_str[i:i+node_length] for i in range(0, len(node_str), node_length)]
letter_list = []

#Save and then remove the first character(R or L)
for i in range(len(node_list)):
    s = list(node_list[i])
    letter_list.append(s[0])
    node_list[i] = node_list[i][:0] + node_list[i][1:]

leaf_byte = bytearray().fromhex(leaf)

concat_ba = leaf_byte

for n in range(len(node_list)):
  print(letter_list[n])

  if letter_list[n] == 'L':
    concat_ba = bytearray().fromhex(node_list[n]) + concat_ba
  if letter_list[n] == 'R':
    concat_ba = concat_ba + bytearray().fromhex(node_list[n])

  hash = hashlib.sha1(concat_ba).hexdigest()
  concat_ba = bytearray().fromhex(hash)
 
print("HASH: ", hash)

#Part 2
