import random
def unic(num,list):
  is_unic = True
  for id in range(len(list)):
    if num == list[id]:
      is_unic = False
      break
  return is_unic
def check_missing_number(list):
  control = 0
  for id in list:
    if id != control:
      missing_number = control
      break
    else:
      control = control + 1
  return missing_number
list_num = []
j = 0
while j < 100:
  num = random.randint(0,100)
  if unic(num,list_num):
    list_num.append(num)
    j += 1
list_num.sort()
print(check_missing_number(list_num))
