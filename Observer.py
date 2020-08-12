import time
import os
import json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import Organizer


class Handler(FileSystemEventHandler):
    def on_created(self, event):
        py_dir = os.getcwd()
        with open("Extensions.json", "r+") as jsonfile:
            data = json.load(jsonfile)
            dl_dir = data["download_dir"]
            directories = [directory for directory in data["filetypes"]
                           for directory in directory]
            filetypes = data["filetypes"]
            Organizer.file_organize(dl_dir, *filetypes, directories)
            os.chdir(py_dir)


def run_handler(dl_dir, filetypes):
    event_handler = Handler()
    obs = Observer()
    obs.schedule(event_handler, dl_dir, False)
    obs.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        obs.stop()
        obs.join()
