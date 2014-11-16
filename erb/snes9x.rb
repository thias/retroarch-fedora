require 'erb'

@name = 'snes9x'
@commit = '85ceb4bf4a8e95637415b0c708e4c8ac0e86565d'
@version = '1.53'
@release = '1'
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
* Sun Nov 16 2014 Matthias Saou <matthias@saou.eu> 1.53-1.85ceb4bf4a
- Set correct version.

* Sat Nov 08 2014 Matthias Saou <matthias@saou.eu> 0-0.1.e62b25975d
- Initial RPM release.
'

print ERB.new(File.read('spec.erb'),nil,'<>').result(binding)

