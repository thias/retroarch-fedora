Name:           libretro-genesis_plus_gx
Version:        1.7.4
Release:        1.c61817699d%{?dist}
Summary:        Libretro genesis_plus_gx core

Group:          Applications/Emulators
License:        Non Commercial
URL:            https://github.com/libretro/Genesis-Plus-GX
Source0:        https://github.com/libretro/Genesis-Plus-GX/archive/c61817699d.tar.gz
Source1:        https://github.com/libretro/libretro-super/blob/master/dist/info/genesis_plus_gx_libretro.info

BuildRequires:  zlib-devel

%description
Libretro genesis_plus_gx core.


%prep
%setup -q -n Genesis-Plus-GX-c61817699d383072c7c6810177ddc7f5888ba65d


%build
make -f Makefile.libretro %{?_smp_mflags}


%install
install -D -m 0755 genesis_plus_gx_libretro.so \
  %{buildroot}%{_libexecdir}/libretro/genesis_plus_gx.so
install -p -m 0644 %{SOURCE1} \
  %{buildroot}%{_libexecdir}/libretro/genesis_plus_gx.info


%files
%doc HISTORY.txt LICENSE.txt README.md
%{_libexecdir}/libretro/


%changelog
* Sun Nov 16 2014 Matthias Saou <matthias@saou.eu> 1.7.4-1.c61817699d
- Initial RPM release.

