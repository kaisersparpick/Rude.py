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
