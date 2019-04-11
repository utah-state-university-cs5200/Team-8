import time
from threading import Thread

from src.processors.constants import WORKER_SLEEP_TIME


class WorkerException(Exception):
    pass

JOB_CLIENT_ASSIGN_ID = 1


class Worker(Thread):
    """
    Parent worker class to be specialized. Specializations need to define their own
    _initJobMap functions, as well as any specific functions for their domain-specific
    jobs.

    Jobs themselves are dictionaries by convention, in the form of:
    job = {
            'id': id_num,
            'args': ['param1', 'param2',..., 'paramN']
            'kwargs': {'key1': 'value1,...,'keyN': 'valueN'}
    }
    Where the payload is a list of parameters to be passed into the function
    """
    def __init__(self, master, group=None, target=None, name=None, *args, **kwargs):
        super().__init__(group, target, name, args, kwargs)
        self.alive = True
        self.master = master
        self.jobs = []
        self._initJobMap()

    def _initJobMap(self):
        """
        Specializations will need to implement a map of job_ids -> functions to run

        ex.
        self.job_map = {job_id1: self.doFoo, job_id2: self.master.doBar}
        """
        raise NotImplementedError

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
            method = self.job_map[job['id']]
            method(*job['args'], **job['kwargs'])
        except KeyError:
            raise WorkerException("Error: Job not defined for this worker type.")

    def cleanup(self):
        self.alive = False
