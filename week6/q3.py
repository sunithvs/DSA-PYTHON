def evenpositions(l):
  if len(l) == 0:
    return([])
  else:
    return([l[0],*evenpositions(l[2:])])

print (evenpositions([1,2,3,4,5,6,7,8,9,10]))