%global commit c48f1784c5
%global longcommit c48f1784c56a471f3a42fbca8833305fa39daec6

Name:           emulationstation
Version:        2.0.0
Release:        0.3.rc1%{?dist}
Summary:        Graphical front-end for emulators with controller navigation

Group:          Applications/Emulators
License:        BSD and ASL 2.0 and MIT
URL:            http://emulationstation.org/
Source0:        https://github.com/Aloshi/EmulationStation/archive/%{commit}.tar.gz
Source1:        http://emulationstation.org/downloads/themes/simple_latest.zip
Source2:        emulationstation.desktop

BuildRequires:  cmake
BuildRequires:  SDL2-devel
BuildRequires:  boost-devel
BuildRequires:  freeimage-devel
BuildRequires:  freetype-devel
BuildRequires:  eigen3-devel
BuildRequires:  curl-devel
BuildRequires:  mesa-libGL-devel
# For desktop entry
BuildRequires:  ImageMagick
BuildRequires:  desktop-file-utils

%description
Graphical front-end for emulators with controller navigation.


%prep
%setup -q -n EmulationStation-%{longcommit} -a 1


%build
%cmake .
make %{?_smp_mflags}
# This will extract multiple es_icon-*.png files
convert data/es_icon.ico es_icon.png


%install
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}/etc/emulationstation/themes
cp -a simple %{buildroot}/etc/emulationstation/themes/
# Desktop entry
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE2}
for i in 16 24 32 48 64 96 128 256; do
  for j in es_icon-*.png; do
    file $j | grep "${i} x ${i}" && install -D -m 0644 $j \
      %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/emulationstation.png
  done
done

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
  /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
  /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files
%doc *.md opensans_license.txt
%doc external/nanosvg/nanosvg_license.txt
%doc external/pugixml/pugixml_license.txt
/etc/emulationstation
%{_bindir}/emulationstation
%{_datadir}/applications/emulationstation.desktop
%{_datadir}/icons/hicolor/*/apps/emulationstation.png


%changelog
* Tue Dec 23 2014 Matthias Saou <matthias@saou.eu> 2.0.0-0.3.rc1
- Update to c48f1784c5 which adds vsync.

* Sun Nov 16 2014 Matthias Saou <matthias@saou.eu> 2.0.0-0.2.rc1
- Include desktop file and hicolor icons extracted from the included .ico.

* Sat Nov 08 2014 Matthias Saou <matthias@saou.eu> 2.0.0-0.1.rc1
- Initial RPM release.

