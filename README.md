# vim-reddit

Browse [reddit](http://www.reddit.com) inside Vim!

![subreddit home](https://raw.githubusercontent.com/mnpk/vim-reddit/master/vim-reddit-home.png)

Heavily inspired (and forked) from [vim-hackernews](https://github.com/ryanss/vim-hackernews))

## usage

* Open the front page of a subreddit with the `:Reddit [subreddit]`
* Press lowercase `o` to open links in Vim
* Press uppercase `O` to open links in default web browser
* Press lowercase `u` to go back (or whatever you've remapped `undo` to)
* Press `Ctrl+r` to go forward (or whatever you're remapped `redo` to)
* Execute the `:bd` command to close and remove the reddit buffer

## installation

##### Pathogen
```bash
git clone https://github.com/joshhartigan/vim-reddit ~/.vim/bundle/vim-reddit
```

##### Vundle, vim-plug and friends
```
Plugin 'joshhartigan/vim-reddit'
```
