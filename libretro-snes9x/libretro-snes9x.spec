%global commit e62b25975d
%global longcommit e62b25975d0c9125bfb9b476063eafe5a50065ac

%global core_name snes9x

Name:           libretro-%{core_name}
Version:        0
Release:        0.1.%{commit}1%{?dist}
Summary:        Libretro %{core_name} core

Group:          Applications/Emulators
License:        GPLv2 and LGPLv2.1
URL:            https://github.com/libretro/%{core_name}
Source0:        https://github.com/libretro/%{core_name}/archive/%{commit}.tar.gz

BuildRequires:  zlib-devel
BuildRequires:  libpng-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel

%description
Libretro %{core_name} core.


%prep
%setup -q -n %{core_name}-%{longcommit}


%build
make -C libretro %{?_smp_mflags}


%install
install -D -m 0755 libretro/%{core_name}_libretro.so \
  %{buildroot}%{_libexecdir}/libretro/%{core_name}.so


%files
%doc docs/*
%{_libexecdir}/libretro/


%changelog
* Sat Nov 08 2014 Matthias Saou <matthias@saou.eu> 0-0.1.e62b25975d
- Initial RPM release.

