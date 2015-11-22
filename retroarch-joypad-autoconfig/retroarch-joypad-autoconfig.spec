%global commit b5dbd19aaf
%global longcommit b5dbd19aafbc0fcd7a5c85f745b163f14ba4914f

Name:           retroarch-joypad-autoconfig
Version:        0
Release:        0.3.%{commit}%{?dist}
Summary:        Joypad automatic configuration data files for RetroArch

Group:          Applications/Emulators
License:        ?
URL:            http://www.libretro.com/
Source0:        https://github.com/libretro/retroarch-joypad-autoconfig/archive/%{commit}.tar.gz
Patch0:         retroarch-joypad-autoconfig-exit-on-select-start.patch

BuildArch:      noarch
Requires:       retroarch

%description
Joypad automatic configuration data files for RetroArch.

%prep
%setup -q -n retroarch-joypad-autoconfig-%{longcommit}
%patch0 -p1


%build


%install
mkdir -p %{buildroot}/etc/retroarch/joypad
install -p -m 0644 udev/*.cfg %{buildroot}/etc/retroarch/joypad/


%files
%dir /etc/retroarch/
%dir /etc/retroarch/joypad/
%config(noreplace) /etc/retroarch/joypad/*.cfg


%changelog
* Sun Nov 22 2015 Matthias Saou <matthias@saou.eu> 0-0.3.b5dbd19aaf
- Update to latest git code.
- Make package noarch.

* Wed Dec 24 2014 Matthias Saou <matthias@saou.eu> 0-0.2.34af70c2bb
- Update to latest git code.

* Sun Nov 09 2014 Matthias Saou <matthias@saou.eu> 0-0.1.7a6e3a9fec
- Initial RPM release.

