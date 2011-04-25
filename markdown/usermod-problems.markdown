Be Careful With usermod

For my CS project, I had to add myself and my partner to a group on my Linux
box. So, being the UNIX noob that I am, I added us to the group with

`usermod -G project1 dan`

`usermod -G project1 zhehao`

I did not realize that doing so would also remove me from all other groups,
including the admin group. This was obviously a problem, because the next time
I logged in, I found that I was no longer able to use sudo. This of course,
freaked me out. The only way I was able to fix the problem was to boot up from
a Knoppix live USB, mount my hard drive, and manually edit the /etc/sudoers
file. I later found from reading the man pages that this could all have been
avoided if I had used the `-a` flag, which appends groups to the list. If
you are reading this, don't repeat my mistake, always use `usermod -aG user`
when adding users to groups.