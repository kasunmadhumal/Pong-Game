from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.core.window import Window
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.app import App


# We add a PongPaddle class to create a widget that
# will be our  player rackets and it defence the ball from hitting the wall
class PongPaddle(Widget):
    score = NumericProperty(0)

    # The PongPaddle class also implements a bounce_ball method,
    # so that the ball bounces differently based on where it hits the racket
    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * 1.1
            ball.velocity = vel.x, vel.y + offset




# We add a new PongBall class to create a widget that will be our ball and make it bounce around.
class PongBall(Widget):

    # velocity of the ball on x and y axis
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    # referencelist property so we can use ball.velocity as
    # a shorthand, just like e.g. w.pos for w.x and w.y
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    # ``move`` function will move the ball one step. This
    #  will be called in equal intervals to animate the ball
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos





# inherit all the functions from widget class.
# inside this class we are create the pong game.
class PongGame(Widget):
    Window.clearcolor = (100, 100, 0, 0)
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    # sets a random x and y velocity for the ball, and also resets the position
    def serve_ball(self, vel=(4, 0)):
        self.ball.center = self.center
        self.ball.velocity = vel

    # using this method , we can easily reference the ball property inside
    # the update method and even make it bounce off the edges. also it's update the players scores
    def update(self, dt):
        self.ball.move()

        # bounce of paddles
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

        # bounce ball off bottom or top
        if (self.ball.y < self.y) or (self.ball.top > self.top):
            self.ball.velocity_y *= -1

        # went of to a side to score point?
        if self.ball.x < self.x:
            self.player2.score += 1
            self.serve_ball(vel=(4, 0))

        if self.ball.right > self.width:
            self.player1.score += 1
            self.serve_ball(vel=(-4, 0))


    # The on_touch_move function for the PongGame class and have it set the position of the
    # left or right player based on whether the touch occurred on the left or right side of the screen.
    def on_touch_move(self, touch):
        if touch.x < self.width / 3:
            self.player1.center_y = touch.y
        if touch.x > self.width - self.width / 3:
            self.player2.center_y = touch.y


# create PongApp class and it inherits from App class .
# also the inside this PongApp class  we are build the app
class PongApp(App):

    # using this build method we build the app and return the game
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game
