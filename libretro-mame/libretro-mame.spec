%global commit c7ebbc3efe
%global longcommit c7ebbc3efed89ca094dae7c01ed3807ee3fd1f90

%global core_name mame

Name:           libretro-%{core_name}
Version:        0
Release:        0.1.%{commit}1%{?dist}
Summary:        Libretro %{core_name} core

Group:          Applications/Emulators
License:        MAME
URL:            https://github.com/libretro/%{core_name}
Source0:        https://github.com/libretro/%{core_name}/archive/%{commit}.tar.gz
Source1:        https://github.com/libretro/libretro-super/blob/master/dist/info/mame_libretro.info

BuildRequires:  python

%description
Libretro %{core_name} core.


%prep
%setup -q -n %{core_name}-%{longcommit}


%build
make -f Makefile.libretro %{?_smp_mflags}


%install
install -D -m 0755 %{core_name}_libretro.so \
  %{buildroot}%{_libexecdir}/libretro/%{core_name}.so
install -p -m 0644 %{SOURCE1} \
  %{buildroot}%{_libexecdir}/libretro/%{core_name}.info


%files
%doc README.md
%{_libexecdir}/libretro/


%changelog
* Sat Nov 08 2014 Matthias Saou <matthias@saou.eu> 0-0.1.c7ebbc3efe
- Initial RPM release.

