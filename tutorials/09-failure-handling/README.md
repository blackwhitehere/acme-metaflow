# Episode 09-failure-handling

**Shows how to make flows robust to failures**

More info at [Link](https://docs.metaflow.org/scaling/failures).

#### Showcasing:
- Use `retry` to deal with transient platform issues. You can add it for all steps with the `--with retry` option on command line.
- Use `retry` with `catch` if you want your code to deal with faulty steps.
- Use `catch` without `retry` to handle steps that can't be retried safely. It is a good idea to pass `times=0` to retry in this case.
- Use `timeout` with any of the above if your code can get stuck.


#### To play this episode:
1. ```cd tutorials```
2. ```python 09-failure-handling/failure_handling_flow.py --no-pylint run```

