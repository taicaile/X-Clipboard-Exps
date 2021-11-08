# README

Usage,

```bash
./xclip.py
```

This script removes the prefix `x-special/nautilus-clipboard` given by `Nautilus` on Gnome Desktop when a user copy file from desktop.

For example, then the following text is copied to clipboard when a user copy `/home/li/Pictures` directory,

```text
x-special/nautilus-clipboard
copy
file:///home/li/Pictures
```

This script will convert it to,

```text
/home/li/Pictures
```

Updates:

- It looks that the Nautilus have fixed this bug in some cases (It is still problematic if a user copy file from desktop directly). Tested on `GNOME nautilus 3.36.3`.
