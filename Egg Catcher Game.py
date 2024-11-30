from itertools import cycle
from random import randrange
from tkinter import Tk, Canvas, messagebox


class EggCatcherGame:
    def __init__(self, width=800, height=400):
        # Initialize game variables
        self.canvas_width = width
        self.canvas_height = height
        self.color_cycle = cycle(['light blue', 'light pink', 'light yellow', 'light green', 'red', 'blue', 'green', 'black'])
        self.egg_width = 45
        self.egg_height = 55
        self.egg_score = 10
        self.egg_speed = 500
        self.egg_interval = 4000
        self.difficulty_factor = 0.95
        self.score = 0
        self.lives_remaining = 3
        self.eggs = []

        # Initialize Tkinter
        self.win = Tk()
        self.win.title("Egg Catcher Game")
        self.canvas = Canvas(self.win, width=self.canvas_width, height=self.canvas_height, background='deep sky blue')
        self.canvas.create_rectangle(-5, self.canvas_height - 100, self.canvas_width + 5, self.canvas_height + 5,
                                     fill='sea green', width=0)
        self.canvas.create_oval(-80, -80, 120, 120, fill='orange', width=0)  # Sun
        self.canvas.pack()

        # Catcher properties
        self.catcher_width = 100
        self.catcher_height = 100
        catcher_start_x = self.canvas_width / 2 - self.catcher_width / 2
        catcher_start_y = self.canvas_height - self.catcher_height - 20
        self.catcher = self.canvas.create_arc(catcher_start_x, catcher_start_y,
                                              catcher_start_x + self.catcher_width,
                                              catcher_start_y + self.catcher_height,
                                              start=200, extent=140, style='arc',
                                              outline='blue', width=3)

        # Score and lives display
        self.score_text = self.canvas.create_text(10, 10, anchor='nw', font=('Arial', 18, 'bold'),
                                                  fill='darkblue', text='Score: 0')
        self.lives_text = self.canvas.create_text(self.canvas_width - 10, 10, anchor='ne', font=('Arial', 18, 'bold'),
                                                  fill='darkblue', text='Lives: 3')

        # Bind keys
        self.canvas.bind('<Left>', self.move_left)
        self.canvas.bind('<Right>', self.move_right)
        self.canvas.focus_set()

    def create_eggs(self):
        """Create new eggs at random positions."""
        x = randrange(10, self.canvas_width - self.egg_width)
        y = 40
        new_egg = self.canvas.create_oval(x, y, x + self.egg_width, y + self.egg_height, fill=next(self.color_cycle),
                                          width=0)
        self.eggs.append(new_egg)
        self.win.after(self.egg_interval, self.create_eggs)

    def move_eggs(self):
        """Move eggs downward and check if they hit the ground."""
        for egg in self.eggs:
            (egg_x, egg_y, egg_x2, egg_y2) = self.canvas.coords(egg)
            self.canvas.move(egg, 0, 10)
            if egg_y2 > self.canvas_height:
                self.egg_dropped(egg)
        self.win.after(self.egg_speed, self.move_eggs)

    def egg_dropped(self, egg):
        """Handle eggs that are not caught."""
        self.eggs.remove(egg)
        self.canvas.delete(egg)
        self.lose_a_life()
        if self.lives_remaining == 0:
            self.game_over()

    def lose_a_life(self):
        """Decrease lives when an egg is missed."""
        self.lives_remaining -= 1
        self.canvas.itemconfigure(self.lives_text, text=f'Lives: {self.lives_remaining}')

    def catch_check(self):
        """Check if eggs are caught by the catcher."""
        (catcher_x, catcher_y, catcher_x2, catcher_y2) = self.canvas.coords(self.catcher)
        for egg in self.eggs:
            (egg_x, egg_y, egg_x2, egg_y2) = self.canvas.coords(egg)
            if catcher_x < egg_x and egg_x2 < catcher_x2 and catcher_y2 - egg_y2 < 40:
                self.eggs.remove(egg)
                self.canvas.delete(egg)
                self.increase_score(self.egg_score)
        self.win.after(100, self.catch_check)

    def increase_score(self, points):
        """Increase the score and make the game progressively harder."""
        self.score += points
        self.egg_speed = int(self.egg_speed * self.difficulty_factor)
        self.egg_interval = int(self.egg_interval * self.difficulty_factor)
        self.canvas.itemconfigure(self.score_text, text=f'Score: {self.score}')

    def move_left(self, event):
        """Move the catcher to the left."""
        (x1, _, x2, _) = self.canvas.coords(self.catcher)
        if x1 > 0:
            self.canvas.move(self.catcher, -20, 0)

    def move_right(self, event):
        """Move the catcher to the right."""
        (x1, _, x2, _) = self.canvas.coords(self.catcher)
        if x2 < self.canvas_width:
            self.canvas.move(self.catcher, 20, 0)

    def game_over(self):
        """End the game and show the final score."""
        messagebox.showinfo('GAME OVER!', f'Final Score: {self.score}')
        self.win.destroy()

    def start_game(self):
        """Start the game loop."""
        self.win.after(1000, self.create_eggs)
        self.win.after(1000, self.move_eggs)
        self.win.after(1000, self.catch_check)
        self.win.mainloop()


# Run the game
if __name__ == "__main__":
    game = EggCatcherGame()
    game.start_game()
