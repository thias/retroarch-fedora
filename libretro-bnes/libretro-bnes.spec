%global commit 86b2aafbda
%global longcommit 86b2aafbda5a79a33a3ca69ee5c54a8657798dab

%global core_name bnes

Name:           libretro-%{core_name}
Version:        0
Release:        0.1.%{commit}1%{?dist}
Summary:        Libretro %{core_name} core

Group:          Applications/Emulators
License:        GPLv3
URL:            https://github.com/libretro/%{core_name}-libretro
Source0:        https://github.com/libretro/%{core_name}-libretro/archive/%{commit}.tar.gz
Source1:        https://github.com/libretro/libretro-super/blob/master/dist/info/bnes_libretro.info

%description
Libretro %{core_name} core.


%prep
%setup -q -n %{core_name}-libretro-%{longcommit}


%build
make %{?_smp_mflags}


%install
install -D -m 0755 libretro.so \
  %{buildroot}%{_libexecdir}/libretro/%{core_name}.so
install -p -m 0644 %{SOURCE1} \
  %{buildroot}%{_libexecdir}/libretro/%{core_name}.info


%files
%doc README
%{_libexecdir}/libretro/


%changelog
* Sat Nov 08 2014 Matthias Saou <matthias@saou.eu> 0-0.1.86b2aafbda
- Initial RPM release.

