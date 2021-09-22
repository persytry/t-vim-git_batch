# -*- coding:utf-8 -*-
"""
batch operators of git
@date: 2021/9/21 19:36
@author: persy
"""
import subprocess
import os


def isInsideWorkTree(path: str = None) -> bool:
    if path is None:
        path = os.getcwd()
    else:
        path = os.path.expanduser(path)
        path = os.path.realpath(path)
        if not os.path.exists(path): return False
    return _isInsideWorkTree(path)


def hasDiff(path: str = None) -> bool:
    if path is None:
        path = os.getcwd()
    else:
        path = os.path.expanduser(path)
        path = os.path.realpath(path)
        if not os.path.exists(path): return False
    return _hasDiff(path)


def needPush(path: str = None) -> bool:
    if path is None:
        path = os.getcwd()
    else:
        path = os.path.expanduser(path)
        path = os.path.realpath(path)
        if not os.path.exists(path): return False
    return _needPush(path)


def walkRepo(path: str = None) -> str:
    if path is None:
        path = os.getcwd()
    else:
        path = os.path.expanduser(path)
        path = os.path.realpath(path)
    if _isInsideWorkTree(path):
        yield path
        return
    yield from _walkRepo(path)


def walkRepoDiff(path: str = None) -> str:
    for repo in walkRepo(path):
        if _hasDiff(repo):
            yield repo


def walkRepoNeedPush(path: str = None) -> str:
    for repo in walkRepo(path):
        if _needPush(repo):
            yield repo


def commitAll(comment: str, path: str = None) -> None:
    assert len(comment) > 0
    for repo in walkRepoDiff(path):
        subprocess.run(['git', 'commit', '-m', f'"{comment}"'], check=False, timeout=60, text=True, shell=False, cwd=repo, universal_newlines=True)


def pullAll(path: str = None) -> None:
    for repo in walkRepo(path):
        subprocess.run(['git', 'pull'], check=False, timeout=60, text=True, shell=False, cwd=repo, universal_newlines=True)


def pushAll(path: str = None) -> None:
    for repo in walkRepoNeedPush(path):
        subprocess.run(['git', 'push'], check=False, timeout=60, text=True, shell=False, cwd=repo, universal_newlines=True)


def _isInsideWorkTree(path: str) -> bool:
    res = subprocess.run(['git', 'rev-parse', '--is-inside-work-tree'], check=False, timeout=60, text=True, shell=False, cwd=path, stdout=subprocess.PIPE, universal_newlines=True, stderr=subprocess.DEVNULL)
    if res.returncode != 0: return False
    return res.stdout.strip() == 'true'


def _hasDiff(path: str) -> bool:
    res = subprocess.run(['git', 'diff', '--quiet'], check=False, timeout=60, text=True, shell=False, cwd=path, stdout=subprocess.DEVNULL, universal_newlines=True, stderr=subprocess.DEVNULL)
    return res.returncode == 1


def _needPush(path: str) -> bool:
    res = subprocess.run(['git', 'cherry', '-v'], check=False, timeout=60, text=True, shell=False, cwd=path, stdout=subprocess.PIPE, universal_newlines=True, stderr=subprocess.DEVNULL)
    if res.returncode != 0: return False
    return len(res.stdout) != 0


def _walkRepo(path: str) -> str:
    for d in os.listdir(path):
        dir = os.path.join(path, d)
        if not os.path.isdir(dir): continue
        if _isInsideWorkTree(dir):
            yield dir
            continue
        yield from _walkRepo(dir)
