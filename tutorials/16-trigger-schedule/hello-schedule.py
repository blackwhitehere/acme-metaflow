from metaflow import FlowSpec, step, retry, kubernetes, project, schedule

@project(name='example_project')
@schedule(hourly=True)
class HelloRemoteSchedule(FlowSpec):
    """
    A flow where Metaflow prints 'Metaflow says: Hi from the cloud!' on an hourly schedule.
    """
    @kubernetes(cpu=0.5, memory=124)
    @step
    def start(self):
        print("HelloRemoteSchedule is starting.")
        self.next(self.hello)

    @kubernetes(cpu=0.5, memory=124)
    @retry
    @step
    def hello(self):
        self.message = "Hi from the Cloud!"
        print("Metaflow says: %s" % self.message)
        self.next(self.end)

    @kubernetes(cpu=0.5, memory=124)
    @step
    def end(self):
        print("HelloRemoteSchedule is finished.")


if __name__ == "__main__":
    HelloRemoteSchedule()
