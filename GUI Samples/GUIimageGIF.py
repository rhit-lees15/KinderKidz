import tkinter as tk
from PIL import Image, ImageTk

class GIFPlayer(tk.Frame):
    def __init__(self, master, gif_path):
        super().__init__(master)
        self.master = master
        self.gif_path = gif_path
        self.load_gif()
        self.create_widgets()

    def load_gif(self):
        self.gif = Image.open(self.gif_path)
        self.frames = []
        try:
            while True:
                self.frames.append(ImageTk.PhotoImage(self.gif))
                self.gif.seek(len(self.frames))
        except EOFError:
            pass

    def create_widgets(self):
        self.label = tk.Label(self.master, image=self.frames[0])
        self.label.pack()

        self.animate(0)

    def animate(self, frame):
        self.label.config(image=self.frames[frame])
        frame = (frame + 1) % len(self.frames)
        self.master.after(100, self.animate, frame)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("GIF Player")
    gif_path = "MARSHALL.gif"
    player = GIFPlayer(root, gif_path)
    player.pack()
    root.mainloop()
