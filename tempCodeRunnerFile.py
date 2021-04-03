
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