from src.processors.worker import Worker, JOB_CLIENT_ASSIGN_ID


class PlayerClientWorker(Worker):
    def _initJobMap(self):
        self.job_map = {
            JOB_CLIENT_ASSIGN_ID: self.master.setID
        }
