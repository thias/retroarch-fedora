Name:           libretro-scummvm
Version:        1.7.0
Release:        1.228def6913%{?dist}
Summary:        Libretro scummvm core

Group:          Applications/Emulators
License:        GPLv2+
URL:            https://github.com/libretro/scummvm
Source0:        https://github.com/libretro/scummvm/archive/228def6913.tar.gz
Source1:        https://github.com/libretro/libretro-super/blob/master/dist/info/scummvm_libretro.info

BuildRequires:  SDL-devel
BuildRequires:  freetype-devel
BuildRequires:  nasm
BuildRequires:  readline-devel

%description
Libretro scummvm core.


%prep
%setup -q -n scummvm-228def6913594dd01770c44f6a516908877878f4


%build
make -C backends/platform/libretro/build %{?_smp_mflags}


%install
install -D -m 0755 backends/platform/libretro/build/scummvm_libretro.so \
  %{buildroot}%{_libexecdir}/libretro/scummvm.so
install -p -m 0644 %{SOURCE1} \
  %{buildroot}%{_libexecdir}/libretro/scummvm.info


%files
%doc README COPY*
%{_libexecdir}/libretro/


%changelog
* Sun Nov 16 2014 Matthias Saou <matthias@saou.eu> 1.7.0-1.228def6913
- Set correct version.

* Sat Nov 08 2014 Matthias Saou <matthias@saou.eu> 0-0.1.7dc8e24f17
- Initial RPM release.

