import re 
def resultado(data=None):
  eusou_um_panda = re.findall("'streamId': '(23.*?)'", str(data))
  if len(eusou_um_panda) > 0:
    return eusou_um_panda
  else:
    return False
    
