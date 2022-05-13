num_atoms =3
print(" $IFREEZ(1) = ", end='\n')
for i in range(1,num_atoms*3+1):
  if(i%3 == 0):
    print(i, end=',\n')
  elif (i == num_atoms*3):
    print(i, end='\n')
  else:
    print(i, end=',')

print(" $END \n ")
