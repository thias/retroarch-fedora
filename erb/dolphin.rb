require 'erb'

@name = 'dolphin'
@commit = '8ae5c4469693db6eeef13b73ae361c98f06be1d0'
@version = '4.0.2'
@release = '1'
@license = 'GPLv2+'
@buildrequires = [
  'SDL-devel',
  'SFML-devel',
  'alsa-lib-devel',
  'bluez-libs-devel',
  'cmake',
  'enet-devel',
  'gdk-pixbuf2-devel',
  'gtk2-devel',
  'libao-devel',
  'libX11-devel',
  'libXrandr-devel',
  'libpng-devel',
  'libusb-devel',
  'lzo-devel',
  'mesa-libGL-devel',
  'miniupnpc-devel',
  'openal-soft-devel',
  'polarssl-devel',
  'portaudio-devel',
  'pulseaudio-libs-devel',
  'soundtouch-devel',
  'wxGTK-devel',
  'zlib-devel',
]
@build = [
  'make -C libretro %{?_smp_mflags}',
]
@install_lib = 'libretro/' + @name + '_libretro.so'
@doc = [
  'docs/*',
]
@changelog = '
* Mon May  9 2016 Matthias Saou <matthias@saou.eu> 4.0.2-2
- Update to latest git code.

* Sun Nov 22 2015 Matthias Saou <matthias@saou.eu> 4.0.2-1
- Initial RPM release.
'

print ERB.new(File.read('spec.erb'),nil,'<>').result(binding)

