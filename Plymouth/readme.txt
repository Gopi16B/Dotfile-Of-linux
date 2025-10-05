to change the background of the initial loading scripts(the starting of linux):


1) in /etc/default/grub add lines GRUB_DEFAULT='0' and GRUB_TIMEOUT_STYLE=hidden
2) in the line GRUB_CMDLINE_LINUX_DEFAULT add queit splash like 'queit splas ... .. '
3) Copy the Contents of plymouth folder to folder to /usr/share/Plymouth/themes


Done!

