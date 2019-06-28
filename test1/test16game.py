def validate_board(board):
   count_1=0
   count_2=0
   n = [0,1,2]
   N = []
   if len(board)!=3:
       return False
   for line in board:
       count_1 += line.count(1)
       count_2 += line.count(2)
       if len(line) != 3:
           N.append(0)
       #if (line.count(1)==line.count(2)) or (line.count(1) - line.count(2) == 1):
       #    N.append(1)
       #else:
       #    N.append(0)
       for x in line:
           if x in n:
               N.append(1)
           else:
               N.append(0)
   if 0 in N:
        return False
   else:
       return True




b = [[1, 2, 1], [0, 1, 2], [2, 2, 1, ]]
print(validate_board(b))

