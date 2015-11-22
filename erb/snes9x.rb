require 'erb'

@name = 'snes9x'
@commit = 'ccf1ee2eae73ed1e4044c8dd9536dd4ac1be6d8b'
@version = '1.53'
@release = '3'
@license = 'GPLv2 and LGPLv2.1'
@buildrequires = [
  'zlib-devel',
  'libpng-devel',
  'libX11-devel',
  'libXext-devel',
]
@build = [
  'make -C libretro %{?_smp_mflags}',
]
@install_lib = 'libretro/' + @name + '_libretro.so'
@doc = [
  'docs/*',
]
@changelog = '
* Sun Nov 22 2015 Matthias Saou <matthias@saou.eu> 1.53-3.ccf1ee2eae
- Update to latest git code.

* Sun Nov 16 2014 Matthias Saou <matthias@saou.eu> 1.53-1.85ceb4bf4a
- Set correct version.

* Sat Nov 08 2014 Matthias Saou <matthias@saou.eu> 0-0.1.e62b25975d
- Initial RPM release.
'

print ERB.new(File.read('spec.erb'),nil,'<>').result(binding)

