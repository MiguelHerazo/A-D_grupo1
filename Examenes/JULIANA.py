
#PUNTO 2
#Dada una cadena, encuentre sus letras mayúsculas de forma recursiva con sus indices
def mayus_indi(string, ind=0):
  if ind >= len(string):
    return []
  if string[ind].isupper():
      return [(string[ind], ind)] + mayus_indi(string, ind + 1)
  else:
      return mayus_indi(string, ind + 1)

cadena = "julianA BetAncUR"
resultado = mayus_indi(cadena)
print(resultado)
