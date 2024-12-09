# Episode 09-failure-handling

**Shows how to make flows robust to failures**

More info at [Link](https://docs.metaflow.org/scaling/failures).

#### Showcasing:
- Use `retry` to deal with transient platform issues. You can do this easily on the command line with the --with retry option.
- Use `retry` with `catch` for extra robustness if you have modified your code to deal with faulty steps which are handled by catch.
- Use `catch` without `retry` to handle steps that can't be retried safely. It is a good idea to use times=0 for retry in this case.
- Use `timeout` with any of the above if your code can get stuck.


#### To play this episode:
1. ```cd tutorials```
2. ```python 09-failure-handling/failure_handling_flow.py --no-pylint run```

