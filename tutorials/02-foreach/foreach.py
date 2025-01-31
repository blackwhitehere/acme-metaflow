from metaflow import FlowSpec, step


class ForeachFlow(FlowSpec):
    """
    A flow to demonstrate the use of foreach in Metaflow.

    """

    @step
    def start(self):
        n_chunks = 10
        print(f"Launching parallelizable computation for {n_chunks} chunks.")
        self.chunks = list(range(n_chunks))
        self.next(self.parallel_compute, foreach="chunks") # note: do not use num_parallel kwarg, use `--max-workers <n>` on command line instead

    @step
    def parallel_compute(self):
        """Uses the reserved attribute 'self.input' for value of chunk being worked on."""
        self.chunk = self.input
        sum = 0
        for i in range(10_000):
            sum += i * i + self.chunk
        self.sum = sum
        print(f"Sum for chunk {self.chunk}: {sum}")
        self.next(self.join)

    @step
    def join(self, inputs):
        self.final_sum = sum(input.sum for input in inputs)
        print(f"Final sum of parallelizable compute: {self.final_sum}")
        self.next(self.end)

    @step
    def end(self):
        print("ForeachFlow is all done.")


if __name__ == "__main__":
    ForeachFlow()
