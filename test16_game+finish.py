def game_finished(board):
   count_1=0
   count_2=0
   N = []
   L =[]
   for line in board:
       count_1 += line.count(1)
       count_2 += line.count(2)
       if line.count(1)== 3:
           N.append(1)
       elif line.count(2)== 3:
           N.append(2)
       elif (line.count(1)+line.count(2)):
           L.append((line.count(1)+line.count(2)))
       else:
           N.append(-1)
   if sum(L)<=6:
       N.append(0)
   if 1 in N:
       return 1
   elif 2 in N:
       return 2
   elif 0 in N:
       return 0
   else:
       return -1

b = [[1, 0, 1], [2, 1, 0], [2, 1, 2]]

print(game_finished(b))
