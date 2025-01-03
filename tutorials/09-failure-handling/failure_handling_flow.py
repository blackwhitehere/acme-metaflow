from metaflow import FlowSpec, step, retry, catch, timeout

class HandleFailure(FlowSpec):

    # will retry the step for three times before giving up. It waits for 2 minutes between retries for remote tasks
    @retry # pass params to retry like retry(times=4, minutes_between_retries=1) to modify default
    @step
    def start(self):
        import time
        if int(time.time()) % 2 == 0:
            raise Exception("Bad luck!")
        else:
            print("Lucky you!")
        self.next(self.withdraw_money_from_account)

    @retry(times=0)
    @step
    def withdraw_money_from_account(self):
        print("This step will be never be retried to avoid withdrawing money multiple times")
        self.next(self.start_catch)

    @step
    def start_catch(self):
        self.params = range(3)
        self.next(self.compute, foreach='params')

    # catch decorator will make sure flow execution continues even if the step fails allowing flow to recover
    @catch(var='compute_failed', print_exception=True)
    @step
    def compute(self):
        """This will fail when self.input is 0"""
        self.div = self.input
        self.x = 5 / self.div
        self.next(self.join)

    @step
    def join(self, inputs):
        """Handles the failed computation by reading the 'compute_failed' variable set by the catch decorator"""
        for input in inputs:
            if input.compute_failed:
                print('compute failed for parameter: %d' % input.div)
        self.next(self.start_platform_exception)

    # Catch can also handle exceptions from failed infrastructure/platform issues
    # rather than just application exceptions
    @catch(var='start_platform_exception_failed')
    @retry
    @step
    def start_platform_exception(self):
        import os, signal
        # kill this process with the KILL signal
        os.kill(os.getpid(), signal.SIGKILL)
        self.next(self.end_platform_exception)

    @step
    def end_platform_exception(self):
        if self.start_platform_exception_failed is not None:
            print("It seems 'start' did not survive.")
        self.next(self.timeout)

    @catch(var='timeout_failed')
    @timeout(seconds=5)
    @step
    def timeout(self):
        import time
        for i in range(100):
            print(i)
            time.sleep(1)
        self.next(self.end)

    @step
    def end(self):
        print("Phew!")

if __name__ == '__main__':
    HandleFailure()