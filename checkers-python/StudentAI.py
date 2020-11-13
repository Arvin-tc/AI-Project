import copy
from random import randint
from BoardClasses import Move
from BoardClasses import Board
#The following part should be completed by students.
#<<<<<<< HEAD
#Students can modify anything except the class name and exisiting functions and varibl


#class SCTS:
    #def __init__(self):

class Node():
    PassNumber = 0
    WinNumber = 0
    def __init__(self, move, color, parents = None):
        self.move = move
        self.children = []
        self.parent = parents
        self.color = color

    # add a calculate function to calculate the win rate
#=======
#Students can modify anything except the class name and exisiting functions and varibles.
#git_test
#>>>>>>> f0e13ba757e80af7111e18bf625a82efae6c1350

class StudentAI():
    def __init__(self,col,row,p):
        self.col = col
        self.row = row
        self.p = p
        self.board = Board(col,row,p)
        self.board.initialize_game()
        self.color = ''
        self.opponent = {1:2,2:1}
        self.color = 2
        self.simulate_timer = 100

    def get_move(self,move):
        if len(move) != 0:
            self.board.make_move(move, self.opponent[self.color])
        else:
            self.color = 1
        moves = self.board.get_all_possible_moves(self.color)
        # if there is a Jump move in the current board, do the Jump.
        if len(moves)==1:
            move = moves[0][0]
            self.board.make_move(move, self.color)
            return move
        # if there are no Jump moves in the current board, do the simulation.
        else:
            decided_move = self.RecursionMove(0, [])
            self.board.make_move(decided_move, self.color)
            return decided_move

    def RecursionMove(self, counter, ansList):
        if (counter == 400):
            ans = ansList[0]
            for node in ansList:
                if (node.WinNumber/node.PassNumber) > (ans.WinNumber/ans.PassNumber):
                    ans=node
            return ans.move
        else:
            SB = copy.deepcopy(self.board)
            Pmoves=SB.get_all_possible_moves(self.color)
            if len(ansList) != 0:
                for ans in ansList:
                    for i in range(0,len(Pmoves)):
                        if (Pmoves[i]==ans.move):
                            Pmoves.pop(i)
            if (len(Pmoves)!=0)or(len(ansList)<len(Pmoves)):
                randomMovex= randint(0, len(Pmoves)-1)
                randomMovey = randint(0, len(Pmoves[randomMovex]) - 1)
                new_Node= Node(Pmoves[randomMovex][randomMovey], self.color)
                ansList.append(new_Node)
                SB.make_move(Pmoves[randomMovex][randomMovey], self.color)
                turn_num = self.opponent[self.color]
                while(SB.is_win(turn_num)==0)&(len(SB.get_all_possible_moves(turn_num))!=0):
                    Rmoves=SB.get_all_possible_moves(turn_num)
                    RMovex = randint(0, len(Rmoves) - 1)
                    RMovey = randint(0, len(Rmoves[RMovex]) - 1)
                    SB.make_move(Rmoves[RMovex][RMovey], turn_num)
                    turn_num = self.opponent[turn_num]
                new_Node.PassNumber+=1
                if SB.is_win(turn_num) == self.color:
                    new_Node.WinNumber+=1
                return self.RecursionMove(counter+1, ansList)
            #if part seems working, but else part isn't
            #seems like something goes wrong with the check of ansList, tried to fix but doesn't help
            #Also, some kind of
            else:
                present_list = []
                for ans in ansList:
                    present_list.append(ans)
                present_node = None
                present_color = self.color
                mother_node = None
                while (len(present_list)!=0):
                    mother_node = present_node
                    present_node= present_list[randint(0, len(present_list)-1)]
                    present_list= present_node.children
                    SB.make_move(present_node.move, present_color)
                    present_color = self.opponent[present_color]
                #the node is found
                Prmoves = SB.get_all_possible_moves(present_color)
                PresentMovex = randint(0, len(Prmoves) - 1)
                PresentMovey = randint(0, len(Prmoves[PresentMovex]) - 1)
                new_Node = Node(Prmoves[PresentMovex][PresentMovey], present_color, mother_node)
                new_Node.parent.children.append(new_Node)
                SB.make_move(Prmoves[PresentMovex][PresentMovey], present_color)
                turn_num = self.opponent[present_color]
                while (SB.is_win(turn_num) == 0):
                    Rmoves = SB.get_all_possible_moves(turn_num)
                    RMovex = randint(0, len(Rmoves) - 1)
                    RMovey = randint(0, len(Rmoves[RMovex]) - 1)
                    SB.make_move(Rmoves[RMovex][RMovey], turn_num)
                    turn_num = self.opponent[turn_num]
                new_Node.PassNumber += 1
                while(new_Node.parent != None):
                    new_Node.parent.PassNumber += 1
                    new_Node = new_Node.parent
                if SB.is_win(turn_num) == self.color:
                    new_Node.WinNumber += 1
                    while (new_Node.parent!=None):
                        new_Node.parent.WinNumber+=1
                        new_Node=new_Node.parent
                return self.RecursionMove(counter + 1, ansList)










    '''
        if len(move) != 0
        self.board.make_move(move,self.opponent[self.color])
    else:
        self.color = 1
    index = randint(0,len(moves)-1)
    inner_index =  randint(0,len(moves[index])-1)
    move = moves[index][inner_index]
    self.board.make_move(move,self.color)
    return
    '''


