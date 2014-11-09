%global commit 47b014d3cd
%global longcommit 47b014d3cdb7ce4170c85d23f4d4ed244025ef73

Name:           retroarch
Version:        0
Release:        0.1.%{commit}%{?dist}
Summary:        Official reference frontend for libretro

Group:          Applications/Emulators
License:        ?
URL:            http://www.libretro.com/
Source0:        https://github.com/libretro/RetroArch/archive/%{commit}.tar.gz

BuildRequires:  libX11-devel
BuildRequires:  libXv-devel
BuildRequires:  libxml2-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  libv4l-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  mesa-libgbm-devel
#BuildRequires:  Cg
BuildRequires:  zlib-devel
BuildRequires:  freetype-devel
#BuildRequires:  ffmpeg-devel
BuildRequires:  SDL2-devel
#Requires:

%description
RetroArch is the official reference frontend for the libretro API.
Libretro is a simple but powerful development interface that allows for the
easy creation of emulators, games and multimedia applications that can plug
straight into any libretro-compatible frontend. This development interface
is open to others so that they can run these pluggable emulator and game
cores also in their own programs or devices.


%prep
%setup -q -n RetroArch-%{longcommit}


%build
# No autotools, custom configure script
./configure --prefix=%{_prefix}
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
install -m 0755 tools/retroarch-joyconfig \
  %{buildroot}%{_prefix}/bin/retroarch-joyconfig
# Configuration changes
sed -i \
  's|^# libretro_directory.*|libretro_directory = "/usr/libexec/libretro"|;
   s|^# libretro_info_path.*|libretro_info_path = "/usr/libexec/libretro"|;
   s|^# joypad_autoconfig_dir.*|joypad_autoconfig_dir = "/etc/retroarch/joypad"|' \
  %{buildroot}/etc/retroarch.cfg


%files
%doc README.md
%config /etc/retroarch.cfg
%{_prefix}/bin/retroarch
%{_prefix}/bin/retroarch-cg2glsl
%{_prefix}/bin/retroarch-joyconfig
%{_prefix}/share/man/man1/*.1*
%{_prefix}/share/pixmaps/retroarch.*


%changelog
* Sat Nov 08 2014 Matthias Saou <matthias@saou.eu> 0-0.1.47b014d3cd
- Initial RPM release.

