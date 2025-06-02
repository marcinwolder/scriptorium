# Scriptorium Interpreter Implementation

In this document you can find details on how **🪶 Scriptorium** interpreter was created.

## Variable Management (`Var` class)

### Use of var_map

To keep track of every variable in Scriptorium we use a dictionary. We have a list of tokens that we define as **"scope tokens"** (list of tokens below). Those tokens are keys in `var_map` dictionary. Then there is another dictionary where keys are variable names and values are `Var` objects.

Structure of `var_map`:

```python
var_map: Dict[ctx, Dict[str, Var]]
```

*\* Where `ctx` is a type of node context object*

**Example:**  

```scriptorium
numerus a esto 5.
nihil munus func(numerus x):
    scribere x.
```

would result with `var_map` looking like this:

```python
{
    <ctx of "scope token" node>: {
        "a": <Var>,
        "func": <FuncVar>
    }
    <ctx of "scope token" node>: {
        "x": <ParamVar>
    }
}
```

#### List of scope tokens

1.
1.

### `Var` class

To manage scopes, variable types and all metadata of variable system there are following classes implemented:

![Var class diagram](./AGH%20-%20TKK.png)

### Storing stack of variable values

Every variable in Scriptorium has it's own stack. We obtain a value from the stack based on recursion level:

```python
current_value = some_var.value[recursion_level]
```

#### How it works

##### Writing

When writing new value to the stack there are only two options

1. There is a value for specified `recursion_level`:

    Value gets overwritten

    ```python
    recursion_level = 2
    # var.value -> [0, 1, 2]
    var.change_or_append_value(recursion_level, 10)
    # var.value -> [0, 1, 10]
    ```

2. There is no value for specified `recursion_level`:

    Value is appended at specified index = recursion_level. Values at indices < `recursion_level` are set to `None`

    ```python
    recursion_level = 2
    # var.value -> [15]
    var.change_or_append_value(recursion_level, 20)
    # var.value -> [15, None, 10]
    ```

##### Reading

### Detecting nearest scope

When we need to read value of a variable we use a `Var.nearest_scope_variable()` (#TODO: Add link to API) static method. It finds a variable with specified name or raise an error when there is no variable with that name.

## Variable Listener

### Variable declaration

### Declaration of `i` variable in `for` function

### Definition of function parameters

## Language Visitor

### Handling `break` and `continue` without using python keywords

### Functions and how recurrence work

### Type casting
