require 'erb'

@name = 'mame'
@commit = 'a9d5a09ae9d6bfbc21450d57c07342de01a63583'
@version = '0.166'
@release = '1'
@license = 'MAME'
@buildrequires = [
  'alsa-lib-devel',
  'python',
]
@build = [
  'make -f Makefile.libretro %{?_smp_mflags}',
]
@doc = [
  'README.md',
]
@changelog = '
* Sun Nov 22 2015 Matthias Saou <matthias@saou.eu> 0.166-1.a9d5a09ae9
- Update to latest git code.
- Add missing alsa-lib-devel build requirement.

* Sun Nov 16 2014 Matthias Saou <matthias@saou.eu> 0.155-1.c7ebbc3efe
- Set correct version.

* Sat Nov 08 2014 Matthias Saou <matthias@saou.eu> 0-0.1.c7ebbc3efe
- Initial RPM release.
'

print ERB.new(File.read('spec.erb'),nil,'<>').result(binding)

