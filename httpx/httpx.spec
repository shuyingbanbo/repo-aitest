# compat package: official has python3-httpx-0.27.0
# force_compat mode: introducing 0.28.1 alongside official as python3-httpx-0.28
# Fix: remove httpcore wildcard from METADATA to avoid RPM illegal char error
Name:           python-httpx-0.28
Version:        0.28.1
Release:        1%{?dist}
Summary:        The next generation HTTP client (compat version 0.28)
License:        BSD-3-Clause
URL:            https://www.python-httpx.org/
Source0:        %{pypi_source httpx}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-hatchling
BuildRequires:  python3-hatch-fancy-pypi-readme
BuildRequires:  python3-certifi
BuildRequires:  python3-httpcore
BuildRequires:  python3-anyio
BuildRequires:  python3-idna

%description
HTTPX is a fully featured HTTP client for Python 3, which provides sync
and async APIs, and support for both HTTP/1.1 and HTTP/2.

This is the compat package providing version 0.28.x alongside the system
python3-httpx package.


%package -n python3-httpx-0.28
Summary:        The next generation HTTP client (compat version 0.28)
Requires:       python3-certifi
Requires:       python3-httpcore
Requires:       python3-anyio
Requires:       python3-idna
Provides:       python3dist(httpx) = %{version}
Provides:       python-httpx-0.28

%description -n python3-httpx-0.28
HTTPX is a fully featured HTTP client for Python 3, which provides sync
and async APIs, and support for both HTTP/1.1 and HTTP/2.

This is the compat package providing version 0.28.x alongside the system
python3-httpx package.


%package help
Summary:        Development documents and examples for httpx-0.28
Requires:       python3-httpx-0.28 = %{version}-%{release}

%description help
Documentation and examples for httpx 0.28.x.


%prep
%autosetup -n httpx-%{version} -p1

%build
%pyproject_build

%install
%pyproject_install
# Remove httpcore wildcard constraint from dist-info/METADATA to avoid
# 'Illegal char * in 1.*' RPM build error from pythondistdeps.py
find %{buildroot}%{python3_sitelib} -name "METADATA" -path "*/httpx*" | xargs -r sed -i '/^Requires-Dist: httpcore/d'

%files -n python3-httpx-0.28
%license LICENSE.md
%{python3_sitelib}/httpx/
%{python3_sitelib}/httpx-%{version}*.dist-info/
%{_bindir}/httpx

%files help
%license LICENSE.md
%doc README.md CHANGELOG.md

%changelog
* Wed May 27 2026 Python_Bot <Python_Bot@openeuler.org> - 0.28.1-1
- Initial compat package alongside system python3-httpx-0.27.0
- Remove httpcore Requires-Dist wildcard from METADATA to avoid RPM illegal char error
