while True:
 print("Умножим да поделим.Предлагаю вам написать всего лишь число")
 N= int(input())
 Answer =(N*(N+1))/2
 print(Answer)
 repeat=input("Еще раз ?")
 if repeat.strip().lower() =='нет':
     break

