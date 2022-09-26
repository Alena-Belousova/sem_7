import people
ask = (input("хотите записать пользователя(+) или найти(-)или экспортировать в эксель(*)?: "))
if ask=='+':
  people.input_people()
elif ask=='-':
    people.output_people()
elif ask=='*':
    people.export()
else: 
    print('ошибка ввода')

   

