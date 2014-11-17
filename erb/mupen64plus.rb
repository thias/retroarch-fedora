require 'erb'

@name = 'mupen64plus'
@urlname = 'mupen64plus-libretro'
@commit = '114ddec34aba8c82e10ff0d109803c5ee6591589'
@version = '2.0'
@release = '1'
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
* Sun Nov 16 2014 Matthias Saou <matthias@saou.eu> 2.0-1.114ddec34a
- Initial RPM release.
'

print ERB.new(File.read('spec.erb'),nil,'<>').result(binding)

