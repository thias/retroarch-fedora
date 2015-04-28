Name:           libretro-mame
Version:        0.155
Release:        2.5074d3c409%{?dist}
Summary:        Libretro mame core

Group:          Applications/Emulators
License:        MAME
URL:            https://github.com/libretro/mame
Source0:        https://github.com/libretro/mame/archive/5074d3c409.tar.gz
Source1:        https://raw.githubusercontent.com/libretro/libretro-super/master/dist/info/mame_libretro.info

BuildRequires:  python

%description
Libretro mame core.


%prep
%setup -q -n mame-5074d3c409a7475107c7734ca76fd01adba03c6c


%build
make -f Makefile.libretro %{?_smp_mflags}


%install
install -D -m 0755 mame_libretro.so \
  %{buildroot}%{_libexecdir}/libretro/mame.so
install -p -m 0644 %{SOURCE1} \
  %{buildroot}%{_libexecdir}/libretro/mame.info


%files
%doc README.md
%{_libexecdir}/libretro/


%changelog
* Sun Nov 16 2014 Matthias Saou <matthias@saou.eu> 0.155-1.c7ebbc3efe
- Set correct version.

* Sat Nov 08 2014 Matthias Saou <matthias@saou.eu> 0-0.1.c7ebbc3efe
- Initial RPM release.

