%global commit d89ab913ab
%global longcommit d89ab913abdd90e559e48a38a07fd571cbf8a607

Name:		emulationstation
Version:	1.0.2
Release:	1.%{commit}%{?dist}
Summary:	Graphical front-end for emulators with controller navigation

Group:		Applications/Emulators
License:        BSD and ASL 2.0 and MIT
URL:		http://emulationstation.org/
Source0:	https://github.com/Aloshi/EmulationStation/archive/%{commit}.tar.gz
Source1:        http://emulationstation.org/downloads/themes/simple_latest.zip

BuildRequires:	cmake
BuildRequires:	SDL2-devel
BuildRequires:	boost-devel
BuildRequires:	freeimage-devel
BuildRequires:	freetype-devel
BuildRequires:	eigen3-devel
BuildRequires:	curl-devel
BuildRequires:	mesa-libGL-devel

%description
Graphical front-end for emulators with controller navigation.


%prep
%setup -q -n EmulationStation-%{longcommit} -a 1


%build
%cmake .
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}/etc/emulationstation/themes
cp -a simple %{buildroot}/etc/emulationstation/themes/


%check
ctest


%files
%doc *.md opensans_license.txt
%doc external/nanosvg/nanosvg_license.txt
%doc external/pugixml/pugixml_license.txt
/etc/emulationstation
%{_bindir}/emulationstation


%changelog
* Sat Nov 08 2014 Matthias Saou <matthias@saou.eu> 1.0.2-1.d89ab913ab
- Initial RPM release.

