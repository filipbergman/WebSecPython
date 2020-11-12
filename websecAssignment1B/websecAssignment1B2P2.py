import sys
import os
import hashlib

#Part 2 ------------------------------------------------------------------------------------------------
print("Assignment 1B2 part 2")
with open('leaves.txt') as f:
  leaf_list = f.readlines()
leaf_list = [x.strip() for x in leaf_list] 

start_leaf_index = int(leaf_list.pop(0))
depth_val = int(leaf_list.pop(0))

depth_list = []
depth_list.append(leaf_list)
i = 0
while len(depth_list[i]) > 1:
  depth_list.append([])
  for k in range(int(len(depth_list[i]) / 2)):
    left_node = bytearray.fromhex(depth_list[i][k * 2])
    right_node = bytearray.fromhex(depth_list[i][k * 2 + 1])
    #print(depth_list[i][k * 2], " : ", depth_list[i][k * 2 + 1])
    
    concat_ba = left_node + right_node

    hash = hashlib.sha1(concat_ba).hexdigest()
    depth_list[i+1].append(hash)

  # Check if odd amount of nodes, if true, duplicate the last node and append to list on one lower depth
  if len(depth_list[i]) % 2 != 0:
    print("ODD: ", len(depth_list[i]))
    node_to_duplicate = depth_list[i][len(depth_list[i]) - 1]
    depth_list[i].append(node_to_duplicate)
    depth_list[i + 1].append(hashlib.sha1(bytearray.fromhex(node_to_duplicate) + bytearray.fromhex(node_to_duplicate)).hexdigest())
  
  #print("LIST: ", depth_list[i])
  print("LENGTH: ", len(depth_list[i]), "\n")
  i = i + 1

#print("DEPTH LIST: ", depth_list)

#Put L/R in front of each node:
for i in range(len(depth_list) - 1):
  for k in range(len(depth_list[i])):
    if k % 2 == 0:
      depth_list[i][k] = "L" + depth_list[i][k]
    else: 
      depth_list[i][k] = "R" + depth_list[i][k]

#Get the right path:
path_list = []
if start_leaf_index % 2 == 0:
  path_list.append(depth_list[0][start_leaf_index + 1])
else:
  path_list.append(depth_list[0][start_leaf_index - 1])

next_index = start_leaf_index
for i in range(len(depth_list) - 2):
  next_index = int(next_index / 2)
  if next_index % 2 == 0:
    path_list.append(depth_list[i+1][next_index + 1])
  else:
    path_list.append(depth_list[i+1][next_index - 1])

#print("PATH LIST: ", path_list)

final_concatenation = path_list[len(path_list) - depth_val] + depth_list[len(depth_list)-1][0]
print(final_concatenation)
#print("LENGTH: ", len(final_concatenation))