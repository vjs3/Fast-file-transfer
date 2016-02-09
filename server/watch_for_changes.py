import time
import sys
import os

from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


from locking import Semaphore

# Usage


def get_file_name(absolute_path):
    string = absolute_path
    string = string[::-1]
    file_name = string[: string.find('/')][::-1]
    return file_name

FTP_PATH = '/home/pygeek/Desktop/oslab/ftp/'
USER_PATH = '/home/pygeek/Desktop/oslab/ftp/user/'

class MyHandler(PatternMatchingEventHandler):
    patterns = ["*.txt"]
    def process(self, event):
        # the file will be processed there

        try:
            lock = Semaphore("/tmp/dir_lock.tmp")
            lock.acquire()
            path =  event.src_path
            print path
            # Do important stuff that needs to be synchronized
            time.sleep(50)
            fo = open(path, "rw+")
            count = fo.readline().strip()
            print count
            file_name = get_file_name(fo.readline().strip())
            print file_name
            file_name =  file_name[:-1]
            print file_name
            fo.close()
            for i in xrange(1,int(count)+1):
                os.rename(FTP_PATH + file_name + '.' + str(i), USER_PATH + file_name + '.'  + str(i))


            lock.release()

        finally: 
            lock.release()
            print 'released by driver'


    def on_created(self, event):
        self.process(event)


if __name__ == '__main__':
    args = sys.argv[1:]
    watcher = Observer()
    watcher.schedule(MyHandler(), path=args[0] if args else '.')
    # recursive=True
    watcher.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        watcher.stop()

    watcher.join()

