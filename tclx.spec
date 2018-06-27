#
# spec file for package tclx
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           tclx
BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  tcl-devel
Version:        8.6.0_git20180628
Release:        0
Summary:        TclX - Extended Tcl
License:        SUSE-Permissive and BSD-3-Clause
Group:          Development/Languages/Tcl
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
URL:            https://github.com/flightaware/tclx
Source0:        %name%version.tar.bz2

%description 
Extended Tcl (TclX), is an extension to Tcl.

TclX provides additional interfaces to the operating system, and adds many
new programming constructs, text manipulation tools, and debugging tools.


Authors:
--------
    Karl Lehenbauer and Mark Diekhan <info@NeoSoft.com>
    TclX 8.4 work was done by Jeff Hobbs at ActiveState.

%package devel
Summary:        Development package for TclX
Group:          Development/Libraries/Tcl
Requires:       %{name} = %version

%description devel
Extended Tcl (TclX), is an extension to Tcl.

This package contains development files for TclX.    
    
%prep
%setup -q -n %{name}%{version}

%build
autoconf
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
%configure \
	--with-tcl=%_libdir \
	--with-help \
	--enable-threads
make

%install
make install DESTDIR=%buildroot pkglibdir=%tcl_archdir/%{name}8.6

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%tcl_archdir
%doc %_mandir/mann/*
%doc ChangeLog README.md

%files devel
%defattr(-,root,root)
%_prefix/include/*

%changelog
