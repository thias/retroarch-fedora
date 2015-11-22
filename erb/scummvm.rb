require 'erb'

@name = 'scummvm'
@commit = 'c3e719acc08c1873609bab3578939b7c9e606511'
@version = '1.8.0'
@release = '0.1'
@license = 'GPLv2+'
@buildrequires = [
  'SDL-devel',
  'freetype-devel',
  'nasm',
  'readline-devel',
]
@build = [
  'make -C backends/platform/libretro/build %{?_smp_mflags}',
]
@install_lib = 'backends/platform/libretro/build/' + @name + '_libretro.so'
@doc = [
  'README COPY*',
]
@changelog = '
* Sun Nov 22 2015 Matthias Saou <matthias@saou.eu> 1.8.0-0.1.c3e719acc0
- Update to latest git code.

* Sun Nov 16 2014 Matthias Saou <matthias@saou.eu> 1.7.0-1.228def6913
- Set correct version.

* Sat Nov 08 2014 Matthias Saou <matthias@saou.eu> 0-0.1.7dc8e24f17
- Initial RPM release.
'

print ERB.new(File.read('spec.erb'),nil,'<>').result(binding)

