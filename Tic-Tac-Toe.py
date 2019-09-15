board=['-','-','-','-','-','-','-','-','-']
turn=1

"""
1 - X's turn
-1 - O's turn
"""


def isBoardEmpty(board):
    if(len(board)==0):
        return 1


def isBoardFull(board):
    if '-' in board:
        return 0
    else:
        return 1


def who_won(board):
    if((board[0] == 'X' and board[1] == 'X' and board[2] == 'X') or (board[3] == 'X' and board[4] == 'X' and board[5] == 'X') or (board[6] == 'X' and board[7] == 'X' and board[8] == 'X') or (board[0] == 'X' and board[3] == 'X' and board[6] == 'X') or (board[1] == 'X' and board[4] == 'X' and board[7] == 'X') or (board[2] == 'X' and board[5] == 'X' and board[8] == 'X') or (board[0] == 'X' and board[4] == 'X' and board[8] == 'X') or (board[2] == 'X' and board[4] == 'X' and board[6] == 'X')):
        return 1
    elif((board[0] == 'O' and board[1] == 'O' and board[2] == 'O') or (board[3] == 'O' and board[4] == 'O' and board[5] == 'O') or (board[6] == 'O' and board[7] == 'O' and board[8] == 'O') or (board[0] == 'O' and board[3] == 'O' and board[6] == 'O') or (board[1] == 'O' and board[4] == 'O' and board[7] == 'O') or (board[2] == 'O' and board[5] == 'O' and board[8] == 'O') or (board[0] == 'O' and board[4] == 'O' and board[8] == 'O') or (board[2] == 'O' and board[4] == 'O' and board[6] == 'O')):
        return 2
    elif(isBoardFull(board)==1):
        return 3
    else:
        return 0

    
def render_board(a):
    print("0: {}  |1: {}  |2: {} ".format(a[0],a[1],a[2]))
    print("-------|-------|-----")
    print("3: {}  |4: {}  |5: {} ".format(a[3],a[4],a[5]))
    print("-------|-------|-----")
    print("6: {}  |7: {}  |8: {} ".format(a[6],a[7],a[8]))

def posavailable(board):
    posavail=[]
    for i in range(0,len(board)):
        if(board[i] == '-'):
            posavail.append(i)
    return posavail
"""
def ifXwins(state,pos):
    try:
        for x in pos:
            state[x]='X'
            if (who_won(state)==1):
                return x
            state[x]='-'
    except:
        state[pos]='X'
        if (who_won(state)==1):
            return x
        state[pos]='-'
    return None

def ifOwins(state,pos):
    try:
        for x in pos:
            state[x]='O'
            if (who_won(state)==2):
                return x
            state[x]='-'
    except:
        state[pos]='O'
        if (who_won(state)==2):
            return x
        state[pos]='-'
    return None

def ai_turn(board):
    avpos = posavailable(board)
    posscore = dict.fromkeys(avpos , 0)
    temp=ifOwins(board,avpos)
    if(temp!=None):
        return temp
    temp=ifXwins(board,avpos)
    if(temp!=None):
        return temp
    for key in posscore:
        board[int(key)]='O'
        if(who_won(board)==1):
            posscore[key]=posscore[key]-100
        elif(who_won(board)==2):
            posscore[key]=posscore[key]+100
        elif(who_won(board)==3):
            posscore[key]=posscore[key]+0
        else:
            temp=minmax(board,posscore[key],1)
            posscore[key]=posscore[key]+temp
        board[int(key)]='-'
    mmax,mkey=temp,avpos[0]
    print(posscore)
    for key in posscore:
        if posscore[key]>mmax:
            mmax=posscore[key]
            mkey=key
    return mkey
 
def minmax(board, score, tempturn):
    if(who_won(board)==1):
        return -100
    elif(who_won(board)==2):
        return 100
    elif(who_won(board)==3):
        return 0
    else:
        if(tempturn==1):
            avpos = posavailable(board)
            for key in avpos:
                board[int(key)]='X'
                score = score + minmax(board,score,-tempturn)
                board[int(key)]='-'
            return score
        elif(tempturn==-1):
            avpos = posavailable(board)
            for key in avpos:
                board[int(key)]='O'
                score = score + minmax(board,score,-tempturn)
                board[int(key)]='-'
            return score

"""
def ai_turn(board):
    tl=[]
    avpos = posavailable(board)
    posscore = dict.fromkeys(avpos , 0)
    """temp=ifOwins(board,avpos)
    if(temp!=None):
        return temp
    temp=ifXwins(board,avpos)
    if(temp!=None):
        return temp"""
    for key in posscore:
        board[int(key)]='O'
        temp=minmax(board,posscore[key],1)
        posscore[key]=posscore[key]+temp
        tl.append(temp)
        board[int(key)]='-'
    tl.sort()
    mmax,mkey=tl[0],avpos[0]
    print(posscore)
    for key in posscore:
        if posscore[key]>mmax:
            mmax=posscore[key]
            mkey=key
    return mkey

def minmax(board, score, tempturn):
    scorelist=[]
    if(who_won(board)==1):
        return -10
    elif(who_won(board)==2):
        return 10
    elif(who_won(board)==3):
        return 0
    else:
        if(tempturn==1):
            avpos = posavailable(board)
            for key in avpos:
                board[int(key)]='X'
                scorelist.append(score + minmax(board,score,-tempturn))
                board[int(key)]='-'
            scorelist.sort()
            return scorelist[0]
        elif(tempturn==-1):
            avpos = posavailable(board)
            for key in avpos:
                board[int(key)]='O'
                scorelist.append(score + minmax(board,score,-tempturn))
                board[int(key)]='-'
            scorelist.sort()
            return scorelist[len(scorelist)-1]

    
render_board(board)
while(isBoardFull(board)!=1):
    if(turn==1):
        print("X turn: ")
        ch = input("Choose the position: ")
        if ch not in posavailable(board):
            board[int(ch)]='X'
            turn=-1
        else:
            print("Invalid move")
            continue
    elif(turn==-1):
        print("O turn: ")
        ch = ai_turn(board)
        board[int(ch)]='O'
        turn=1
    render_board(board)
    if(who_won(board)==1):
        print("\n############  X WON!! ############\n")
        break
    elif(who_won(board)==2):
        print("\n############  O WON!! ############\n")
        break
    elif(who_won(board)==3):
        print("\n############  DRAW!! ############\n")
        break

    
