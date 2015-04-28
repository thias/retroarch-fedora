Name:           libretro-snes9x
Version:        1.53
Release:        2.85ceb4bf4a%{?dist}
Summary:        Libretro snes9x core

Group:          Applications/Emulators
License:        GPLv2 and LGPLv2.1
URL:            https://github.com/libretro/snes9x
Source0:        https://github.com/libretro/snes9x/archive/85ceb4bf4a.tar.gz
Source1:        https://raw.githubusercontent.com/libretro/libretro-super/master/dist/info/snes9x_libretro.info

BuildRequires:  zlib-devel
BuildRequires:  libpng-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel

%description
Libretro snes9x core.


%prep
%setup -q -n snes9x-85ceb4bf4a8e95637415b0c708e4c8ac0e86565d


%build
make -C libretro %{?_smp_mflags}


%install
install -D -m 0755 libretro/snes9x_libretro.so \
  %{buildroot}%{_libexecdir}/libretro/snes9x.so
install -p -m 0644 %{SOURCE1} \
  %{buildroot}%{_libexecdir}/libretro/snes9x.info


%files
%doc docs/*
%{_libexecdir}/libretro/


%changelog
* Sun Nov 16 2014 Matthias Saou <matthias@saou.eu> 1.53-1.85ceb4bf4a
- Set correct version.

* Sat Nov 08 2014 Matthias Saou <matthias@saou.eu> 0-0.1.e62b25975d
- Initial RPM release.

