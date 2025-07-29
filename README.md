# 🎯 YouTube Playlist Link Extractor GUI

Extract **YouTube playlist video titles & URLs** using a user-friendly **Tkinter GUI**. Features include:
- Scrollable checkbox list of videos
- Real‑time **progress bar** during extraction
- **Select All / Deselect All**, **Copy to Clipboard**, and **Save to TXT** support
- Runs responsively using **threading** and **pytubefix**




## 🚀 Features
- Paste a **YouTube playlist URL** into the GUI
- Use a **scrollable checkbox list** to view video title + URL
- Real-time **progress bar** while processing playlists
- Remains responsive thanks to **background threading**
- Buttons: **Select All**, **Deselect All**, **Copy Selected**, **Save Selected to TXT**

---

## 🛠️ Tech Stack
- **Python 3.x**
- **Tkinter** for GUI
- **pytubefix** for parsing YouTube playlists
- **threading** to prevent UI freeze
- Clipboard & file-handling utilities for UX

---

## ⚙️ Installation & Quick Start

```bash
git clone https://github.com/jamamjadalone/yt-playlist-extractor-gui.git
cd yt-playlist-extractor-gui
pip install pytubefix
python extract_gui.py


## 🚀 Quick Start

1. Run `extract_gui.py`  
2. Enter your YouTube playlist URL and click Extract Links  
3. Watch the progress bar until extraction completes  
4. Use Select All / Deselect All as needed  
5. Click Copy Selected to copy titles + links  
6. Or click Save Selected to TXT to export a `.txt` file  

---

✨ Why Choose This Tool? 
Ideal for content creators, SEO analysts, and developers—this GUI tool saves hours of manual copying and ensures you can export only the videos you need. It stays fully responsive, even with long playlists (100+ videos).

---

🧩 Repository Structure
```bash
/youtube-playlist-link-extractor-gui
├── extract_gui.py
├── README.md
├── requirements.txt
└── .gitignore

## 📜 License

This project is **open-source** and licensed under the [MIT License](LICENSE).

Open-source & MIT-style — feel free to fork, modify, and adapt this tool for your workflow!
