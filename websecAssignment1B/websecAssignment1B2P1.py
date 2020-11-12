import sys
import os
import hashlib
#Assignment 1B2 -----------------------------------------------------------------------------------------------------------------
#Part 1
print("Assignment 1B2 part 1")
with open('leafAndNotes.txt') as f:
  node_list = f.readlines()
node_list = [x.strip() for x in node_list] 
leaf = node_list.pop(0)
print(node_list)

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