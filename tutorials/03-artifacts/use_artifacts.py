from metaflow import FlowSpec, step


class UseArtifactsFlow(FlowSpec):
    """
    Show how to use artifacts from another flow.
    """

    @step
    def start(self):
        """
        Use the Metaflow client to retrieve the latest successful run from our
        MergeArtifactsFlow and assign them as data artifacts in this flow.

        """
        from metaflow import Flow, get_metadata

        # Print metadata provider
        print("Using metadata provider: %s" % get_metadata())

        # Load the analysis from the MergeArtifactsFlow.
        run = Flow("MergeArtifactsFlow").latest_successful_run
        print("Using analysis from Run '%s'" % str(run))

        self.y = run['b'].task.data.y
        print("Fetched value `y` from step `b` in flow MergeArtifactsFlow: %s" % self.y)
        self.next(self.end)

    @step
    def end(self):
        """
        This is the 'end' step. All flows must have an 'end' step, which is the
        last step in the flow.
        """
        print("UseArtifactsFlow is all done.")


if __name__ == "__main__":
    UseArtifactsFlow()
