#Libraries
import random




#Functions
def Encrypte():
    sentence = input("Enter your text: ")
    words = sentence.split()
    new_words = []
    
    for word in words:

        #Generate key
        ordered_list=[]
        for i in range(len(word)):
            ordered_list.append(i)
            random.shuffle(ordered_list)
            key = ordered_list
        

        shuffeled_word = []
        i=0

        #Generate encrypted word 
        for j in range(0,len(word)):
            shuffeled_word.append(word[key[j]])
            i += 1
        #print(Encrypted_word)
        
        Encrypted_word = []
        asc_code = 0
        for i in range(0,len(shuffeled_word)):
            asc_code = 122 - ord(shuffeled_word[i])
            Encrypted_word.append(asc_code)
            
        print(Encrypted_word)

        l = []
        for i in range(0, len(Encrypted_word)):
            l += str(chr(Encrypted_word[i]))
        print(l)
            


        
    


#Main
mode = input("Encrypte or Decrypt \t")

if mode == "1":
    Encrypte()