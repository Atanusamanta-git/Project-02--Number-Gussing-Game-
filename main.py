# This is The it's Work like Computer Guess a number And You guess computer numer jodi tumi computer ki number likhche seta guess koro tahole tumi jite jabe 
#but je joto kom attend a guess korte parbe se winner hobe

import random
n=random.randint(1, 100)
a=-1
guess=1
while(a != n): #mane a!=n jotokhon thakbe toto khon loop cholbe ar jokhon a = n hobe loop close hoia jabe
    
    a=int(input("Enter The Number 1 - 100: "))
    if (a>n):
        print("Enter Lower Number")
        
    elif(a<n):
        print("Enter Upper Number")
    guess =guess+1
    

print(f"you Guess the Number Correctly in {n} for {guess} Attampt")