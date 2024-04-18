import tkinter as tk
from PIL import Image, ImageTk
import pygame

class GIFViewerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GIF Viewer")

        # Set window size to be square
        window_size = 400
        self.root.geometry(f"{window_size}x{window_size}")

        # Load the GIF image
        self.gif_image = Image.open("jarvisGUI.gif")
        self.gif_frames = [ImageTk.PhotoImage(frame) for frame in self.iterate_frames(self.gif_image)]

        # Create a label to display the image
        self.image_label = tk.Label(root)
        self.image_label.pack()

        # Create a start button to begin the animation
        self.start_button = tk.Button(root, text="Start Animation", command=self.start_animation)
        self.start_button.pack(side=tk.LEFT, padx=10, pady=10)

        # Create a stop button to stop the animation
        self.stop_button = tk.Button(root, text="Stop Animation", command=self.stop_animation)
        self.stop_button.pack(side=tk.LEFT, padx=10, pady=10)

        # Load and play music
        pygame.init()
        pygame.mixer.init()
        self.music_file = "Entry.mp3"
        pygame.mixer.music.load(self.music_file)

        # Start animation
        self.current_frame = 0
        self.duration = 5000  # 5 seconds

    def iterate_frames(self, gif):
        while True:
            try:
                yield gif.copy()
                gif.seek(gif.tell() + 1)
            except EOFError:
                break

    def animate(self):
        if self.current_frame < len(self.gif_frames):
            self.image_label.config(image=self.gif_frames[self.current_frame])
            self.current_frame += 1
            self.root.after(100, self.animate)
        else:
            self.root.after(self.duration, self.root.destroy)  # Close the window after 5 seconds

    def start_animation(self):
        pygame.mixer.music.play()
        self.current_frame = 0  # Start from the first frame
        self.animate()

    def stop_animation(self):
        pygame.mixer.music.stop()

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = GIFViewerApp(root)
#     root.mainloop()
