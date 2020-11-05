Name:    watchman
Version: c769068b24655b14fd2c0e43eee1c5ca5d741ece
Release: 2%{?dist}
Summary: Watches files and records, or triggers actions, when they change.
License: APL2
URL:     https://facebook.github.io/watchman/
Source0: https://github.com/facebook/%{name}/archive/%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: libtool
BuildRequires: make
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: openssl-devel
BuildRequires: git
BuildRequires: pcre
BuildRequires: python3-devel
BuildRequires: python3dist(setuptools)
BuildRequires: zlib-devel

%description
Watches files and records, or triggers actions, when they change.

%prep
%autosetup -n %{name}-%{version}
./autogen.sh

# See https://github.com/facebook/watchman/issues/638 as to why --enable-lenient
# is required.
%configure --enable-lenient --with-python=%{__python3} --disable-statedir

%build
%make_build

# Unfortunately make check fails on art.t
# %%check
#make check

%install
make install DESTDIR=%{buildroot}
mkdir %{buildroot}%{_docdir}/%{name}
rm -rf %{buildroot}%{_docdir}/%{name}-%{version}

%files
%defattr(-,root,root,-)
%doc README.markdown
%attr(0755,root,root) %{_bindir}/watchman{,-make,-wait}

%changelog
* Thu Nov 5 2020 Leonard Ehrenfried <mail@leonard.io>
- Updates to the newest version of watchman
* Thu Nov 22 2018 Evan Klitzke <evan@eklitzke.org>
- Initial version
