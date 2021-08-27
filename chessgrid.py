from tkinter import *
import random
import time
import math
from tkinter import messagebox

grid = ['a1', 'a2', 'b1', 'b2']


class chess:
    def __init__(self, window):
        window.geometry('440x440'); window.title('Chess Grid'); window.resizable(0,0); window.configure(background='#CBC3E3')
        a1 = Button(window, background='black',  text = '',  width = 2, font = ('Times', 10),command=self.a1)
        a2 = Button(window, background='white',  text = '',  width = 2, font = ('Times', 10),command=self.a2)
        a3 = Button(window, background='black',  text = '',  width = 2, font = ('Times', 10),command=self.a3)
        a4 = Button(window, background='white',  text = '',  width = 2, font = ('Times', 10),command=self.a4)
        a5 = Button(window, background='black',  text = '',  width = 2, font = ('Times', 10),command=self.a5)
        a6 = Button(window, background='white',  text = '',  width = 2, font = ('Times', 10),command=self.a6)
        a7 = Button(window, background='black',  text = '',  width = 2, font = ('Times', 10),command=self.a7)
        a8 = Button(window, background='white',  text = '',  width = 2, font = ('Times', 10),command=self.a8)

        b1 = Button(window, background='white',  text = '',  width = 2, font = ('Times', 10),command=self.b1)
        b2 = Button(window, background='black',  text = '',  width = 2, font = ('Times', 10),command=self.b2)
        b3 = Button(window, background='white',  text = '',  width = 2, font = ('Times', 10),command=self.b3)
        b4 = Button(window, background='black',  text = '',  width = 2, font = ('Times', 10),command=self.b4)
        b5 = Button(window, background='white',  text = '',  width = 2, font = ('Times', 10),command=self.b5)
        b6 = Button(window, background='black',  text = '',  width = 2, font = ('Times', 10),command=self.b6)
        b7 = Button(window, background='white',  text = '',  width = 2, font = ('Times', 10),command=self.b7)
        b8 = Button(window, background='black',  text = '',  width = 2, font = ('Times', 10),command=self.b8)

        c1 = Button(window, background='black',  text = '',  width = 2, font = ('Times', 10),command=self.c1)
        c2 = Button(window, background='white',  text = '',  width = 2, font = ('Times', 10),command=self.c2)
        c3 = Button(window, background='black',  text = '',  width = 2, font = ('Times', 10),command=self.c3)
        c4 = Button(window, background='white',  text = '',  width = 2, font = ('Times', 10),command=self.c4)
        c5 = Button(window, background='black',  text = '',  width = 2, font = ('Times', 10),command=self.c5)
        c6 = Button(window, background='white',  text = '',  width = 2, font = ('Times', 10),command=self.c6)
        c7 = Button(window, background='black',  text = '',  width = 2, font = ('Times', 10),command=self.c7)
        c8 = Button(window, background='white',  text = '',  width = 2, font = ('Times', 10),command=self.c8)

        d1 = Button(window, background='white',  text = '',  width = 2, font = ('Times', 10),command=self.d1)
        d2 = Button(window, background='black',  text = '',  width = 2, font = ('Times', 10),command=self.d2)
        d3 = Button(window, background='white',  text = '',  width = 2, font = ('Times', 10),command=self.d3)
        d4 = Button(window, background='black',  text = '',  width = 2, font = ('Times', 10),command=self.d4)
        d5 = Button(window, background='white',  text = '',  width = 2, font = ('Times', 10),command=self.d5)
        d6 = Button(window, background='black',  text = '',  width = 2, font = ('Times', 10),command=self.d6)
        d7 = Button(window, background='white',  text = '',  width = 2, font = ('Times', 10),command=self.d7)
        d8 = Button(window, background='black',  text = '',  width = 2, font = ('Times', 10),command=self.d8)

        e1 = Button(window, background='black',  text = '',  width = 2, font = ('Times', 10),command=self.e1)
        e2 = Button(window, background='white',  text = '',  width = 2, font = ('Times', 10),command=self.e2)
        e3 = Button(window, background='black',  text = '',  width = 2, font = ('Times', 10),command=self.e3)
        e4 = Button(window, background='white',  text = '',  width = 2, font = ('Times', 10),command=self.e4)
        e5 = Button(window, background='black',  text = '',  width = 2, font = ('Times', 10),command=self.e5)
        e6 = Button(window, background='white',  text = '',  width = 2, font = ('Times', 10),command=self.e6)
        e7 = Button(window, background='black',  text = '',  width = 2, font = ('Times', 10),command=self.e7)
        e8 = Button(window, background='white',  text = '',  width = 2, font = ('Times', 10),command=self.e8)

        f1 = Button(window, background='white',  text = '',  width = 2, font = ('Times', 10),command=self.f1)
        f2 = Button(window, background='black',  text = '',  width = 2, font = ('Times', 10),command=self.f2)
        f3 = Button(window, background='white',  text = '',  width = 2, font = ('Times', 10),command=self.f3)
        f4 = Button(window, background='black',  text = '',  width = 2, font = ('Times', 10),command=self.f4)
        f5 = Button(window, background='white',  text = '',  width = 2, font = ('Times', 10),command=self.f5)
        f6 = Button(window, background='black',  text = '',  width = 2, font = ('Times', 10),command=self.f6)
        f7 = Button(window, background='white',  text = '',  width = 2, font = ('Times', 10),command=self.f7)
        f8 = Button(window, background='black',  text = '',  width = 2, font = ('Times', 10),command=self.f8)

        g1 = Button(window, background='black',  text = '',  width = 2, font = ('Times', 10),command=self.g1)
        g2 = Button(window, background='white',  text = '',  width = 2, font = ('Times', 10),command=self.g2)
        g3 = Button(window, background='black',  text = '',  width = 2, font = ('Times', 10),command=self.g3)
        g4 = Button(window, background='white',  text = '',  width = 2, font = ('Times', 10),command=self.g4)
        g5 = Button(window, background='black',  text = '',  width = 2, font = ('Times', 10),command=self.g5)
        g6 = Button(window, background='white',  text = '',  width = 2, font = ('Times', 10),command=self.g6)
        g7 = Button(window, background='black',  text = '',  width = 2, font = ('Times', 10),command=self.g7)
        g8 = Button(window, background='white',  text = '',  width = 2, font = ('Times', 10),command=self.g8)

        h1 = Button(window, background='white',  text = '',  width = 2, font = ('Times', 10),command=self.h1)
        h2 = Button(window, background='black',  text = '',  width = 2, font = ('Times', 10),command=self.h2)
        h3 = Button(window, background='white',  text = '',  width = 2, font = ('Times', 10),command=self.h3)
        h4 = Button(window, background='black',  text = '',  width = 2, font = ('Times', 10),command=self.h4)
        h5 = Button(window, background='white',  text = '',  width = 2, font = ('Times', 10),command=self.h5)
        h6 = Button(window, background='black',  text = '',  width = 2, font = ('Times', 10),command=self.h6)
        h7 = Button(window, background='white',  text = '',  width = 2, font = ('Times', 10),command=self.h7)
        h8 = Button(window, background='black',  text = '',  width = 2, font = ('Times', 10),command=self.h8)


        submit = Button(window, background='white',  text = 'Prompt',  width = 10, font = ('Times', 10),command = self.submit)

        timer = Button(window, background='white',  text = 'Timer',  width = 10, font = ('Times', 10),command = self.timer)
        timer.place(x=50,y=360)


        self.cont = True
        self.score = 0
        self.total = 0
        self.timer0 = False
        self.grid = ['a1','a2','a3','a4','a5','a6','a7','a8','b1','b2','b3','b4','b5','b6','b7','b8','c1','c2','c3','c4','c5','c6','c7','c8','d1','d2','d3','d4','d5','d6','d7','d8',
        'e1','e2','e3','e4','e5','e6','e7','e8','f1','f2','f3','f4','f5','f6','f7','f8','g1','g2','g3','g4','g5','g6','g7','g8']

        self.grid_prompt = ''

        score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
        score.place(x=140,y=360)

        reset = Button(window, background='white',  text = 'Reset',  width = 10, font = ('Times', 10),command=self.reset)  
        reset.place(x=260,y=50)     


        a1.place(x=100,y=310);a2.place(x=100,y=280);a3.place(x=100,y=250);a4.place(x=100,y=220);a5.place(x=100,y=190);a6.place(x=100,y=160);a7.place(x=100,y=130);a8.place(x=100,y=100)
        b1.place(x=130,y=310);b2.place(x=130,y=280);b3.place(x=130,y=250);b4.place(x=130,y=220);b5.place(x=130,y=190);b6.place(x=130,y=160);b7.place(x=130,y=130);b8.place(x=130,y=100)
        c1.place(x=160,y=310);c2.place(x=160,y=280);c3.place(x=160,y=250);c4.place(x=160,y=220);c5.place(x=160,y=190);c6.place(x=160,y=160);c7.place(x=160,y=130);c8.place(x=160,y=100)
        d1.place(x=190,y=310);d2.place(x=190,y=280);d3.place(x=190,y=250);d4.place(x=190,y=220);d5.place(x=190,y=190);d6.place(x=190,y=160);d7.place(x=190,y=130);d8.place(x=190,y=100)
        e1.place(x=220,y=310);e2.place(x=220,y=280);e3.place(x=220,y=250);e4.place(x=220,y=220);e5.place(x=220,y=190);e6.place(x=220,y=160);e7.place(x=220,y=130);e8.place(x=220,y=100)
        f1.place(x=250,y=310);f2.place(x=250,y=280);f3.place(x=250,y=250);f4.place(x=250,y=220);f5.place(x=250,y=190);f6.place(x=250,y=160);f7.place(x=250,y=130);f8.place(x=250,y=100)
        g1.place(x=280,y=310);g2.place(x=280,y=280);g3.place(x=280,y=250);g4.place(x=280,y=220);g5.place(x=280,y=190);g6.place(x=280,y=160);g7.place(x=280,y=130);g8.place(x=280,y=100)
        h1.place(x=310,y=310);h2.place(x=310,y=280);h3.place(x=310,y=250);h4.place(x=310,y=220);h5.place(x=310,y=190);h6.place(x=310,y=160);h7.place(x=310,y=130);h8.place(x=310,y=100)
        submit.place(x=100,y=50)

    def timer(self):
        self.timer0 = False
        second=StringVar()
        second.set("30")
        secondtime= Label(root, background='#CBC3E3',width=5, font=("Times",18,""),
                        textvariable=second)
        secondtime.place(x=65,y=390)
        temp = 30   
        while temp >= 0:
            if not self.timer0:
                mins,secs = divmod(temp,60)
                second.set("{0:2}".format(secs))
                root.update()
                time.sleep(.25)
                temp -= .25
                if temp == 0:
                    messagebox.showinfo("Times Up!", "You got " + str(self.score) + ' out of ' + str(self.total) +' correct!')
                    self.cont = False
            elif self.timer0:
                temp=-1
                zero= Label(root, background='#CBC3E3',width=5, font=("Times",18,""), text=(''))
                zero.place(x=65,y=390)


    
    def submit(self):
            if self.cont:
                def rand(grid):
                    return str(random.choice(self.grid))
                gridprompt = rand(grid)
                prompt = Label(root, background='#CBC3E3',  text = gridprompt,  width = 5, font = ('Times', 20))
                prompt.place(x=180,y=40)
                self.grid_prompt = str(gridprompt)

    def reset(self):
        self.timer0 = True
        self.score = 0
        self.total = 0
        self.cont = True
        score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
        score.place(x=140,y=360)
        prompt = Label(root, background='#CBC3E3',  text = '',  width = 5, font = ('Times', 20))
        prompt.place(x=180,y=40)
        self.grid_prompt = ''


    def a1(self):
        if self.cont:
            if self.grid_prompt == 'a1':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)

    def a2(self):
        if self.cont:
            if self.grid_prompt == 'a2':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)

    def a3(self):
        if self.cont:
            if self.grid_prompt == 'a3':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)

    def a4(self):
        if self.cont:
            if self.grid_prompt == 'a4':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)

    def a5(self):
        if self.cont:
            if self.grid_prompt == 'a5':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)

    def a6(self):
        if self.cont:
            if self.grid_prompt == 'a6':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)

    def a7(self):
        if self.cont:
            if self.grid_prompt == 'a7':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)

    def a8(self):
        if self.cont:
            if self.grid_prompt == 'a8':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)

    def b1(self):
        if self.cont:
            if self.grid_prompt == 'b1':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)

    def b2(self):
        if self.cont:
            if self.grid_prompt == 'b2':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)

    def b3(self):
        if self.cont:
            if self.grid_prompt == 'b3':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)

    def b4(self):
        if self.cont:
            if self.grid_prompt == 'b4':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)

    def b5(self):
        if self.cont:
            if self.grid_prompt == 'b5':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)

    def b6(self):
        if self.cont:
            if self.grid_prompt == 'b6':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)

    def b7(self):
        if self.cont:
            if self.grid_prompt == 'b7':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)

    def b8(self):
        if self.cont:
            if self.grid_prompt == 'b8':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)

    def c1(self):
        if self.cont:
            if self.grid_prompt == 'c1':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)    

    def c2(self):
        if self.cont:
            if self.grid_prompt == 'c2':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)    

    def c3(self):
        if self.cont:
            if self.grid_prompt == 'c3':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)    

    def c4(self):
        if self.cont:
            if self.grid_prompt == 'c4':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)    

    def c5(self):
        if self.cont:
            if self.grid_prompt == 'c5':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)    

    def c6(self):
        if self.cont:
            if self.grid_prompt == 'c6':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)    

    def c7(self):
        if self.cont:
            if self.grid_prompt == 'c7':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)    

    def c8(self):
        if self.cont:
            if self.grid_prompt == 'c8':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)            

    def d1(self):
        if self.cont:
            if self.grid_prompt == 'd1':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)       

    def d2(self):
        if self.cont:
            if self.grid_prompt == 'd2':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)       

    def d3(self):
        if self.cont:
            if self.grid_prompt == 'd3':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)  

    def d4(self):
        if self.cont:
            if self.grid_prompt == 'd4':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)  

    def d5(self):
        if self.cont:
            if self.grid_prompt == 'd5':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)  

    def d6(self):
        if self.cont:
            if self.grid_prompt == 'd6':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)  

    def d7(self):
        if self.cont:
            if self.grid_prompt == 'd7':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)  

    def d8(self):
        if self.cont:
            if self.grid_prompt == 'd8':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)  

    def e1(self):
        if self.cont:
            if self.grid_prompt == 'e1':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)

    def e2(self):
        if self.cont:
            if self.grid_prompt == 'e2':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)

    def e3(self):
        if self.cont:
            if self.grid_prompt == 'e3':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)

    def e4(self):
        if self.cont:
            if self.grid_prompt == 'e4':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)

    def e5(self):
        if self.cont:
            if self.grid_prompt == 'e5':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)

    def e6(self):
        if self.cont:
            if self.grid_prompt == 'e6':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)

    def e7(self):
        if self.cont:
            if self.grid_prompt == 'e7':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)

    def e8(self):
        if self.cont:
            if self.grid_prompt == 'e8':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)

    def f1(self):
        if self.cont:
            if self.grid_prompt == 'f1':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)

    def f2(self):
        if self.cont:
            if self.grid_prompt == 'f2':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)

    def f3(self):
        if self.cont:
            if self.grid_prompt == 'f3':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)

    def f4(self):
        if self.cont:
            if self.grid_prompt == 'f4':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)

    def f5(self):
        if self.cont:
            if self.grid_prompt == 'f5':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)

    def f6(self):
        if self.cont:
            if self.grid_prompt == 'f6':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)

    def f7(self):
        if self.cont:
            if self.grid_prompt == 'f7':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)

    def f8(self):
        if self.cont:
            if self.grid_prompt == 'f8':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)

    def g1(self):
        if self.cont:
            if self.grid_prompt == 'g1':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)

    def g2(self):
        if self.cont:
            if self.grid_prompt == 'g2':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)

    def g3(self):
        if self.cont:
            if self.grid_prompt == 'g3':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)

    def g4(self):
        if self.cont:
            if self.grid_prompt == 'g4':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)

    def g5(self):
        if self.cont:
            if self.grid_prompt == 'g5':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)

    def g6(self):
        if self.cont:
            if self.grid_prompt == 'g6':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)

    def g7(self):
        if self.cont:
            if self.grid_prompt == 'g7':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)

    def g8(self):
        if self.cont:
            if self.grid_prompt == 'g8':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)

    def h1(self):
        if self.cont:
            if self.grid_prompt == 'h1':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)

    def h2(self):
        if self.cont:
            if self.grid_prompt == 'h2':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)

    def h3(self):
        if self.cont:
            if self.grid_prompt == 'h3':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)

    def h4(self):
        if self.cont:
            if self.grid_prompt == 'h4':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)

    def h5(self):
        if self.cont:
            if self.grid_prompt == 'h5':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)

    def h6(self):
        if self.cont:
            if self.grid_prompt == 'h6':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)

    def h7(self):
        if self.cont:
            if self.grid_prompt == 'h7':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)

    def h8(self):
        if self.cont:
            if self.grid_prompt == 'h8':
                self.score += 1
            self.total += 1
            score = Label(root, background = '#CBC3E3', font = ('Times', 20), width = 10, text= str(self.score)+'/'+str(self.total))
            score.place(x=140,y=360)

root = Tk()
app = chess(root)
root.mainloop()