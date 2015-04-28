require 'erb'

@name = 'genesis_plus_gx'
@urlname = 'Genesis-Plus-GX'
@commit = 'c61817699d383072c7c6810177ddc7f5888ba65d'
@version = '1.7.4'
@release = '2'
@license = 'Non Commercial'
@buildrequires = [
  'zlib-devel',
]
@build = [
  'make -f Makefile.libretro %{?_smp_mflags}',
]
#@install_lib = 'libretro/' + @name + '_libretro.so'
@doc = [
  'HISTORY.txt LICENSE.txt README.md',
]
@changelog = '
* Sun Nov 16 2014 Matthias Saou <matthias@saou.eu> 1.7.4-1.c61817699d
- Initial RPM release.
'

print ERB.new(File.read('spec.erb'),nil,'<>').result(binding)

