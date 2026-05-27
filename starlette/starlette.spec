# compat package: official has python3-starlette-0.46.1
# force_compat mode: introducing 1.0.1 alongside official as python3-starlette-1.0
Name:           python-starlette-1.0
Version:        1.0.1
Release:        1%{?dist}
Summary:        The little ASGI library that shines (compat 1.0)
License:        BSD-3-Clause
URL:            https://www.starlette.io/
Source0:        %{pypi_source starlette}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-hatchling
BuildRequires:  python3-anyio >= 3.6.2
BuildRequires:  python3-typing-extensions >= 4.10.0

%description
Starlette is a lightweight ASGI framework/toolkit for building async web services in Python.
This is the compat package providing version 1.0.x alongside the system python3-starlette package.


%package -n python3-starlette-1.0
Summary:        The little ASGI library that shines (compat 1.0)
Requires:       python3-anyio >= 3.6.2
Requires:       python3-typing-extensions >= 4.10.0
Provides:       python3dist(starlette) = %{version}
Provides:       python-starlette-1.0

%description -n python3-starlette-1.0
Starlette is a lightweight ASGI framework/toolkit for building async web services in Python.
This is the compat package providing version 1.0.x alongside the system python3-starlette package.


%package help
Summary:        Development documents for starlette-1.0
Requires:       python3-starlette-1.0 = %{version}-%{release}

%description help
Documentation for starlette 1.0.x.


%prep
%autosetup -n starlette-%{version} -p1

%build
%pyproject_build

%install
%pyproject_install

%files -n python3-starlette-1.0
%license LICENSE.md
%{python3_sitelib}/starlette/
%{python3_sitelib}/starlette-%{version}*.dist-info/

%files help
%license LICENSE.md
%doc README.md

%changelog
* Wed May 27 2026 Python_Bot <Python_Bot@openeuler.org> - 1.0.1-1
- Initial compat package alongside system python3-starlette-0.46.1
