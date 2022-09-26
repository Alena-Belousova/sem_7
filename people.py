


def input_people():
  last_name = (input("Введите фамилию: "))
  print(last_name)
  name = (input("Введите имя: "))
  print(name)
  message =(input("Введите комментарий: "))
  print(message)
  phone_number = (input("Введите номер телефона без разделителей: ")) 
  file = open("C:\\Users\\Alena\\Desktop\\гикбрейнс\\python\\27.09\\book.txt", "w")
  file.write(last_name)
  file.write(" ")
  file.write(name)
  file.write(" ")
  file.write(message)
  file.write(" ")
  file.write(phone_number)
  file.write(';')
  file.close()  

def output_people():
   last_name = (input("Введите фамилию: "))  
   with open('C:\\Users\\Alena\\Desktop\\гикбрейнс\\python\\27.09\\book.txt') as file:
    
    all=file.read()
    humans = all.split(';')
    found=False
    for human in humans:
       elements=human.split(' ')
       if elements[0]==last_name:
          print(elements[3])
          found=True
    if found==False:
        print('фамилия не найдена')
def export():
    with open('C:\\Users\\Alena\\Desktop\\гикбрейнс\\python\\27.09\\book.txt') as file:
      all=file.read()
      humans = all.split(';')
      str=""
      for human in humans:
       elements=human.split(' ')
       
       str=str+';'.join(elements)+('\n')
      print(str)
      file_csv = open("C:\\Users\\Alena\\Desktop\\гикбрейнс\\python\\27.09\\книга2.csv", "w") 
      file_csv.write(str)
      file_csv.close()  




        

