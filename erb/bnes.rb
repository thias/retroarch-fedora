require 'erb'

@name = 'bnes'
@urlname = 'bnes-libretro'
@commit = '0e30b99baf08fe40162d71097249e84a0c6c7c21'
@version = '1'
@release = '3'
@license = 'GPLv3'
#@url = ''
@buildrequires = []
@build = [
  'make %{?_smp_mflags}',
]
@install_lib = 'libretro.so'
@doc = [
  'README',
]
@changelog = '
* Sun Nov 16 2014 Matthias Saou <matthias@saou.eu> 1-1.86b2aafbda
- Set correct version.

* Sat Nov 08 2014 Matthias Saou <matthias@saou.eu> 0-0.1.86b2aafbda
- Initial RPM release.
'

print ERB.new(File.read('spec.erb'),nil,'<>').result(binding)

