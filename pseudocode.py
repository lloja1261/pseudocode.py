position.zebrafish=(x1,y2,z3)
position.predator=(x2,y2,z2)

distance=(sqrt((x1-x2)^2+(y1-y2)^2+(z1-z2)^2))
distance.storage=[distance1, distance2,...]

def turn():
  equation.ellipse=("ellipse equation")
  if (distance)<=15:   //or other mmore specific number
    return position.zebrafish, position.predator
  find the equation of the line tangent to position.predator  //refer to internet
  find the equation from fish to fish using their positions //find slope and plug-in
  use abs((tan1-tanb)/(1+tanatab)) to find degree to turn   //only gives answers less than 90
  find perpendicular line to tangent   //use formula
    if position.zebrafish to the right:
      then more than 90 deg turn        // The stepper motors will help turn the fish
    else:                               // use the distance between the y components
      less than 90 deg turn
def oscillate():
  repeat 4 times: 
    move y axis 3cm left and right
    move z axis at the same time. 
def go back():
  turn same angle deg but opposite the one done the first time. ]
  follow the assigned path

def attack():
  turn()
  while(y1!=y2):
    move_dc encoder
    while(dc_encoder moving);
      move_servo(max distance)
      if(max_distance reached):
        break
  oscillate()
  go back()
print("Luis Loja")
