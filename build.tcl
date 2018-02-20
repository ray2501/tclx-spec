#!/usr/bin/tclsh

set arch "x86_64"
set base "tclx8.6.0_git20180221"

set var2 [list git clone https://github.com/flightaware/tclx.git $base]
exec >@stdout 2>@stderr {*}$var2

cd tclx8.6.0_git20180221

set var2 [list git checkout 8b01a0dd5ee1bd22b6126c08bede8ee3105a50c0]
exec >@stdout 2>@stderr {*}$var2

set var2 [list git reset --hard]
exec >@stdout 2>@stderr {*}$var2

file delete -force .git

cd ..

set var2 [list tar cjvf ${base}.tar.bz2 $base]
exec >@stdout 2>@stderr {*}$var2

if {[file exists build]} {
    file delete -force build
}

file mkdir build/BUILD build/RPMS build/SOURCES build/SPECS build/SRPMS
file copy -force $base.tar.bz2 build/SOURCES

set buildit [list rpmbuild --target $arch --define "_topdir [pwd]/build" -bb tclx.spec]
exec >@stdout 2>@stderr {*}$buildit

# Remove our source code
file delete -force $base
file delete -force $base.tar.bz2

