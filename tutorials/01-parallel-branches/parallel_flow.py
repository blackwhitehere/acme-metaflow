from metaflow import FlowSpec, step


class ParallelFlow(FlowSpec):
    """
    A flow to demonstrate parallel branches in Metaflow.
    """

    @step
    def start(self):
        """
        This step lanuches two parallel branches.

        """
        print("ParallelFlow is starting.")
        self.next(self.hello_short, self.hello_long)

    @step
    def hello_short(self):
        """
        The first of parallely executed steps.
        """
        print("Metaflow says: Hi!")
        self.a = 1
        self.next(self.join)

    @step
    def hello_long(self):
        """
        The second of parallely executed steps.
        """
        print("Metaflow says: Hello World!")
        self.b = 2
        self.next(self.join)

    @step
    def join(self, inputs):
        """
        Join parallel branches and merge results.
        """
        # Access data set in branches.
        self.a = inputs.hello_short.a
        self.b = inputs.hello_long.b
        self.next(self.end)

    @step
    def end(self):
        """
        This is the 'end' step. All flows must have an 'end' step, which is the
        last step in the flow.
        """
        print("ParallelFlow is all done.")


if __name__ == "__main__":
    ParallelFlow()
