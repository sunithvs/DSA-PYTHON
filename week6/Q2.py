def alldistinct(a,b,c):
  if a != b:
    if b != c:
      if a != c:
        result = True
      else:
        result = False
    else:
      result = False
  else:
    result = False

  return (result)

print(alldistinct(1,2,1))