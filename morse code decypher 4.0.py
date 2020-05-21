## dictionnaires
dict_letters={
    "A": "._",
    "B": "_...",
    "C": "_._.",
    "D": "_..",
    "E": ".",
    "F": ".._.",
    "G": "__.",
    "H": "....",
    "I": "..",
    "J": ".___",
    "K": "_._",
    "L": "._..",
    "M": "__",
    "N": "_.",
    "O": "___",
    "P": ".__.",
    "Q": "__._",
    "R": "._.",
    "S": "...",
    "T": "_",
    "U": ".._",
    "V": "..._",
    "W": ".__",
    "X": "_.._",
    "Y": "_.__",
    "Z": "__..",
    "1": ".____",
    "2": "..___",
    "3": "...__",
    "4": "...._",
    "5": ".....",
    "6": "_....",
    "7": "__...",
    "8": "___..",
    "9": "____.",
    "0": "_____",
    " ": " "
    }


dict_morse = {v: k for k, v in dict_letters.items()}

##debut du programme morse vers letters

sequence = input("what morse sequence do you want to decypher? \n")

length_sequence = len(sequence)

##essaye avec 6"_" : ______: le programme affiche TTTTTT soit 6"T", tres bien.
##mais si tu rentres 7"_______": le programme affiche TTTTTTM soit 6 caracteres differenciés mais pas TTTTTTT soit 7"T"


## ce code est aussi precis qu'il n'y a de boucle for ou plutot de --> s_" "<--. ici, 6. donc ce proramme peut dissocier 6 caracteres les uns des autres



    
    
for i in range(0, length_sequence):
    s_debut= slice(0,i+1)
    if sequence[s_debut] in dict_morse:
        for j in range(i+1,length_sequence):
            s_j= slice(i+1,j+1)
            if sequence[s_j] in dict_morse:
                for k in range(j+1,length_sequence):
                    s_k=slice(j+1,k+1)
                    if sequence[s_k] in dict_morse:
                        for l in range(k+1, length_sequence):
                            s_l=slice(k+1,l+1)
                            if sequence[s_j] in dict_morse:
                                for m in range(l+1, length_sequence):
                                    s_m=slice(l+1, m+1)
                                    # if sequence[s_m] in dict_morse:
                                    
                                    # bloc a rajouter ici en suivant la meme logique : for "n" puis section_"n" du for puis section_fin puis verifier s'ils existent avant d'imprimer
                                    s_fin=slice(m+1,length_sequence)
                                    if sequence[s_m] in dict_morse and sequence[s_fin] in dict_morse:
                                        print(dict_morse.get(sequence[s_debut],"")+dict_morse.get(sequence[s_j],"")+dict_morse.get(sequence[s_k],"")+dict_morse.get(sequence[s_l],"")+dict_morse.get(sequence[s_m],"")+dict_morse.get(sequence[s_fin],""))
                            s_fin=slice(l+1,length_sequence)
                            if sequence[s_l] in dict_morse and sequence[s_fin] in dict_morse:
                                print(dict_morse.get(sequence[s_debut],"")+dict_morse.get(sequence[s_j],"")+dict_morse.get(sequence[s_k],"")+dict_morse.get(sequence[s_l],"")+dict_morse.get(sequence[s_fin],"")) 
                    s_fin=slice(k+1,length_sequence)
                    if sequence[s_k] in dict_morse and sequence[s_fin] in dict_morse:
                        print(dict_morse.get(sequence[s_debut],"")+dict_morse.get(sequence[s_j],"")+dict_morse.get(sequence[s_k],"")+dict_morse.get(sequence[s_fin],""))   
            s_fin= slice(j+1, length_sequence)
            if sequence[s_j] in dict_morse and sequence[s_fin] in dict_morse:
                print(dict_morse.get(sequence[s_debut],"")+dict_morse.get(sequence[s_j],"")+dict_morse.get(sequence[s_fin],""))
    s_fin=slice(i+1, length_sequence)
    if sequence[s_debut] in dict_morse and sequence[s_fin] in dict_morse:
        print(dict_morse.get(sequence[s_debut],"")+dict_morse.get(sequence[s_fin],""))
       
s=slice(0,length_sequence)
if sequence[s] in dict_morse:
    print(dict_morse.get(sequence[s],""))