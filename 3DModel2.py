from Tkinter import *
import math as m
import re

#--------- Declarations ----------
widthm = 3
widthw = 1000
fl = 300
steps = 50

deg = 180/m.pi #57,295
hv = widthw/2  #Fur optimierung
stepsRotate = 20/deg

def reload():
    canv.delete('all')
    for i in range(len(map)):
        try:
            canv.create_line(fl/(float(fl+map[i][0][2]))*map[i][0][0] + hv , fl/(float(fl+map[i][0][2]))*map[i][0][1] + hv,  fl/(float(fl+map[i][1][2]))*map[i][1][0] + hv, fl/(float(fl+map[i][1][2]))*map[i][1][1] + hv, fill="black",width=widthm)
        except():
            print("Fail")
# fl/(float(fl+map[i][0][2]))*map[i][0][0]+500

def left():
    for i in range(len(map)):
        map[i][0][0] -= steps
        map[i][1][0] -= steps
    reload()

def right():
    for i in range(len(map)):
        map[i][0][0] += steps
        map[i][1][0] += steps
    reload()

def up():
    for i in range(len(map)):
        map[i][0][1] -= steps
        map[i][1][1] -= steps
    reload()

def down():
    for i in range(len(map)):
        map[i][0][1] += steps
        map[i][1][1] += steps
    reload()

def near():
    for i in range(len(map)):
        map[i][0][2] -= steps
        map[i][1][2] -= steps
    reload()

def away():
    for i in range(len(map)):
        map[i][0][2] += steps
        map[i][1][2] += steps
    reload()

def rotateR():
    for i in range(len(map)):
        for j in range(2):
            map[i][j][0] = float(map[i][j][0]*m.cos(stepsRotate)) - float(map[i][j][2]*m.sin(stepsRotate))
            map[i][j][2] = float(map[i][j][2]*m.cos(stepsRotate)) + float(map[i][j][0]*m.sin(stepsRotate))
    reload()

def rotateDown():
    for i in range(len(map)):
        for j in range(2):
            map[i][j][0] = map[i][j][0]*m.cos(stepsRotate) - map[i][j][1]*m.sin(stepsRotate)
            map[i][j][1] = map[i][j][1]*m.cos(stepsRotate) + map[i][j][0]*m.sin(stepsRotate)
    reload()

def reset():
    map = pyramid
    reload()

#---------- Create ---------------
root = Tk()
root.title("3D Model 1.2")
root.geometry("1000x1030")

left  = Button(root,text="<--",command=left).grid(row=1,column=0)
rl    = Button(root,text="   ",command=reset).grid(row=1,column=1)
right = Button(root,text="-->",command=right).grid(row=1,column=2)
up = Button(root,text="UP",command=up).grid(row=0,column=1)
down = Button(root,text="DN",command=down).grid(row=2,column=1)

near = Button(root,text="near",command=near).grid(row=0,column=4)
pl = Button(root,text="   ",).grid(row=1,column=4)
away = Button(root,text="away",command=away).grid(row=2,column=4)
rr = Button(root,text="rr",command=rotateR).grid(row=1,column=3)
rd = Button(root,text="rd",command=rotateDown).grid(row=1,column=5)

canv = Canvas(root, width=widthw, height=widthw, bg="gray25")

#----------- Map / Lines ---------
square = [[[-200,-200,0],[-200,-200,300]],
       [[-200, 200,0],[-200, 200,300]],
       [[ 200,-200,0],[ 200,-200,300]],
       [[ 200, 200,0],[ 200, 200,300]],

       [[-200, 200,0],[ 200, 200,0]],
       [[ 200, 200,0],[ 200,-200,0]],
       [[ 200,-200,0],[-200,-200,0]],
       [[-200,-200,0],[-200, 200,0]],

       [[-200, 200,300],[ 200, 200,300]],
       [[ 200, 200,300],[ 200,-200,300]],
       [[ 200,-200,300],[-200,-200,300]],
       [[-200,-200,300],[-200, 200,300]],
      ]

pyramid = [[[-150,-100,50 ] , [150,-100,350]],
           [[150,-100,350 ],  [150,-100,50]],
           [[150,-100,50  ],  [-150,-100,50]],
           [[-150,-100,350],  [-150,-100,350]],

           [[-150,-100,50], [0,-300,200]],
           [[-150,-100,350],[0,-300,200]],
           [[150,-100,50],  [0,-300,200]],
           [[150,-100,350], [0,-300,200]],
          ]
map = square
reset()

#------------ Rest -----------




#------------ End ------------
reload()
canv.grid(row=3,column=0,columnspan=7)
root.mainloop()
