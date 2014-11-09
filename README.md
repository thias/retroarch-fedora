# Overview

RetroArch for Fedora.

Why? Because I own an old X-Arcade (dual, serial + USB adapter, not a recent
Tankstick), and it has been gathering dust for years since I never had any
plug-n-play MAME setup ready. I gave RetroPie a go, and it seemed great up
until I starting wondering what was causing Street Fighter II to be slow and
unplayable... and read that the Raspberry Pie was just too slow (Nov 2014).

I have a powerful-ish x86_64 HTPC with an i3 processor and Intel HD4000 GPU
which can run demanding MAME games just fine, but I couldn't find a RetroPie
equivalent for x86_64. I had a quick look at RetroArch launchers for XBMC
since some can work from OpenELEC, but all seemed quite hack-ish and very
young. I tried trying GroovyArcade (ArchLinux based MAME LiveCD), but couldn't
get it to work properly. It seems to be arcade monitor oriented, with lots of
complexity in the video output area... I just want to scale the output on any
LCD display and be done with it.

Looking around some more, I didn't find any better launcher alternatives than
Emulation Station (used in RetroPie), so I stuck with that and created a nice
Fedora 20 rpm package. Scraping issues initially, but good enough nevertheless.

From there, Emulation Station can trivially launch emulators, such as upstream
mame and snes9x. Unfortunately, if you want a 100% keyboard-less experience,
you need all emulators to support binding gamepad/joystick events to exit, and
that's not possible with most of them.

This is where Libretro and RetroArch come into play : Libretro cores of mame
and snes9x exist, and the RetroArch launcher/wrapper is the one managing most
of the I/O, and includes configuration options to bind a modifier and an exit
button. So on my USB connected Super Nintendo pad, I can now press Select
and Start simultaneously to exit a game and return to Emulation Station. Yay!

I've created Fedora 20 rpm packages of RetroArch and some libretro cores
(initially only the ones I'm interested in, it's trivial to build the others).

Next I would like to create a minimal Live Fedora image which would boot into
Emulation Station fullscreen automatically. Think RetroPie for powerful PCs
in order to be able to play X-Men vs. Street Fighter :-)

Published here are all of the spec files and patches for the rpm packages, and
later maybe the kickstart file(s) for the live image.

Pull requests welcome!

# Raw Notes

```
~/.emulationstation/es_systems.cfg
retroarch -L /usr/libexec/libretro/snes9x.so
retroarch --features
retroarch --menu
rm -rf ~/.config/retroarch
```

# TODO

* Look at what useful things RetroPie does and include them : https://github.com/petrockblog/RetroPie-Setup
* Include more cores, ArchLinux PKGBUILD files are useful to know how to build (which Makefile to use, etc.) : https://aur.archlinux.org/packages/li/libretro-scummvm-git/PKGBUILD
* Find out which subprojects are useful and package them too :
** `libretro/common-shaders.git`
** `libretro/common-overlays.git`
** `libretro/retroarch-assets.git`
** `libretro/retroarch-joypad-autoconfig.git` (done, very useful!)

