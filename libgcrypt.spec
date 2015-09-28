#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libgcrypt
Version  : 1.6.2
Release  : 7
URL      : ftp://ftp.gnupg.org/gcrypt/libgcrypt/libgcrypt-1.6.2.tar.bz2
Source0  : ftp://ftp.gnupg.org/gcrypt/libgcrypt/libgcrypt-1.6.2.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.0+ GPL-2.0
Requires: libgcrypt-bin
Requires: libgcrypt-lib
Requires: libgcrypt-doc
BuildRequires : libgpg-error-dev

%description
Libgcrypt - The GNU Crypto Library
------------------------------------
Version 1.6

%package bin
Summary: bin components for the libgcrypt package.
Group: Binaries

%description bin
bin components for the libgcrypt package.


%package dev
Summary: dev components for the libgcrypt package.
Group: Development
Requires: libgcrypt-lib
Requires: libgcrypt-bin

%description dev
dev components for the libgcrypt package.


%package doc
Summary: doc components for the libgcrypt package.
Group: Documentation

%description doc
doc components for the libgcrypt package.


%package lib
Summary: lib components for the libgcrypt package.
Group: Libraries

%description lib
lib components for the libgcrypt package.


%prep
%setup -q -n libgcrypt-1.6.2

%build
%configure --disable-static
make V=1 %{?_smp_mflags}

%check
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/dumpsexp
/usr/bin/hmac256
/usr/bin/libgcrypt-config
/usr/bin/mpicalc

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/*.so
/usr/share/aclocal/*.m4

%files doc
%defattr(-,root,root,-)
%doc /usr/share/info/*
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
