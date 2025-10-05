#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'
PS1='[\u@\h \W]\$ '
export PATH=/home/dibash/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/bin:/usr/bin/site_perl:/usr/bin/vendor_perl:/usr/bin/core_perl
export PATH="$HOME/bin:$PATH"
export PATH="$HOME/bin:$PATH"

fastfetch --logo /home/dibash/.config/fastfetch/ascii.txt --logo-color-1 red --logo-color-2 black --color red
