Name:           python3-pygit2
Version:        1.16.0
Release:        1%{?dist}
Summary:        Python bindings for libgit2
License:        GPL-2.0-only WITH linking-exception
URL:            https://github.com/libgit2/pygit2
Source0:        pygit2-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  libgit2-devel >= 1.8.0
BuildRequires:  gcc
BuildRequires:  python3-cffi

%description
pygit2 is a set of Python bindings to the libgit2 shared library,
libgit2 implements the core of Git. pygit2 implements Git plumbing
and supports Python 3.11+.

%prep
%autosetup -n pygit2-%{version}

%build
%pyproject_build

%install
%pyproject_install

%files
%license COPYING
%doc README.md
%{python3_sitearch}/pygit2/
%{python3_sitearch}/pygit2-%{version}*.dist-info/

%changelog
* Fri Apr 03 2026 OpenEuler Package Import <pkg@openeuler.org> - 1.16.0-1
- Initial package
