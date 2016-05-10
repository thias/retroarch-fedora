Name:           libretro-dolphin
Version:        4.0.2
Release:        1.8ae5c44696%{?dist}
Summary:        Libretro dolphin core

Group:          Applications/Emulators
License:        GPLv2+
URL:            https://github.com/libretro/dolphin
Source0:        https://github.com/libretro/dolphin/archive/8ae5c44696.tar.gz
Source1:        https://raw.githubusercontent.com/libretro/libretro-super/master/dist/info/dolphin_libretro.info

BuildRequires:  SDL-devel
BuildRequires:  SFML-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  bluez-libs-devel
BuildRequires:  cmake
BuildRequires:  enet-devel
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  gtk2-devel
BuildRequires:  libao-devel
BuildRequires:  libX11-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libpng-devel
BuildRequires:  libusb-devel
BuildRequires:  lzo-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  miniupnpc-devel
BuildRequires:  openal-soft-devel
BuildRequires:  polarssl-devel
BuildRequires:  portaudio-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  soundtouch-devel
BuildRequires:  wxGTK-devel
BuildRequires:  zlib-devel

%description
Libretro dolphin core.


%prep
%setup -q -n dolphin-8ae5c4469693db6eeef13b73ae361c98f06be1d0


%build
make -C libretro %{?_smp_mflags}


%install
install -D -m 0755 libretro/dolphin_libretro.so \
  %{buildroot}%{_libexecdir}/libretro/dolphin.so
install -p -m 0644 %{SOURCE1} \
  %{buildroot}%{_libexecdir}/libretro/dolphin.info


%files
%doc docs/*
%{_libexecdir}/libretro/


%changelog
* Mon May  9 2016 Matthias Saou <matthias@saou.eu> 4.0.2-2
- Update to latest git code.

* Sun Nov 22 2015 Matthias Saou <matthias@saou.eu> 4.0.2-1
- Initial RPM release.

