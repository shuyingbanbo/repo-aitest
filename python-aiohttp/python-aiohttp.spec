Name:           python-aiohttp
Version:        3.9.1
Release:        1%{?dist}
Summary:        Async http client/server framework (asyncio)
License:        Apache-2.0
URL:            https://github.com/aio-libs/aiohttp
Source0:        python-aiohttp-3.9.1.tar.gz

%description
Async http client/server framework (asyncio).
Supports both client and server side of HTTP protocol.
Supports both client and server Web-Sockets out-of-the-box.
Provides Web-server with middleware and pluggable routing.


%package -n python3-aiohttp
Summary:        Async http client/server framework (asyncio)
Provides:       python-aiohttp
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  gcc
BuildRequires:  python3-Cython

%description -n python3-aiohttp
Async http client/server framework (asyncio).
Supports both client and server side of HTTP protocol.
Supports both client and server Web-Sockets out-of-the-box.
Provides Web-server with middleware and pluggable routing.


%prep
%autosetup -n python-aiohttp-%{version}

%build
%define _lto_cflags %{nil}
%undefine _hardened_build
%py3_build

%install
%py3_install

%files -n python3-aiohttp
%license LICENSE.txt
%doc README.rst CHANGES.rst
%{python3_sitearch}/aiohttp/
%{python3_sitearch}/aiohttp-%{version}*.egg-info/

%changelog
* Thu May 07 2026 Python_Bot <Python_Bot@openeuler.org> - 3.9.1-1
- Initial package
