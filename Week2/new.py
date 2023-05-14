import numpy as np

frontier = PriorityQueue()
visited = dict()

game = np.array(
  [[-1,-1,1,1,1,-1,-1],
   [-1,-1,1,1,1,-1,-1],
   [ 1, 1,1,1,1, 1, 1],
   [ 1, 1,1,0,1, 1, 1],
   [ 1, 1,1,1,1, 1, 1],
   [-1,-1,1,1,1,-1,-1],
   [-1,-1,1,1,1,-1,-1],
   
   ]
)
goal = np.array(
  [
   [-1,-1,0,0,0,-1,-1],
   [-1,-1,0,0,0,-1,-1],
   [ 0, 0,0,0,0, 0, 0],
   [ 0, 0,0,1,0, 0, 0],
   [ 0, 0,0,0,0, 0, 0],
   [-1,-1,0,0,0,-1,-1],
   [-1,-1,0,0,0,-1,-1],
    
  ]
)
#f(x) = g(x) + h(x)
frontier.push(Node(state = game, g=0, h=0))
while len(frontier)!=0:
  current_game = frontier.pop()

# class MarbleSolitaire:
#   # heuristic
#     def get_estimate():
        