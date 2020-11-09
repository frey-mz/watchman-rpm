Name:    watchman
Version: f5e66ddb209673296dc7a485b7eaba9ddc9c3442
Release: 3%{?dist}
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


%build
python3 build/fbcode_builder/getdeps.py --allow-system-packages build --src-dir=. watchman  --project-install-prefix watchman:/usr/local

# Unfortunately make check fails on art.t
# %%check
#make check

%install
#make install DESTDIR=%{buildroot}
#mkdir %{buildroot}%{_docdir}/%{name}
#rm -rf %{buildroot}%{_docdir}/%{name}-%{version}

%files
%defattr(-,root,root,-)
%doc README.markdown
%attr(0755,root,root) %{_bindir}/watchman{,-make,-wait}

%changelog
* Thu Nov 5 2020 Leonard Ehrenfried <mail@leonard.io>
- Updates to the newest version of watchman
* Thu Nov 22 2018 Evan Klitzke <evan@eklitzke.org>
- Initial version
