# Episode 03-artifacts

**Shows data `Artifacts` that are automatically persisted when flow is run.
Use them to persist data you want to have access to once the flow completes.
They also help to make flow execution faster when debugging/re-trying failed flows
because flow data can be re-loaded.**

#### Showcasing:
- Creating artifacts by setting instance variables in steps.
- How to merge artifacts from parallel branches using `self.merge_artifacts`.
- Using data artifacts generated from other flows using `Flow` class.


#### To play this episode:
1. ```cd tutorials```
2. ```python 03-artifacts/merge_artifacts.py show```
3. ```python 03-artifacts/use_artifacts.py run```
