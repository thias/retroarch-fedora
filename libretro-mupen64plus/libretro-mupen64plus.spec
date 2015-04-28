Name:           libretro-mupen64plus
Version:        2.0
Release:        2.114ddec34a%{?dist}
Summary:        Libretro mupen64plus core

Group:          Applications/Emulators
License:        GPLv2
URL:            https://github.com/libretro/mupen64plus-libretro
Source0:        https://github.com/libretro/mupen64plus-libretro/archive/114ddec34a.tar.gz
Source1:        https://raw.githubusercontent.com/libretro/libretro-super/master/dist/info/mupen64plus_libretro.info

BuildRequires:  SDL-devel
BuildRequires:  libpng-devel
BuildRequires:  freetype-devel
BuildRequires:  zlib-devel

%description
Libretro mupen64plus core.


%prep
%setup -q -n mupen64plus-libretro-114ddec34aba8c82e10ff0d109803c5ee6591589


%build
make %{?_smp_mflags} WITH_DYNAREC=x86_64


%install
install -D -m 0755 mupen64plus_libretro.so \
  %{buildroot}%{_libexecdir}/libretro/mupen64plus.so
install -p -m 0644 %{SOURCE1} \
  %{buildroot}%{_libexecdir}/libretro/mupen64plus.info


%files
%doc mupen64plus-core/README
%{_libexecdir}/libretro/


%changelog
* Sun Nov 16 2014 Matthias Saou <matthias@saou.eu> 2.0-1.114ddec34a
- Initial RPM release.

