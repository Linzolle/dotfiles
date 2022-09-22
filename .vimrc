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

" Remapping

" for navigating splits easier
nnoremap <C-J> <C-W>j
nnoremap <C-K> <C-W>k
nnoremap <C-H> <C-W>h
nnoremap <C-L> <C-W>l

" Plugin
call plug#begin('~/.vim/plugged')

	" Smooth scrolling
	Plug 'psliwka/vim-smoothie'
	Plug 'ctrlpvim/ctrlp.vim'

call plug#end()

" Misc.
set nocompatible

set tabstop=4
set shiftwidth=4
