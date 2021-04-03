import re
string = """
Sedona Red
Hex Color: #A71930;
rgb: (167,25,48)
HSB: (350,84,65)
CMYK: (23,100,83,17)
PANTONE: PMS 187 C
Buy Matching Paint
"""

def get_color(text):
  try:
    color_regex = r'(\#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})?)'             
    match = re.findall(color_regex, text)
    print(match)
    if match is not None : 
      color = match[0][0]
      return color
    else:
      return ""
  except: return ""

print(get_color(string))
print(get_color("#ffffff"))