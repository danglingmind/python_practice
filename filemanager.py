#! /usr/local/bin/python3.7
import time
import os
import shutil
import re
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class OnMyWatch:
    # Set the directory on watch
    watchDirectory = "/Users/ricky/Downloads"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(
            event_handler, self.watchDirectory, recursive=False)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer Stopped")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None
        else:
            # make directories if not present
            mkdirIfnotExists('/Users/ricky/Downloads/Images')
            mkdirIfnotExists('/Users/ricky/Downloads/Docs')
            mkdirIfnotExists('/Users/ricky/Downloads/dmg')
            mkdirIfnotExists('/Users/ricky/Downloads/zip')

            # directory mapping according to the type of the file
            dirmap = {'.txt': 'Docs',
                      '.pdf': 'Docs',
                      '.csv': 'Docs',
                      '.pdf': 'Docs',
                      '.doc': 'Docs',
                      '.docx': 'Docs',
                      '.jpg': 'Images',
                      '.jpeg': 'Images',
                      '.png': 'Images',
                      '.gif': 'Images',
                      '.dmg': 'dmg',
                      '.zip': 'zip',
                      '.tar': 'zip',
                      }
            # move the images to this folder
            for r, d, f in os.walk('/Users/ricky/Downloads'):
                if r == '/Users/ricky/Downloads':
                    for file in f:
                        # get the extension
                        _, ext = os.path.splitext(file)
                        if ext in dirmap:
                            shutil.move('/Users/ricky/Downloads/'+file,
                                        '/Users/ricky/Downloads/'+dirmap[ext])


def mkdirIfnotExists(path):
    if not os.path.exists(path):
        os.makedirs(path)


def isImage(file):
    regex = r"(.jpg|.jpeg|.gif|.png)"
    match = re.findall(regex, file)
    if len(match) > 0:
        return True
    else:
        return False


if __name__ == '__main__':
    watch = OnMyWatch()
    watch.run()
