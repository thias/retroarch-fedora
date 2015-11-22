Name:           libretro-snes9x_next
Version:        1.52
Release:        3.dfb7eef46d%{?dist}
Summary:        Libretro snes9x_next core

Group:          Applications/Emulators
License:        GPLv2 and LGPLv2.1
URL:            https://github.com/libretro/snes9x-next
Source0:        https://github.com/libretro/snes9x-next/archive/dfb7eef46d.tar.gz
Source1:        https://raw.githubusercontent.com/libretro/libretro-super/master/dist/info/snes9x_next_libretro.info

BuildRequires:  zlib-devel
BuildRequires:  libpng-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel

%description
Libretro snes9x_next core.


%prep
%setup -q -n snes9x-next-dfb7eef46d6bc2dbcc98f25e2bfadc9d2cff5cfd


%build
make -f Makefile.libretro %{?_smp_mflags}


%install
install -D -m 0755 snes9x_next_libretro.so \
  %{buildroot}%{_libexecdir}/libretro/snes9x_next.so
install -p -m 0644 %{SOURCE1} \
  %{buildroot}%{_libexecdir}/libretro/snes9x_next.info


%files
%doc docs/*
%{_libexecdir}/libretro/


%changelog
* Sun Nov 22 2015 Matthias Saou <matthias@saou.eu> 1.52-3.dfb7eef46d
- Update to latest git code.

* Sun Nov 16 2014 Matthias Saou <matthias@saou.eu> 1.52-1.d2aba49db2
- Initial RPM release.

