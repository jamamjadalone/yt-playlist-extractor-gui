import tkinter as tk
from tkinter import messagebox, filedialog, ttk
from pytubefix import Playlist  # pip install pytubefix
import threading

class YouTubeLinkExtractor:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Playlist Link Extractor")
        self.root.geometry("800x600")
        self.videos = []
        self.check_vars = []

        # Playlist URL Input
        tk.Label(root, text="Enter YouTube Playlist URL:", font=("Arial", 12)).pack(pady=5)
        self.url_entry = tk.Entry(root, width=80, font=("Arial", 10))
        self.url_entry.pack(pady=5)

        # Extract Button
        tk.Button(root, text="Extract Links", command=self.start_extraction, bg="#4CAF50", fg="white", width=20).pack(pady=5)

        # Progress Bar
        self.progress = ttk.Progressbar(root, mode="determinate", length=600)
        self.progress.pack(pady=5)

        # Scrollable Frame for Checkboxes
        self.scroll_canvas = tk.Canvas(root, height=350)
        self.scroll_frame = tk.Frame(self.scroll_canvas)
        self.scrollbar = tk.Scrollbar(root, orient="vertical", command=self.scroll_canvas.yview)
        self.scroll_canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side="right", fill="y")
        self.scroll_canvas.pack(side="left", fill="both", expand=True)
        self.canvas_window = self.scroll_canvas.create_window((0, 0), window=self.scroll_frame, anchor="nw")

        self.scroll_frame.bind("<Configure>", lambda e: self.scroll_canvas.configure(scrollregion=self.scroll_canvas.bbox("all")))

        # Button Frame
        button_frame = tk.Frame(root)
        button_frame.pack(pady=5)
        tk.Button(button_frame, text="Select All", command=self.select_all, bg="#2196F3", fg="white", width=15).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Deselect All", command=self.deselect_all, bg="#9C27B0", fg="white", width=15).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="Copy Selected", command=self.copy_selected, bg="#607D8B", fg="white", width=15).grid(row=0, column=2, padx=5)
        tk.Button(button_frame, text="Save Selected to TXT", command=self.save_txt, bg="#FF9800", fg="white", width=20).grid(row=0, column=3, padx=5)

    def start_extraction(self):
        threading.Thread(target=self.extract_links, daemon=True).start()

    def extract_links(self):
        playlist_url = self.url_entry.get().strip()
        if not playlist_url:
            messagebox.showerror("Error", "Please enter a YouTube playlist URL.")
            return

        # Clear previous UI
        for widget in self.scroll_frame.winfo_children():
            widget.destroy()
        self.progress["value"] = 0

        try:
            pl = Playlist(playlist_url)
            total_videos = len(pl.videos)
            self.progress["maximum"] = total_videos

            videos = []
            for idx, video in enumerate(pl.videos, 1):
                videos.append((video.title, video.watch_url))
                self.progress["value"] = idx
                self.root.update_idletasks()  # Update progress bar

            self.root.after(0, lambda: self.display_videos(videos))

        except Exception as e:
            messagebox.showerror("Error", f"Failed to extract links: {e}")

    def display_videos(self, videos):
        for widget in self.scroll_frame.winfo_children():
            widget.destroy()

        self.videos = videos
        self.check_vars = []

        tk.Label(self.scroll_frame, text=f"Total Videos: {len(self.videos)}", font=("Arial", 11, "bold")).pack(anchor="w")

        for title, url in self.videos:
            var = tk.BooleanVar()
            chk = tk.Checkbutton(self.scroll_frame, text=f"{title} ({url})", variable=var, wraplength=750, justify="left", anchor="w")
            chk.pack(fill="x", anchor="w", padx=5)
            self.check_vars.append((var, title, url))

    def select_all(self):
        for var, _, _ in self.check_vars:
            var.set(True)

    def deselect_all(self):
        for var, _, _ in self.check_vars:
            var.set(False)

    def copy_selected(self):
        selected_links = [(title, url) for var, title, url in self.check_vars if var.get()]
        if not selected_links:
            selected_links = self.videos  # Copy all if none selected

        text_to_copy = "\n\n".join([f"{i+1}. {title}\n{url}" for i, (title, url) in enumerate(selected_links)])
        self.root.clipboard_clear()
        self.root.clipboard_append(text_to_copy)
        messagebox.showinfo("Copied", "Selected links copied to clipboard!")

    def save_txt(self):
        selected_links = [(title, url) for var, title, url in self.check_vars if var.get()]

        if not selected_links:
            messagebox.showwarning("Warning", "No videos selected to save!")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            try:
                with open(file_path, "w", encoding="utf-8") as f:
                    for i, (title, url) in enumerate(selected_links, 1):
                        f.write(f"{i}. {title}\n{url}\n\n")
                messagebox.showinfo("Success", f"Selected links saved to {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubeLinkExtractor(root)
    root.mainloop()
