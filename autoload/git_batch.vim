" @author persy
" @date 2021/9/22 12:36

if exists('g:git_batch#loaded')
    finish
else
    let g:git_batch#loaded = 1
endif

if has("python3") == 0
    echoe "Error: git_batch requires vim compiled with +python3"
    finish
endif

silent! exec "py3 pass"
exec "py3 import vim, sys, os, re, os.path"
exec "py3 cwd = vim.eval('expand(\"<sfile>:p:h\")')"
exec "py3 cwd = re.sub(r'(?<=^.)', ':', os.sep.join(cwd.split('/')[1:])) if os.name == 'nt' and cwd.startswith('/') else cwd"
exec "py3 sys.path.insert(0, os.path.join(cwd, 'git_batch', 'python'))"
exec "py3 import git_batch"

function! s:InitVar(var, value)
    if !exists(a:var)
        exec 'let '.a:var.'='.string(a:value)
    endif
endfunction

function! git_batch#py(fn, p1, p2) abort
    let l:s = "py3 git_batch." . a:fn . "("
    if a:p1
        let l:s = l:s . "'" . a:p1 . "'"
    endif
    if a:p2
        let l:s = l:s . ",'" . a:p2 . "'"
    endif
    let l:s = l:s . ")"
    exec l:s
endfunction
