import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("Langit biru cinta searah", 0.06),
        ("Bagai ada tempat yang cerah dalam hati", 0.07),
        ("Bisa bertemu hanya denganmu", 0.06),
        ("Aku pun merasa bahagia", 0.08),
        ("Kusuka kepada dirimu", 0.09),
        ("Sangat suka", 0.1),
        ("♡", 0.1),
    ]
    delays = [0.3, 3.3, 7.1, 10.1, 14.0, 16.9, 18.8]
    
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()
