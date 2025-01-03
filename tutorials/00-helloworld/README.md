# Episode 00-helloworld

**Shows basic syntax for defining a flow.**

Metaflow introduces a Python based Domain Specific Language for defining Directed Acycilc Graph (DAG) computation.

Users implement `Flows` (akin to programs) that must have one `start` and one `end` `Step` (akin to functions).
Each step must define next step to execute.

For explanation of all concepts see [Link](https://docs.metaflow.org/internals/technical-overview#development-time-components)

#### Showcasing:
- `FlowSpec` base class to define a new `Flow`
- `step` decorator to split computation into `Steps`
- `self.next` method to indicate next `Step` to execute
- creating Flow instance inside `if __name__ == "__main__"` block to expose flow execution CLI

#### To play this episode:
1. ```cd tutorials```
2. ```python 00-helloworld/helloworld.py show```
3. ```python 00-helloworld/helloworld.py run```
