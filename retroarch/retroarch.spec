%global commit 6690711ace
%global longcommit 6690711ace3fe146d720d8755528bee8d8d87dd8
%global assets_commit e1c5f1ae32

Name:           retroarch
Version:        1.3.4
Release:        1.%{commit}%{?dist}
Summary:        Official reference frontend for libretro

Group:          Applications/Emulators
License:        GPLv3+
URL:            http://www.libretro.com/
Source0:        https://github.com/libretro/RetroArch/archive/%{commit}.tar.gz
Source1:        https://github.com/libretro/retroarch-assets/archive/%{assets_commit}.tar.gz

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
# Configuration changes
sed -i \
  's|^# libretro_directory.*|libretro_directory = "/usr/libexec/libretro"|;
   s|^# libretro_info_path.*|libretro_info_path = "/usr/libexec/libretro"|;
   s|^# menu_driver.*|menu_driver = "xmb"|;
   s|^# assets_directory.*|assets_directory = "/usr/share/retroarch/assets/"|;
   s|^# joypad_autoconfig_dir.*|joypad_autoconfig_dir = "/etc/retroarch/joypad"|' \
  %{buildroot}/etc/retroarch.cfg

mkdir -p %{buildroot}/%{_datadir}/retroarch/assets/
pushd %{buildroot}/%{_datadir}/retroarch/assets/
tar -x --gunzip --strip-components=1 -f %{SOURCE1}
popd

%files
%doc README.md
%config /etc/retroarch.cfg
%{_prefix}/bin/retroarch
%{_prefix}/bin/retroarch-cg2glsl
%{_prefix}/share/man/man1/*.1*
%{_prefix}/share/pixmaps/retroarch.*
%{_datadir}/applications/retroarch.desktop
%{_datadir}/retroarch/


%changelog
* Fri May 06 2016 Bastien Nocera <hadess@hadess.net> 1.3.4-1.6690711ace
- Update to 1.3.4.
- Default to nicer XMB menu

* Sun Nov 22 2015 Matthias Saou <matthias@saou.eu> 1.2.2-1.589b92cc99
- Update to 1.2.2.

* Wed Dec 24 2014 Matthias Saou <matthias@saou.eu> 1.0.0.3-0.2.8b41762639
- Update to latest git code.

* Sun Nov 16 2014 Matthias Saou <matthias@saou.eu> 1.0.0.3-0.1.436c0407a4
- Update and set version to what makes the most sense.

* Sat Nov 08 2014 Matthias Saou <matthias@saou.eu> 0-0.1.47b014d3cd
- Initial RPM release.

