from metaflow import FlowSpec, step, retry, kubernetes, project

@project(name='example_project')
class HelloRemoteOrchestration(FlowSpec):
    """
    A flow where Metaflow prints 'Metaflow says Hi from the cloud!'

    Run this flow to validate your Kubernetes configuration.

    """
    @kubernetes(cpu=0.5, memory=124)
    @step
    def start(self):
        print("HelloRemoteOrchestration is starting.")
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
        print("HelloRemoteOrchestration is finished.")


if __name__ == "__main__":
    HelloRemoteOrchestration()
