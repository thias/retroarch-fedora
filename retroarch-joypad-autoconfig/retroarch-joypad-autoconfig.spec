%global commit 7a6e3a9fec
%global longcommit 7a6e3a9fece826db540f89abcbdb57737e0f454d

Name:           retroarch-joypad-autoconfig
Version:        0
Release:        0.1.%{commit}%{?dist}
Summary:        Joypad automatic configuration data files for RetroArch

Group:          Applications/Emulators
License:        ?
URL:            http://www.libretro.com/
Source0:        https://github.com/libretro/retroarch-joypad-autoconfig/archive/%{commit}.tar.gz

Requires:       retroarch

%description
Joypad automatic configuration data files for RetroArch.

%prep
%setup -q -n retroarch-joypad-autoconfig-%{longcommit}


%build


%install
mkdir -p %{buildroot}/etc/retroarch/joypad
install -p -m 0644 udev/* %{buildroot}/etc/retroarch/joypad/


%files
%dir /etc/retroarch/
%dir /etc/retroarch/joypad/
%config(noreplace) /etc/retroarch/joypad/*.cfg


%changelog
* Sun Nov 09 2014 Matthias Saou <matthias@saou.eu> 0-0.1.7a6e3a9fec
- Initial RPM release.

