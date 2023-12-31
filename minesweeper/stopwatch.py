from threading import Thread, Event as ThreadEvent
from tkinter import *
from time import *

class Stopwatch():
    def __init__(self, update_callback= None) -> None:
        self.count: int         = 0
        self.is_counting: bool  = False

        self.update_callback = update_callback

        self._stop: ThreadEvent = ThreadEvent()
        self.thread:Thread      = Thread(target=self.__conter)

    def __conter(self) -> None:
        if not self.is_counting: self.is_counting = True
        while not self._stop.is_set():
            self.count += 1
            sleep(1)
            if self.update_callback: self.update_callback(self.count)

    def start_count(self):
        self.thread.start()

    def stop_count(self) -> None:
        self.is_counting = False
        self._stop.set()
