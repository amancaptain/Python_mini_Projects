# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 03:53:38 2018

@author: AMAN
"""

import random
movies=['anand','drishyam','ambe shivam','gol maal','tare jammen par','avengers','expandable','dharam veer','lagan','dilwale dulhaniya le jayenge']

def create_question(movie):
    n=len(movie)
    letters==list(movie)
    temp=[]
    for i in range(n):
        if(letters[i]==' '):
            temp.append(" ")
        else:
            temp.append("*")
            
    qn=' '.join(str(x) for x in temp)
    return qn


def is_present(movie,letter):
    c=movie.count(letter)
    if(c==0):
        return false
    else:
        return trure
    
    
def unlock(qn,movie,letter):
    ref=list(movie)
    qn_list=list(qn)
    temp=[]
    n=len(movie)
    for i in range(n):
        if(ref[i]==" " or ref[i]==letter):
            temp.append(ref[i])
        else:
            if(qn_list=='*'):
                temp.append('*')
            else:
                temp.append(ref[i])
                
    qn_new=' '.join(str(x) for x in temp)
    
    return qn_new



def play():
    p1name=input("Player 1 enter your name")
    p2name=input("Player 2 enter your name")
    pp1=0
    pp2=0
    turn=0
    willing=true
    while willing:
        
        if(turn%2==0):
             print(p1name,"Your turn")
             picked_movie=random.choice(movie)
             qn=create_question(picked_movie)
             print(qn)
              
             modified_qn=qn
             not_said=true
             while not_said:
                 letter=input("Your letter")
                 if(is_present(movie,letter),picked_movie):
                     modified_qn=unlock(modified_qn,picked_movie,letter)
                     print(modified_qn)
                     d=input("Press 1 to guess the movie or 2 to  unlock another letter")
                     if(d==1):
                         ans=input("Your answer")
                         if(ans==picked_movie):
                             pp1=pp1+1
                             print("Correct")
                             not_said=False
                             
                             print(p1name,"Your score :",pp1)
                             
                         else:
                             print("Wrong answer try again")
                 else:
                     print(letter,"not found")
                     
             c=int(input("Press 1 to continue or 0 to quit")
             if(c==0):
                  print(p1name,"Your score:",pp1)
                  print(p2name,"Your score:",pp2)
                  print("have a nice day")
                  print("Thanks for playing")
                  willing=False
                
                
        else:
             print(p1name,"Your turn")
             picked_movie=random.choice(movie)
             qn=create_question(picked_movie)
             print(qn)
              
             modified_qn=qn
             not_said=true
             while not_said:
                 letter=input("Your letter")
                 if(is_present(movie,letter),picked_movie):
                     modified_qn=unlock(modified_qn,picked_movie,letter)
                     print(modified_qn)
                     d=input("Press 1 to guess the movie or 2 to  unlock another letter")
                     if(d==1):
                         ans=input("Your answer")
                         if(ans==picked_movie):
                             pp1=pp1+1
                             print("Correct")
                             not_said=False
                             
                             print(p1name,"Your score :",pp1)
                             
                         else:
                             print("Wrong answer try again")
                 else:
                     print(letter,"not found")
                     
             c=int(input("Press 1 to continue or 0 to quit")
             if(c==0):
                 print(p1name,"Your score:",pp1)
                 print(p2name,"Your score:",pp2)
                 print("have a nice day")
                 print("Thanks for playing")
                 willing=False
                
        turn=turn+1
        
play()
                             
                            
                             
                         
                     
                                    
                
                
                
                
                
                
                
                
                
                