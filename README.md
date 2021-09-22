# git_batch

<!-- vim-markdown-toc GFM -->

* [installation](#installation)
* [shell usage](#shell-usage)
* [commands](#commands)
  * [shell commands](#shell-commands)
  * [vim commands](#vim-commands)

<!-- vim-markdown-toc -->

some useful batch operators for git.

This is a simple little project, it's easy, so don't need any configure from now.

## installation

Using [plug.vim](https://github.com/junegunn/vim-plug):
```vim
Plug 'persytry/t-vim-git_batch', { 'dir': '~/.git_batch' }
```

Using git clone:
```bash
git clone https://github.com/persytry/t-vim-git_batch ~/.git_batch
```

## shell usage

You can use this plug with shell like this:
```bash
python ~/.git_batch/autoload/git_batch/python/git_batch.py repo
```

You can create a shell file and named 'Gb' like [this](https://github.com/persytry/lang-py-setup-dev/blob/main/os/linux/sh/Gb):
```bash
#!/bin/bash

python ~/.git_batch/autoload/git_batch/python/git_batch.py $*
```
Then, add the path of 'Gb' shell file to your system path(e.g. $PATH).

## commands

### shell commands

ps. You can execute `Gb -h` or `python ~/.git_batch/autoload/git_batch/python/git_batch.py -h` to get these shell commands.

- `repo`: print repo in the path
- `diff`: print difference repo in the path
- `needPush`: print repo which need to push to remote repo in the path
- `commit`: commit to local repo in the path. There is an option`--m`, just like `git commit -m`, which you can comment it to sign your commit.
- `pull`: pull all repo in the path
- `push`: push all repo in the path to remote repo


<span id="path">
There is an global option for all commands above, is `--path`, to specify a git work-direction. The default value is None, that's mean the git work-direction is cwd(current work direction).
</span>

### vim commands

These vim commands just like shell commands above, I just list this name of commands.

- GbRepo: one optional arg, is the [path](#path)
- GbDiff: one optional arg, is the [path](#path)
- GbNeedPush: one optional arg, is the [path](#path)
- GbCommit: two optional args, the first on is comment of git commit, the second one is the [path](#path)
- GbPull: one optional arg, is the [path](#path)
- GbPush: one optional arg, is the [path](#path)

