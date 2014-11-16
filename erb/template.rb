require 'erb'

@name = ''
#@urlname = ''
@commit = 'd2aba49db2e027767463409d630bfa8e2a0aa0dc'
@version = ''
@release = '1'
@license = ''
#@url = ''
@buildrequires = [
  'zlib-devel',
]
@build = [
  'make %{?_smp_mflags}',
]
#@install_lib = 'libretro/' + @name + '_libretro.so'
@doc = [
  'docs/*',
]
@changelog = '
* Sun Nov 16 2014 Matthias Saou <matthias@saou.eu> x
- Initial RPM release.
'

print ERB.new(File.read('spec.erb'),nil,'<>').result(binding)

