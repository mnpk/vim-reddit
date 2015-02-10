if exists('b:current_syntax')
  finish
endif

syn match AlienEye /•/
highlight AlienEye ctermfg=202 guifg=#ff4500
syn match Header /http:\/\/www\.reddit\.com\/r\/.*$/
highlight Header ctermfg=153 guifg=#cee3f8

" highlight link info as a comment
syn match Comment /\d\+ points,.*$/

let b:current_syntax = 'reddit'
