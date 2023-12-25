import random
import matplotlib.pyplot as plt

mapping_dict = dict(zip(range(0,10),range(0,10)))

mapping_dict

for k in mapping_dict.keys():

  mapping_dict[k] = str(mapping_dict[k])

mapping_dict

for i in range(0,26):
  mapping_dict[10+i] = chr(65+i)

mapping_dict

random_numbers = list()

for i in range(0,100000):

  blank_str = str()

  random_digit = random.randint(0,35)
  blank_str = blank_str + mapping_dict[random_digit]

  random_digit = random.randint(0,35)
  blank_str = blank_str + mapping_dict[random_digit]

  for i in range(0,8):
    coin_toss = random.randint(0,1)

    if coin_toss == 1:

      random_digit = random.randint(0,35)
      blank_str = blank_str + mapping_dict[random_digit]

    else:
      break

  random_numbers.append(blank_str)

reverse_mapping_dict = dict()

for k in mapping_dict.keys():
  reverse_mapping_dict[mapping_dict[k]] = k

base_frequency = dict()

for blank_str in random_numbers:
  highest_digit = max(blank_str)
  highest_base = reverse_mapping_dict[highest_digit] + 1

  if highest_base in base_frequency.keys():
    base_frequency[highest_base] += 1
  else:
    base_frequency[highest_base] = 1

plt.bar(x=base_frequency.keys(),height=base_frequency.values())


