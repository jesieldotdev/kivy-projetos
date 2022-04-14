import re

txt = "The rain in Spain"
x = re.search("Spain", txt).span()
print(x)