# gothon_project

A little python app.

*Download the app (see [Use](#use), below).*

Based on Exercise 43, from [Learn Python the Hard Way](http://learnpythonthehardway.org) by Zed Shaw, with a couple of bells and whistles. First, the same app runs in either French or English. Second, we added a final interactive fight. Interactive it is as the rest of the story. A tiny story that can be completed in a few minutes, after some trials and errors. Because an error leads to a fatal epilogue... With a little patience, anyone can successfully complete the story. Although there are some code-breaking challenges, since this is a proof-of-concept, we provide the keys. However, anyone can choose to test the game. 

## Clone

- Project name: gothon_project (the parent directory).
- The project runs on Python 2. It could easily be migrated to Python 3. 
- Clone the project; on your PC, the project directory must be organized as follow.

```text
└───gothon_project
    ├───bin
    └───gothonmap
```

- The 'bin' subdir contains the script `engine.py`. The engine refers to a map or story, in the 'gothonmap' subdir to generate an interactive story. The 'tests' subdir is for testing the scripts.
- In your terminal, at the 'gothon_project' level, launch the app with `python2 bin/engine.py`.
- If the Python script fails to launch the website, you might have a path problem; you must set the path for the project to execute.
- For Linux/Mac OS X users, please execute in the terminal:

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

## Use

- Compiled with cx-Freeze (group of files).
-Zip files. Download the files. Unzip the files. Go in the folder-files and find the executable (.exe); launch it. You can simply delete folder-files.
    - [exe.win-amd64-2.7.zip](https://www.dropbox.com/s/4jitx2zjt3r576m/exe.win-amd64-2.7.zip?dl=0)
- Compiled with cx-Freeze (Windows distribution `msi`). Download the distribution file. Launch it and install the 'program' in the folder of your choice (it suggests a 'C:\...\program...' folder, but your can choose the 'desktop'). Go in the installed files and find the executable (.exe); launch it. Launch the distribution file again; this time, remove the 'program'.
    - [gothon_project-0.3-amd64.msi](https://www.dropbox.com/s/iwegfsjy41g7c0i/gothon_project-0.3-amd64.msi?dl=0)
- Compiled with pyInstaller (single-file option). Download the executable file. Launch it. You can simply delete file.
    - [engine.exe](https://www.dropbox.com/s/y4sdz8gi3xfh6x5/engine.exe?dl=0)
