" LIN
" lin's vimrc, just putting stuff in here when i find it useful

" Theme
colo noctu
syntax on

" Line numbers
set number
set relativenumber

" Encoding
set encoding=utf-8
set fileencoding=utf-8

" Plugin
call plug#begin('~/.vim/plugged')

	" Smooth scrolling
	Plug 'psliwka/vim-smoothie'

call plug#end()

" Misc.
set nocompatible
