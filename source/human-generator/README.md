### Description

A very simple graphical utility to convert bytes to IEC/SI human-readable sizes.

Mostly written to help familiarize myself with Python classes and GTK3. Please check out the comment header in the executable for more information. There's no dedicated icon, sadly. If anyone cares for this tool, I'll probably figure out how to create and add one.

If you install it via the instructions below, you'll find it in the Accessories category of the main menu in traditional desktop environments (e.g., GNOME), otherwise, you'll need to launch it manually.

### Requirements

Written for Linux.

Depends:

* Python (>= 3.6)

I'm not sure of the other dependencies, unfortunately. Gi and GTK3 come to mind. If you're on a system like Linux Mint, you likely already have what you need.

### Installation

From within the directory containing these files:

```
sudo install -m 755 -o 0 -g 0 -t /usr/local/bin human-generator
sudo desktop-file-install human-generator.desktop
```

### Files

The above instructions install the following:

* '/usr/local/bin/human-generator'
* '/usr/share/applications/human-generator'

### Contributions

If you're interested in helping, please post an Issue.

Because this repository is currently still in its early days, as far as my learning Python goes, accepting PRs would greatly interrupt my learning processes. However, Issues or Discussions on things I'm doing, or not doing, would _greatly_ help, especially if anyone winds up finding this stuff useful.
