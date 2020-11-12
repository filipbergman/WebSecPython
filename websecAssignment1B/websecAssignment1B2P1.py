import sys
import os
import hashlib
#Assignment 1B2 -----------------------------------------------------------------------------------------------------------------
#Part 1
print("Assignment 1B2 part 1")
leaf = "2354cf006ef4eeefeddf29b9e68d5cb1918ed589"
#Better solution than a long string is used in part 2
node_str = "R69968f8d734080390646bd0f3afff78baadebd2bLed64e17870e63f55b71542f0818ff7639b1f9985L7a6ba60c80a893b7a02999b6415c6ec67d5883b4L64b64c7760e5559aefe701790ee0564af6458cb4L53f1eab7ccd09600908bc49044669cd8fc996171Rc5684eb22d8745a777037c19ff3eff85be800334L058e2c0d7d103a7b45b2a4408ac3389eb10048fe"
node_length = 41
node_list = [node_str[i:i+node_length] for i in range(0, len(node_str), node_length)]

#Better solution
with open('new.txt') as f:
  node_list = f.readlines()
node_list = [x.strip() for x in node_list] 
leaf = node_list[0]

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