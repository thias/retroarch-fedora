require 'erb'

@name = 'genesis_plus_gx'
@urlname = 'Genesis-Plus-GX'
@commit = '7d8d5f1026af8cfd00cdf32c67a999bd1e454a09'
@version = '1.7.4'
@release = '3'
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

