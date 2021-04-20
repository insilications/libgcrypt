#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x528897B826403ADA
#
Name     : libgcrypt
Version  : 1.9.3
Release  : 43
URL      : https://gnupg.org/ftp/gcrypt/libgcrypt/libgcrypt-1.9.3.tar.gz
Source0  : https://gnupg.org/ftp/gcrypt/libgcrypt/libgcrypt-1.9.3.tar.gz
Source1  : https://gnupg.org/ftp/gcrypt/libgcrypt/libgcrypt-1.9.3.tar.gz.sig
Summary  : General purpose cryptographic library
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 LGPL-2.0+ LGPL-2.1
Requires: libgcrypt-bin = %{version}-%{release}
Requires: libgcrypt-info = %{version}-%{release}
Requires: libgcrypt-lib = %{version}-%{release}
Requires: libgcrypt-license = %{version}-%{release}
Requires: libgcrypt-man = %{version}-%{release}
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : libgpg-error-dev
BuildRequires : libgpg-error-dev32
BuildRequires : libgpg-error-extras
Patch1: 0001-Specify-O3-for-func-attribute-override.patch

%description
Libgcrypt - The GNU Crypto Library
------------------------------------
Version 1.9

%package bin
Summary: bin components for the libgcrypt package.
Group: Binaries
Requires: libgcrypt-license = %{version}-%{release}

%description bin
bin components for the libgcrypt package.


%package dev
Summary: dev components for the libgcrypt package.
Group: Development
Requires: libgcrypt-lib = %{version}-%{release}
Requires: libgcrypt-bin = %{version}-%{release}
Provides: libgcrypt-devel = %{version}-%{release}
Requires: libgcrypt = %{version}-%{release}

%description dev
dev components for the libgcrypt package.


%package dev32
Summary: dev32 components for the libgcrypt package.
Group: Default
Requires: libgcrypt-lib32 = %{version}-%{release}
Requires: libgcrypt-bin = %{version}-%{release}
Requires: libgcrypt-dev = %{version}-%{release}

%description dev32
dev32 components for the libgcrypt package.


%package info
Summary: info components for the libgcrypt package.
Group: Default

%description info
info components for the libgcrypt package.


%package lib
Summary: lib components for the libgcrypt package.
Group: Libraries
Requires: libgcrypt-license = %{version}-%{release}

%description lib
lib components for the libgcrypt package.


%package lib32
Summary: lib32 components for the libgcrypt package.
Group: Default
Requires: libgcrypt-license = %{version}-%{release}

%description lib32
lib32 components for the libgcrypt package.


%package license
Summary: license components for the libgcrypt package.
Group: Default

%description license
license components for the libgcrypt package.


%package man
Summary: man components for the libgcrypt package.
Group: Default

%description man
man components for the libgcrypt package.


%prep
%setup -q -n libgcrypt-1.9.3
cd %{_builddir}/libgcrypt-1.9.3
%patch1 -p1
pushd ..
cp -a libgcrypt-1.9.3 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1618895243
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition -fstack-protector-strong -mzero-caller-saved-regs=used "
%configure --disable-static --enable-ciphers="cast5 aes twofish serpent rfc2268 seed camellia idea salsa20 gost28147 chacha20 des" --disable-large-data-tests \
--disable-O-flag-munging
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static --enable-ciphers="cast5 aes twofish serpent rfc2268 seed camellia idea salsa20 gost28147 chacha20 des" --disable-large-data-tests \
--disable-O-flag-munging   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%install
export SOURCE_DATE_EPOCH=1618895243
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libgcrypt
cp %{_builddir}/libgcrypt-1.9.3/COPYING %{buildroot}/usr/share/package-licenses/libgcrypt/dfac199a7539a404407098a2541b9482279f690d
cp %{_builddir}/libgcrypt-1.9.3/COPYING.LIB %{buildroot}/usr/share/package-licenses/libgcrypt/0bf81afbc585fd8fa3a9267d33498831f5a5c9c2
cp %{_builddir}/libgcrypt-1.9.3/LICENSES %{buildroot}/usr/share/package-licenses/libgcrypt/d4e3e69a49ec2136aeeec403b8647c8d23bd2349
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
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
/usr/include/gcrypt.h
/usr/lib64/libgcrypt.so
/usr/lib64/pkgconfig/libgcrypt.pc
/usr/share/aclocal/*.m4

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libgcrypt.so
/usr/lib32/pkgconfig/32libgcrypt.pc
/usr/lib32/pkgconfig/libgcrypt.pc

%files info
%defattr(0644,root,root,0755)
/usr/share/info/gcrypt.info
/usr/share/info/gcrypt.info-1
/usr/share/info/gcrypt.info-2

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgcrypt.so.20
/usr/lib64/libgcrypt.so.20.3.3

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libgcrypt.so.20
/usr/lib32/libgcrypt.so.20.3.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libgcrypt/0bf81afbc585fd8fa3a9267d33498831f5a5c9c2
/usr/share/package-licenses/libgcrypt/d4e3e69a49ec2136aeeec403b8647c8d23bd2349
/usr/share/package-licenses/libgcrypt/dfac199a7539a404407098a2541b9482279f690d

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/hmac256.1
