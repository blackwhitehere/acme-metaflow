from metaflow import FlowSpec, step

class ForeachFlow(FlowSpec):
    """
    A flow to demonstrate the use of foreach in Metaflow.
    """

    @step
    def start(self):
        """Launches parallel branches based on data in 'titles'."""
        self.titles = ['Stranger Things',
                       'House of Cards',
                       'Narcos']
        self.next(self.a, foreach='titles')

    @step
    def a(self):
        """Uses the reserved attribute 'self.input' to access the data."""
        self.title = '%s processed' % self.input
        self.next(self.join)

    @step
    def join(self, inputs):
        """Reads the results from the parallel branches."""
        self.results = [input.title for input in inputs]
        self.next(self.end)

    @step
    def end(self):
        """
        This is the 'end' step. All flows must have an 'end' step, which is the
        last step in the flow.
        """
        print('\n'.join(self.results))

if __name__ == '__main__':
    ForeachFlow()