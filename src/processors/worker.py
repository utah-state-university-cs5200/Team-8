import time
from threading import Thread

from src.processors.constants import WORKER_SLEEP_TIME


class WorkerException(Exception):
    pass


class Worker(Thread):
    JOB_ID_MAP = {

    }

    def __init__(self, master, group=None, target=None, name=None, *args, **kwargs):
        super().__init__(group, target, name, args, kwargs)
        self.alive = True
        self.master = master
        self.jobs = []

    def run(self):
        while self.alive:
            if len(self.jobs) > 0:
                job = self.jobs.pop(0)
                self._doWork(job)
            else:
                time.sleep(WORKER_SLEEP_TIME)

    def process(self, job):
        self.jobs.append(job)

    def _doWork(self, job):
        try:
            method = self.__class__.JOB_ID_MAP[job['id']]
            method(job)
        except KeyError:
            raise WorkerException("Error: Job not defined for this worker type.")

    def cleanup(self):
        self.alive = False
