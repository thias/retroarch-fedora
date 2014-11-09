%global commit 7dc8e24f17
%global longcommit 7dc8e24f1759dfca852014451dfca9103d8b1f04

%global core_name scummvm

Name:           libretro-%{core_name}
Version:        0
Release:        0.1.%{commit}1%{?dist}
Summary:        Libretro %{core_name} core

Group:          Applications/Emulators
License:        BSD and LGPL
URL:            https://github.com/libretro/%{core_name}
Source0:        https://github.com/libretro/%{core_name}/archive/%{commit}.tar.gz
Source1:        https://github.com/libretro/libretro-super/blob/master/dist/info/scummvm_libretro.info

BuildRequires:  SDL-devel
BuildRequires:  freetype-devel
BuildRequires:  nasm
BuildRequires:  readline-devel

%description
Libretro %{core_name} core.


%prep
%setup -q -n %{core_name}-%{longcommit}


%build
make -C backends/platform/libretro/build %{?_smp_mflags}


%install
install -D -m 0755 backends/platform/libretro/build/%{core_name}_libretro.so \
  %{buildroot}%{_libexecdir}/libretro/%{core_name}.so
install -p -m 0644 %{SOURCE1} \
  %{buildroot}%{_libexecdir}/libretro/%{core_name}.info


%files
%doc README COPY*
%{_libexecdir}/libretro/


%changelog
* Sat Nov 08 2014 Matthias Saou <matthias@saou.eu> 0-0.1.7dc8e24f17
- Initial RPM release.

