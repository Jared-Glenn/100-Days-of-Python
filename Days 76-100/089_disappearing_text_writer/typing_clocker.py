from datetime import time
import math


class TypingClocker:
    def __init__(self):
        self.running = False
        self.counter = 0

    def restart_timer(self):
        self.counter = 0
        self.running = True

    def stop_timer(self):
        self.running = False

    def count(self):
        if self.running:
            seconds = self.counter % 60

            dt = time(second=seconds)
            string = dt.isoformat(timespec='auto')
            self.counter += 1

            return string

    def calculate_wpm(self, words):
        self.stop_timer()
        words_per_second = words/self.counter
        wpm = math.floor(words_per_second * 60)
        return wpm
