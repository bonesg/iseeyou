import os

wl_block = []
worldlist = ''
prog_update_speed = 100000
wl_block_memory_max = 20000000
export_name = ''
export_name_index = 0
nwn = False # NUMBERS_STRING_NUMBERS

def generate(debug):
  global wl_block, prog_update_speed, export_name, export_name_index
  index = 0
  export_name_index += 1
  with open(export_name + str(export_name_index) + '.txt', 'w+') as f:
    for block in wl_block:
      f.write(block)
      index += 1
      if debug == True and index % prog_update_speed == 0:
        print(' [', index, ' | ', len(wl_block), ']')

def num_word_num(data, n1, n2, n3, n4, debug):
  global worldlist, wl_block

  initial_second_min = n3
  while n1 < n2:
    while n3 < n4:
      worldlist += str(n1) + data + str(n3) + '\n'
      n3 += 1
    wl_block += worldlist
    worldlist = ''
    if debug == True:
      print(' [', n1 * n3, '/', n2 * n4, ']')
    n3 = initial_second_min
    n1 += 1
  wl_block += worldlist
  worldlist = ''

def word_num(data, n1, n2, use_block, debug):
  global worldlist, wl_block, prog_update_speed

  while n1 < n2:
    worldlist += data + str(n1) + '\n'
    if n1 % 10000 == 0 or use_block == False:
      wl_block += worldlist
      worldlist = ''
    if debug == True and n1 % prog_update_speed == 0:
      print(' [', n1, '/', n2, ']')
    n1 += 1
  wl_block += worldlist
  worldlist = ''

def num_word(data, n1, n2, use_block, debug):
  global worldlist, wl_block, prog_update_speed

  while n1 < n2:
    worldlist += str(n1) + data + '\n'
    if n1 % 10000 == 0 or use_block == False:
      wl_block += worldlist
      worldlist = ''
    if debug == True and n1 % prog_update_speed == 0:
      print(' [ ', data, ' | ', n1, '/', n2, ']')
    n1 += 1
  wl_block += worldlist
  worldlist = ''

def display_options():
  print(' 1) Change Word')
  print(' 2) Numbers + Word')
  print(' 3) Word + Numbers')
  print(' 4) Numbers + Word + Numbers')
  print(' 99) Generate the List')

def custom_wordlist():
  global export_name
  export_name = str(input(' [ Export Wordlist Name ] -> '))
  data = str(input(' [ Word ] -> '))
  gen = 0
  while gen != 99:
    os.system('clear')
    display_options()
    gen = int(input(' -> '))
    if gen == 1:
      data = str(input(' [ Word ] -> '))
    elif gen == 2:
      n1 = int(input(' [ Min number ] -> '))
      n2 = int(input(' [ Max number ] -> '))
      num_word(data, n1, n2, True, False)
    elif gen == 3:
      n1 = int(input(' [ Min number ] -> '))
      n2 = int(input(' [ Max number ] -> '))
      word_num(data, n1, n2, True, False)
    elif gen == 4:
      n1 = int(input(' [ First Min number ] -> '))
      n2 = int(input(' [ First Max number ] -> '))
      n3 = int(input(' [ Second Min number ] -> '))
      n4 = int(input(' [ Second Max number ] -> '))
      num_word_num(data, n1, n2, n3, n4, False)
  generate(True)

def read_file(filename):
  data = []
  temp = ''
  with open(filename, 'r') as f:
    for c in f.read():
      if c == '\n':
        data.append(temp)
        temp = ''
      else:
        temp += c
  return data

def upgrade_wordlist():
  global wl_block, export_name
  export_name = str(input(' [ Export Wordlist Name ] -> '))

  # Allowing multiple wordlists.
  wl_paths = []
  path = ''
  while True:
    path = str(input(' [ Worldlist Path (Leave blank no more wordlist files) ] -> '))
    if path != '':
      wl_paths.append(path)
    else:
      break

  level1 = int(input(' [ Level \033[93mnum\033[0m + word ] -> '))
  level2 = int(input(' [ Level word + \033[93mnum\033[0m ] -> '))
  level3a = int(input(' [ Level \033[93mnum\033[0m + word + num ] -> '))
  level3b = int(input(' [ Level num + word + \033[93mnum\033[0m ] -> '))

  for wl_path in wl_paths:
    data = read_file(wl_path)
    index = 0
    for n in data:
      index += 1
      print(' [', wl_path, ' | ', index, ' / ', len(data),']')
      try:
        num_word(n, 0, level1, False, False)
        word_num(n, 0, level2, False, False)
        num_word_num(n, 0, level3a, 0, level3b, False)
      except:
        generate(True)
        wl_block = []
        num_word(n, 0, level1, False, False)
        word_num(n, 0, level2, False, False)
          num_word_num(n, 0, level3a, 0, level3b, False)

  generate(True)

def applay_roules(word, roules):
  global wl_block_memory_max, wl_block, nwn
  rev = False

  data = ''
  for roule in roules:
    # Generise (word + numb);
    if roule == 'jesus_years;':
      index = 0
      while index <= 2050:
        index += 10
        data += word + str(index) + '\n'
    elif roule == 'nwn;': # Checking if in config file is this option
      nwn = True
    elif roule == 'rev;':
      rev = True
    else:
      data += word + roule + '\n'
      data += roule + word + '\n'
      if rev == True and len(roule) > 1:
        index = len(roule) - 1
        tmp = ''
        while index != -1:
          tmp += roule[index]
          index -= 1
        data += word + tmp + '\n'
        data += tmp + word + '\n'
  if nwn == True:
    num1 = 0
    while num1 <= 100:
      num2 = 0
      while num2 <= 1000:
        data += str(num1) + word + str(num2) + '\n'
        num2 += 1
      num1 += 1
  return data
  
def upgrade_wordlist_roulebased():
  global wl_block, export_name
  # Init of rules.
  export_name = str(input(' [ Export Wordlist Name ] -> '))
  roules_file = str(input(' [ Roules File Path ] -> '))
  roules_data = read_file(roules_file)
  # Input of wordlists.
  wl_paths = []
  path = ''
  while True:
    path = str(input(' [ Worldlist Path (Leave blank no more wordlist files) ] -> '))
    if path != '':
      wl_paths.append(path)
    else:
      break
  # Going trough every wordlist.
  for wl_path in wl_paths:
    data = read_file(wl_path)
    index = 0
    for n in data:
      index += 1
      print(' [', wl_path, ' | ', index, '-', len(data), ' | ', n, ' | wl = ', len(wl_block),']')
      wl_block.append(applay_roules(n, roules_data))
      #if len(wl_block) >= 50: # Heap Out of memory prevention. Needs to be prevented.
      #        print(' [ Exporting... ]')
      #        generate(True)
      #        wl_block = []
  generate(True)

def main():
  os.system('clear')
  print(' 1) Custom Wordlist')
  print(' 2) Update Wordlists')
  print(' 3) Update Wordlist from Rouls')
  x = int(input(' -> '))

  if x == 1:
    custom_wordlist()
  if x == 2:
    upgrade_wordlist()
  if x == 3:
    upgrade_wordlist_roulebased()

main()
