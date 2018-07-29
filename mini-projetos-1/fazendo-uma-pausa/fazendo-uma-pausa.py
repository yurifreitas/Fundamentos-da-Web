import webbrowser
import time

paradas = int(input("Digite o numero de de intervalos de 15 min para seu foco? "))
contador = 0

while(contador < paradas) :
    time.sleep(15*60)
    print ("É hora de fazer uma pausa de 5 min")
    webbrowser.open("https://www.youtube.com/watch?v=uUHHdNa81NM")
    time.sleep(5*60)
    print ("É hora de voltar ao trabalho")
    time.sleep(10)
    contador =contador + 1
