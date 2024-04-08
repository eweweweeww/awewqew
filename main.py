import re 
def resultado(data=response.json()):
  sssss = re.findall("'streamId': '(23.*?)'", str(data))
  if len(sssss) > 0:
    return sssss
  else:
    return False
    
