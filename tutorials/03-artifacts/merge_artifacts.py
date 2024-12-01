from metaflow import FlowSpec, step

class MergeArtifactsFlow(FlowSpec):
    """
    Shows how to merge artifacts from different branches.
    """
    # https://docs.metaflow.org/metaflow/basics#data-flow-through-the-graph

    @step
    def start(self):
        """Sets an artifact and launches two parallel branches."""
        self.pass_down = 'a' # unmodified value
        self.next(self.a, self.b)

    @step
    def a(self):
        """Sets conflicing values for x and y with step `b`"""
        self.common = 5 # value is the same as in b, so no conflict
        self.x = 1
        self.y = 3
        self.from_a = 6
        self.next(self.join)

    @step
    def b(self):
        """Sets conflicing values for x and y with step `a`"""
        self.common = 5 # value is the same as in a, so no conflict
        self.x = 2
        self.y = 4
        self.next(self.join)

    @step
    def join(self, inputs):
        """Merges artifacts from steps `a` and `b`"""
        # x is set to the value from step `a`, so merge_artifacts will not overwrite it
        self.x = inputs.a.x
        # value of y is ambiguous, so we need to exclude it from the merge
        self.merge_artifacts(inputs, exclude=['y'])
        print('x is %s' % self.x)
        print('pass_down is %s' % self.pass_down)
        print('common is %d' % self.common) # is available because it is the same value in both branches
        print('from_a is %d' % self.from_a) # from_a is only available in branch a, but is not conflicting so is availble
        self.next(self.c)

    @step
    def c(self):
        """Launch parallel branches `d` and `e` to show how to include only certain artifacts in a step"""
        self.next(self.d, self.e)

    @step
    def d(self):
        self.conflicting = 7
        self.next(self.join2)

    @step
    def e(self):
        self.conflicting = 8
        self.next(self.join2)

    @step
    def join2(self, inputs):
        """Shows how to include only certain artifacts in a step"""
        self.merge_artifacts(inputs, include=['pass_down', 'common'])
        print('Only pass_down and common exist here')
        print(f"Has attribure self.from_a: `{hasattr(self, 'from_a')}`")
        self.next(self.end)

    @step
    def end(self):
        pass

if __name__ == '__main__':
    MergeArtifactsFlow()