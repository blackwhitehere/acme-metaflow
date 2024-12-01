from metaflow import FlowSpec, step, conda, conda_base

import platform


# Use the specified version of python for this flow.
@conda_base(python=platform.python_version(), packages={"numpy": "1.26.4"})
class DependencyFlow(FlowSpec):
    """
    """
    @conda(packages={"pandas": "1.5.3"})
    @step
    def start(self):
        """
        """
        import pandas as pd
        import numpy as np

        self.distance = pd.DataFrame({'a': [1,2,3]})

        self.arr = np.array([1, 2, 3])

        self.next(self.peekaboo)

    @conda(disabled=True)
    @step
    def peekaboo(self):
        import sys
        print(sys.executable)
        self.next(self.end)

    @step
    def end(self):
        """
        """
        from mymodule import hello
        from mypackage.module_in_package import hello_short
        hello()
        hello_short()
        print("Since the same version of numpy is set for all steps, the array can"
              f"be accessed without pickling error: {self.arr}")


if __name__ == "__main__":
    DependencyFlow()
