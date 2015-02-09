if !has('python')
  echo 'vim-reddit requires Vim compiled with +python!'
  finish
endif

execute 'python import sys'
execute "python sys.path.append(r'" . expand("<sfile>:p:h")  . "')"
execute "python from vimreddit import vim_reddit, vim_reddit_link"

command! -nargs=1 Reddit python vim_reddit(<f-args>)

au! BufRead,BufNewFile *.reddit set filetype=reddit
