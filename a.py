travelbag = ["vattenflaska", "tröja", "shorts"]


while True:
    menyval = input("1. Kolla i resväskan\n"
                   "2. Lägg sak i resväskan\n"
                   "3. Ta bort sak i resväskan\n"
                   "4. Avsluta program\n")


    if menyval == "1":
    
       print(*travelbag, sep=", ")
       
    elif menyval == "2":
        läggtill = input("Vad vill du lägga till i väskan? ")
        travelbag.append(läggtill)
        print(*travelbag, sep=", ")


        
    elif menyval == "3":
        removee = input("Vad vill du ta bort från väskan? ")
        travelbag.remove(removee)
        print(*travelbag, sep=", ")
        
    elif menyval == "4":
       break
