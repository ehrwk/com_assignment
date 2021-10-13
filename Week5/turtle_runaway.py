import turtle, random, time

score = 0

class RunawayGame:
    def __init__(self, canvas, runner, reset, chaser, catch_radius=50, init_dist=400):
        self.canvas = canvas
        self.runner = runner
        self.reset = reset
        self.chaser = chaser
        self.catch_radius2 = catch_radius**2
       
        
        self.runner.shape('turtle')
        self.runner.color('blue')
        self.runner.penup()
        self.runner.setx(-init_dist / 2)
        
        self.reset.shape('turtle')
        self.reset.color('green')
        self.reset.penup()
        self.reset.setx(-init_dist / 2)
        
                
        self.chaser.shape('turtle')
        self.chaser.color('red')
        self.chaser.penup()
        self.chaser.setx(+init_dist / 2)
        self.chaser.setheading(180)
        
        
        self.drawer = turtle.RawTurtle(canvas)
        self.drawer.hideturtle()
        self.drawer.penup()

    def is_catch_blue(self):
        p = self.runner.pos()
        q = self.chaser.pos()
        dx, dy = p[0] - q[0], p[1] - q[1]
        return dx**2 + dy**2 < self.catch_radius2
    
    def is_catch_green(self):
        p = self.reset.pos()
        q = self.chaser.pos()
        dx, dy = p[0] - q[0], p[1] - q[1]
        return dx**2 + dy**2 < self.catch_radius2

    def start(self, ai_timer_msec=100):
        self.ai_timer_msec = ai_timer_msec
        
        self.start_time = time.time()
        self.canvas.ontimer(self.step, self.ai_timer_msec)
          

    def step(self):
        self.runner.run_ai(self.chaser)
        self.chaser.run_ai(self.runner)
        global score
           
        is_catched = self.is_catch_blue()
        is_catched1 = self.is_catch_green()
        
        if(is_catched > 0):
            score += 1
            
        if(is_catched1 > 0):
            self.chaser.setpos(100, 100)
            
                
        self.drawer.undo()
        self.drawer.penup()
        self.drawer.setpos(-300, 300)
        elapse = time.time() - self.start_time
        self.drawer.write(f'Is catched blue? {is_catched} / Is catched green? {is_catched1} / Elapse: {elapse:.0f} / Score: {score}')
        
        self.canvas.ontimer(self.step, self.ai_timer_msec)
                    

class ManualMover(turtle.RawTurtle):
    def __init__(self, canvas, step_move=10, step_turn=10):
        super().__init__(canvas)
        self.step_move = step_move
        self.step_turn = step_turn

        canvas.onkeypress(lambda: self.forward(self.step_move), 'Up')
        canvas.onkeypress(lambda: self.backward(self.step_move), 'Down')
        canvas.onkeypress(lambda: self.left(self.step_turn), 'Left')
        canvas.onkeypress(lambda: self.right(self.step_turn), 'Right')
        canvas.listen()

    def run_ai(self, opponent):
        pass

class LessRandomMover(turtle.RawTurtle):
    def __init__(self, canvas, step_move=10, step_turn=10):
        super().__init__(canvas)
        self.step_move = step_move
        self.step_turn = step_turn

    def run_ai(self, oppoenent):
        opp_pos = oppoenent.pos()
        opp_heading = oppoenent.heading()
        mode = random.random()
        if mode < 0.6:
            self.forward(self.step_move)
        elif mode < 0.9:
            self.left(self.step_turn)
        elif mode == 2:
            self.right(self.step_turn)
            
class ResetTurtle(turtle.RawTurtle):
    def __init__(self, canvas, step_move = 5, step_turn = 15):
        super().__init__(canvas)
        self.step_move = step_move
        self.step_turn = step_turn
            

if __name__ == '__main__':
    canvas = turtle.Screen()
    runner = LessRandomMover(canvas)
    reset = ResetTurtle(canvas)
    chaser = ManualMover(canvas)

    game = RunawayGame(canvas, runner, reset, chaser)
    game.start()
    canvas.mainloop()