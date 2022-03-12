bcount=0
s=int(input("Enter the size of your NxN matrix: "))
game=[]
global k
k=int(s//2)
global b
b=0
win=[['W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', ' ', ' ', ' ', ' ', ' ', 'W'], ['W', ' ', ' ', ' ', ' ', ' ', 'W'], ['W', ' ', ' ', '1', '1', ' ', 'W']]

def array(x):
    
    for i in range(x):
     game.append([])
     if i==0: 
         abc=game[0]
         for h in range(x):
              abc.append("W")  
     elif i==(x-1):

         lastrow=game[x-1]    
         lastrow.append("W")
         for i in range(x-2):
             lastrow.append("G")
         lastrow.append("W")
         game[x-1][k]="o"
     else:
         asd=game[i]
         asd.append("W")
         for i in range(x-2):
             asd.append(" ")
         asd.append("W")


array(s)


def brick(inpstr):
    splstr=inpstr.split( )
    n=int(splstr[0])
    m=int(splstr[1])
    w=splstr[2]
    game[n][m]=w



def destroy(d):
    global k
    if d=="LD":
        if game[s-1][k-1]=='_':
          game[s-1][k]="_"
          k=k-1
          game[s-1][k]="o"
        else:
          game[s-1][k]="G" 
          k=k-1
          game[s-1][k]="o"
    elif d=="RD":
        if game[s-1][k+1]=='_':
          game[s-1][k]="_"
          k=k+1
          game[s-1][k]="o"
        else:
          game[s-1][k]="G"
          k=k+1
          game[s-1][k]="o"

        
    else:
        print("ST")

    for x in range(s-2,0,-1):
            if game[x][k]!=" ":
                    if game[x][k]=="1":
                         game[x][k]=" "
                         break
                    elif game[x][k]=="B":
                        game[x][k]=" "
                        global b
                        if b==0:
                          game[s-1][k+1]="_"
                          b=b+1
                        else:
                          game[s-1][k-1]="_"

                    elif game[x][k]=="DE":
                         for i in range(1,s-1):
                             game[x][i]=" "   
                    elif game[x][k]=="DS":
                             if k==1:
                                 game[x][k]=" "
                                 game[x][k+1]=" "
                                 game[x-1][k+1]=" "
                                 game[x-1][k]=" "
                                 game[x+1][k+1]=" "
                                 break
                             elif mid==(s-2):
                                 game[x][k]=" "
                                 game[x][k-1]=" "
                                 game[x-1][k-1]=" "
                                 game[x-1][k]=" "
                                 game[x+1][k-1]=" " 
                                 break
                             else:
                                 game[x][k]=" "
                                 game[x][k-1]=" "
                                 game[x][k+1]=" "
                                 game[x-1][k-1]=" "
                                 game[x-1][k]=" "
                                 game[x-1][k+1]=" "
                                 game[x+1][k-1]=" "
                                 game[x+1][k+1]=" "    
                                 break      
                    else:
                         game[x][k]=str(int(game[x][k])-1)
                         break   



def printmat():
    for i in range(0,s):
         row=""
         for j in range(0,s):
             c=str(game[i][j])
             row=row+c
         print(row)    



while True:

    if input('Do you want to add bricks? Y/N :  ') == 'n':
        printmat()
        break
    else:
         position=input("Enter the brick's position and the brick type : ")
         brick(position)


ballcount=input("Enter ball count :  ")
ballcount=int(ballcount)


while True:

    if input('Do you want to traverse the ball ? Y/N :  ')=='n':
        printmat()
        del game[s-1]
        if game==win:
             print("HURRAY YOU WON !!")
        break
    else:
         balldir=input("Enter the direction in which the ball need to traverse : ")    
         destroy(balldir) 
         printmat()
         print("The ballcount is ",ballcount)
         

