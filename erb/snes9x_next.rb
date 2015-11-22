require 'erb'

@name = 'snes9x_next'
@urlname = 'snes9x-next'
@commit = 'dfb7eef46d6bc2dbcc98f25e2bfadc9d2cff5cfd'
@version = '1.52'
@release = '3'
@license = 'GPLv2 and LGPLv2.1'
@buildrequires = [
  'zlib-devel',
  'libpng-devel',
  'libX11-devel',
  'libXext-devel',
]
@build = [
  'make -f Makefile.libretro %{?_smp_mflags}',
]
@doc = [
  'docs/*',
]
@changelog = '
* Sun Nov 22 2015 Matthias Saou <matthias@saou.eu> 1.52-3.dfb7eef46d
- Update to latest git code.

* Sun Nov 16 2014 Matthias Saou <matthias@saou.eu> 1.52-1.d2aba49db2
- Initial RPM release.
'

print ERB.new(File.read('spec.erb'),nil,'<>').result(binding)

