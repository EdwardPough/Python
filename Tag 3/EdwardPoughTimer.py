import time

array = ["Frage 1","Frage 2","Frage 3","Frage 4","Frage 5","Frage 6","Frage 7","Frage 8","Frage 9","Frage 10",]
counter = 0
while counter != 10:
    x = array[counter]
    print(x)
    time.sleep(1)
    input("Bitte antworten Sie jetzt: ")
    counter = counter + 1
