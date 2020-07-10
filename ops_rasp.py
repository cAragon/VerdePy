
def get_pi_serial():
  piserial = "0000000000000000"
  try:
    f = open('/proc/cpuinfo','r')
    for line in f:
      if line[0:6]=='Serial':
        piserial = line[10:26]
    f.close()
  except:
    piserial = "0000000000000000"
  return piserial
