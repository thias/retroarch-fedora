require 'erb'

@name = 'snes9x_next'
@urlname = 'snes9x-next'
@commit = 'd2aba49db2e027767463409d630bfa8e2a0aa0dc'
@version = '1.52'
@release = '2'
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
* Sun Nov 16 2014 Matthias Saou <matthias@saou.eu> 1.52-1.d2aba49db2
- Initial RPM release.
'

print ERB.new(File.read('spec.erb'),nil,'<>').result(binding)

