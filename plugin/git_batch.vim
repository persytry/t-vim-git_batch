" @author persy
" @date 2021/9/22 13:19

if exists('g:git_batch_loaded')
    finish
else
    let g:git_batch_loaded = 1
endif

function! s:InitVar(var, value)
    if !exists(a:var)
        exec 'let '.a:var.'='.string(a:value)
    endif
endfunction

command! -nargs=? GbRepo :call git_batch#py("printRepo", <args>)
command! -nargs=? GbDiff :call git_batch#py('printRepoDiff', <args>)
command! -nargs=? GbNeedPush :call git_batch#py('printRepoNeedPush', <args>)
command! -nargs=+ GbCommit :call git_batch#py('commitAll', <args>)
command! -nargs=? GbPull :call git_batch#py('pullAll', <args>)
command! -nargs=? GbPush :call git_batch#py('pushAll', <args>)
