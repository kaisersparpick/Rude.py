# Rude.py
Rude.py is a **Python** implementation of the *rule-based control-flow pattern* [Rude](https://github.com/kaisersparpick/Rude).

## Usage

#### Creating an instance
```python
from rude import Rude
rude = Rude()
```

#### Adding a rule

```js
rude.add_rule(app.py_found, app.pycache_pyc_found, app.pyc_found)
rude.add_rule(app.success)
```
`add_rule` accepts three arguments: the condition to check, the function to call when the result is true, and the function to call when it is false. Each argument can be a function reference, None or left empty.

The return value of conditions must be `True` for proceeding with the yes callback and `False` with the no branch. When a condition returns `None`, Rude exits the condition chain. In this case, the yes and no callbacks are not necessary. These conditions are usually exit points.

#### Checking conditions

Checking conditions based on the applied rules is triggered by calling `rude.check_conditions()`.

```js
rude.check_conditions(app.py_found)
```

This specifies the entry point in the condition chain and can be set to any valid rule condition.

See the examples for more details.

## Benefits

  - Rude allows for an on-demand execution of a chain of `dynamic if-then-else` statements - hereinafter referred to as `rules`.
  - The control flow is easy to manage and the logic can be modified by simply changing the callbacks in the `rules`.
  - The chain of condition checking can be exited or paused at any given point.
  - The position in the `rule` hierarchy can be stored and the execution resumed at a later stage by setting the `entry point`. 
  - Each `rule` is seen as a separate and *independent logical unit*.
  - Individual `rules` and groups of rules can be easily moved around.
  - `Rules` can be generated dynamically or loaded from a datasource. 
  - The dispatcher makes it possible to ditch the rigid static conditional model in favour of a considerably more flexible one.
