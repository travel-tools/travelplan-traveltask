# Travel Task

The base structure to extend to create a [Travel](https://github.com/travel-tools/travel) Task.

This is a [Travel Plan](https://github.com/travel-tools/cookiecutter-travelplan).

Travel can download Travel Tasks from PyPi registries or use a local Travel Task provided that it is a Bag inside the current Travel project.

### Creating a Travel Task

Issue a `travel add <repo_url_of_plan or path_to_plan_folder>` command in the folder where you want to create a new Bag of a Travel Task.

For instance, to use this basic Travel Task, use:

```
travel add https://github.com/travel-tools/travelplan-traveltask.git
```

### Customizing a Travel Task

- Declare parameters that you'll reference in the Bag
- Write your Task code

#### Declare parameters

Simply add a new field in `config.py` with its type. Nested/dictionary parameters are not supported. 

Note: this type will be used in `argparse`'s `parser.add_argument` call.


`config.py`
```
from dataclasses import dataclass


@dataclass
class TaskConfig:

    # Travel parameters
    context: str
    task: str

    # Custom parameters
    example: str  # Required parameter
    another_example: int = 0  # Optional parameter
    another_param: str = None  # Optional parameter
```

#### Write your Task Code

Simply add your Task code in `task.py`, in the `perform` function.

It will receive an instance of your `TaskConfig` with all its attributes.

You are free to create nested modules to reference other functions. Just remember that Travel will run `__main__.py` with parameters read from the Bag as command line arguments.