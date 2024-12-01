from metaflow import FlowSpec, step, project, current

@project(name='project_abc')
class SimpleFlow(FlowSpec):
    """
    Simple flow used to show how to load results of flow execution.
    """

    @step
    def start(self):
        """
        This is the 'start' step. All flows must have a step named 'start' that
        is the first step in the flow.

        """
        print("SimpleFlow is starting.")
        self.next(self.hello_short)

    @step
    def hello_short(self):
        print("hello_short has a different step name: %s" % current.step_name)
        print("hello_short has a different task id: %s" % current.task_id)
        print("hello_short has a different pathspec: %s" % current.pathspec)
        self.a=2
        self.next(self.hello_long)

    @step
    def hello_long(self):
        print("flow name: %s" % current.flow_name)
        print("run id: %s" % current.run_id)
        print("origin run id: %s" % current.origin_run_id)
        print("step name: %s" % current.step_name)
        print("task id: %s" % current.task_id)
        print("pathspec: %s" % current.pathspec)
        print("namespace: %s" % current.namespace)
        print("username: %s" % current.username)
        print("flow parameters: %s" % str(current.parameter_names))
        self.next(self.end)

    @step
    def end(self):
        """
        This is the 'end' step. All flows must have an 'end' step, which is the
        last step in the flow.

        """
        print("SimpleFlow is all done.")


if __name__ == "__main__":
    SimpleFlow()
