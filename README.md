# Travel Plan

The base structure to extend to create a [Travel](https://github.com/travel-tools/travel) Plan.

Travel Plans use [Cookiecutter](https://github.com/cookiecutter/cookiecutter) under the hood. Please, refer to their documentation.

## What is a Travel Plan

A Travel Plan is a tool to speed up the creation of new projects. A Plan refers to the template of Travel Bags.

Instead of manually creating repetitive folder structures, you can use `travel plan` to make them for you.

A Travel Plan is a repository or structure that is used by Travel to create a Bag (for instance, another Python package) with a well-known format easily.

There are plenty of public Plans to use that should cover most needs.

## How to use a Plan

You can either use several Plans at once (e.g. to create different Bags) or use a single Plan from command line, interactively.

### Several Plans at once

Once you have choosen the perfect Plans (or you have created one by yourself, as explained below), you are ready to create a `travel.yml` file and then run `travel plan <name>`, which will look for it.

In the `travel.yml` you have to specify the structure of your Bags. For instance, to create a project like this:

```
name/
  common/
  microservices/
      first/
      second/
travel.yml
```

You have to run write the following `travel.yml` and run `travel plan name` in the same folder:

```
common:
  plan: <repo_url_of_plan or path_to_plan_folder>
  config:
    ...

microservices:

  first:
    plan: <repo_url_of_plan or path_to_plan_folder>
    config:
      ...

  second:
    plan: <repo_url_of_plan or path_to_plan_folder>
    config:
      ...
```

Please refer to the documentation of the specific Plan to know how to write the relative section of `config` in the `travel.yml`.


### Single Plan from command line (interactive)

Issue a `travel add <repo_url_of_plan or path_to_plan_folder>` command in the folder where you want to create a new Bag.

This will ask you for the parameters defined in the `cookiecutter.json` file interactively.

If you *do not want interactivity*, just add all the configs after the command as specified by [Cookiecutter](https://github.com/cookiecutter/cookiecutter) docs. This command is just an alias for `cookiecutter <repo_url_of_plan or path_to_plan_folder>`.


## Creating a Travel Plan

To create a Travel Plan, you have to clone this repo. Feel free to modify it according to [Cookiecutter](https://github.com/cookiecutter/cookiecutter) docs.
