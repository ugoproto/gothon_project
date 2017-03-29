# gothon_project

A little python app.

Based on Exercise 43, from [Learn Python the Hard Way](http://learnpythonthehardway.org) by Zed Shaw, with a couple of bells and whistles..

- Project name: gothon_project (the parent directory).
- The project runs on Python 2.7.
- Clone the project; on your PC, the project directory must organized as follow.

```text
└───gothon_project
    ├───bin
    └───gothonmap
```

- The 'bin' subdir contains the script `engine.py`. The engine refers to a map or story, in the 'gothonmap' subdir to generate an interactive story. The 'tests' subdir is for testing the scripts.
- In your terminal, at the 'gothon_project' level, launch the app with `python2 bin/engine.py`.
- If the Python script fails to launch the website, you might have a path problem; you must set the path for the project to execute.
- For Linux/MacOSX users, please execute in the terminal:

```bash
export PYTHONPATH=$PYTHONPATH:.
```

- For Windows users, please execute in the shell:

```bash
$env:PYTHONPATH = "$env:PYTHONPATH;."
```

- Or set the path with Windows Advanced Systeme Parameters (consult the documentation for that matter).
- Then relaunch the script; `python2 bin/engine.py` works on Linux/MacOSX.
- For Windows, you might need to try `py -2 bin/engine.py` or `py -2.7 bin/engine.py`.
- Consult the Python documentation otherwise.
- Have fun!
