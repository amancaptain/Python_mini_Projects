# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 17:35:26 2018

@author: AMAN
"""

def magic_square(n):
    magicSquare=[]
    for i in range(n):
        l=[]
        for j in range(n):
            l.append(0)
        magicSquare.append(l)
        
        
    i=n//2
    j=n-1
    num=n*n
    count=1
    
    while(count<=num):
        if(i==-1 and j==n):
            i=0
            j=n-2
        else:
            if(i<0):
                i=n-1
            if(j==n):
                j=0
                
                
        if( magicSquare[i][j]!=0):
                i=i+1
                j=j-2
                continue
            
        else:
            magicSquare[i][j]=count
            count=count+1
            
        i=i-1
        j=j+1
      
            
    for i in range(n):
        for j in range(n):
            print(magicSquare[i][j],end=" ")
        print()
    print("The sum of each row/column/dialog is:"+ str((n*(n*n+1))/2))
    
magic_square(15)
    
    
            
            
     
        