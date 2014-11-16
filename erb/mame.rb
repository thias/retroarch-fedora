require 'erb'

@name = 'mame'
@commit = '5074d3c409a7475107c7734ca76fd01adba03c6c'
@version = '0.155'
@release = '1'
@license = 'MAME'
@buildrequires = [
  'python',
]
@build = [
  'make -f Makefile.libretro %{?_smp_mflags}',
]
@doc = [
  'README.md',
]
@changelog = '
* Sun Nov 16 2014 Matthias Saou <matthias@saou.eu> 0.155-1.c7ebbc3efe
- Set correct version.

* Sat Nov 08 2014 Matthias Saou <matthias@saou.eu> 0-0.1.c7ebbc3efe
- Initial RPM release.
'

print ERB.new(File.read('spec.erb'),nil,'<>').result(binding)

