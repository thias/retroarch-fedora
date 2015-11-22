require 'erb'

@name = 'mupen64plus'
@urlname = 'mupen64plus-libretro'
@commit = '7db9296453629a44de806589f3ff64e824e775ad'
@version = '2.0'
@release = '3'
@license = 'GPLv2'
@buildrequires = [
  'SDL-devel',
  'libpng-devel',
  'freetype-devel',
  'zlib-devel',
]
@build = [
  'make %{?_smp_mflags} WITH_DYNAREC=x86_64',
]
@doc = [
  'mupen64plus-core/README',
]
@changelog = '
* Sun Nov 22 2015 Matthias Saou <matthias@saou.eu> 2.0-1.7db9296453
- Update to latest git code.

* Sun Nov 16 2014 Matthias Saou <matthias@saou.eu> 2.0-1.114ddec34a
- Initial RPM release.
'

print ERB.new(File.read('spec.erb'),nil,'<>').result(binding)

