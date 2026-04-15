%global srcname httpx

Name:           python3-httpx
Version:        0.28.1
Release:        1%{?dist}
Summary:        Next generation HTTP client for Python
License:        BSD-3-Clause AND BSD-2-Clause
URL:            https://github.com/encode/httpx
Source0:        %{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
BuildRequires:  python3-hatchling
BuildRequires:  python3-hatch-fancy-pypi-readme
BuildRequires:  python3-anyio
BuildRequires:  python3-certifi
BuildRequires:  python3-httpcore
BuildRequires:  python3-idna

%description
HTTPX is a fully featured HTTP client library for Python 3 with synchronous and
asynchronous APIs, HTTP/1.1 and HTTP/2 support, and an integrated command line
client.

%prep
%autosetup -n %{srcname}-%{version}

%build
%pyproject_build

%install
%pyproject_install

%files
%license LICENSE.md
%doc README.md
%{_bindir}/httpx
%{python3_sitelib}/httpx/
%{python3_sitelib}/httpx-%{version}*.dist-info/

%changelog
* Wed Apr 15 2026 OpenEuler Package Import <pkg@openeuler.org> - 0.28.1-1
- Initial package
