#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libogg
Version  : 1.3.2
Release  : 10
URL      : http://downloads.xiph.org/releases/ogg/libogg-1.3.2.tar.xz
Source0  : http://downloads.xiph.org/releases/ogg/libogg-1.3.2.tar.xz
Summary  : Ogg Bitstream Library Development
Group    : Development/Tools
License  : BSD-3-Clause
Requires: libogg-lib
Requires: libogg-doc
BuildRequires : llvm-dev
Patch1: fmv.patch

%description
Libogg is a library for manipulating ogg bitstreams.  It handles
both making ogg bitstreams and getting packets from ogg bitstreams.

%package dev
Summary: dev components for the libogg package.
Group: Development
Requires: libogg-lib
Provides: libogg-devel

%description dev
dev components for the libogg package.


%package doc
Summary: doc components for the libogg package.
Group: Documentation

%description doc
doc components for the libogg package.


%package lib
Summary: lib components for the libogg package.
Group: Libraries

%description lib
lib components for the libogg package.


%prep
%setup -q -n libogg-1.3.2
%patch1 -p1

%build
export LANG=C
export CC=clang
export CXX=clang++
export LD=ld.gold
export CFLAGS="-g -O3 -feliminate-unused-debug-types  -pipe -Wall -D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wformat -Wformat-security -Wl,--copy-dt-needed-entries -m64 -march=westmere  -mtune=native -fasynchronous-unwind-tables -D_REENTRANT  -Wl,-z -Wl,now -Wl,-z -Wl,relro "
export CXXFLAGS=$CFLAGS
unset LDFLAGS
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -flto "
export FCFLAGS="$CFLAGS -O3 -flto "
export FFLAGS="$CFLAGS -O3 -flto "
export CXXFLAGS="$CXXFLAGS -O3 -flto "
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/ogg/config_types.h
/usr/include/ogg/ogg.h
/usr/include/ogg/os_types.h
/usr/lib64/libogg.so
/usr/lib64/pkgconfig/ogg.pc
/usr/share/aclocal/*.m4

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/libogg/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libogg.so.0
/usr/lib64/libogg.so.0.8.2
