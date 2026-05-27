# compat package: official has python3-trio-0.25.1
# force_compat mode: introducing 0.29.0 alongside official as python3-trio-0.29
# Uses pyproject.toml with setuptools backend and dynamic version from src layout
Name:           python-trio-0.29
Version:        0.29.0
Release:        1%{?dist}
Summary:        A friendly Python library for async concurrency and I/O (compat 0.29)
License:        MIT OR Apache-2.0
URL:            https://trio.readthedocs.io/
Source0:        %{pypi_source trio}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-setuptools >= 64
BuildRequires:  python3-attrs >= 23.2.0
BuildRequires:  python3-sortedcontainers
BuildRequires:  python3-idna
BuildRequires:  python3-outcome
BuildRequires:  python3-sniffio >= 1.3.0
BuildRequires:  python3-cffi >= 1.14
BuildRequires:  python3-exceptiongroup
BuildRequires:  python3-wheel

%description
Trio is a Python library for writing async code using modern Python features.
This is the compat package providing version 0.29.x alongside the system
python3-trio package.


%package -n python3-trio-0.29
Summary:        A friendly Python library for async concurrency and I/O (compat 0.29)
Requires:       python3-attrs >= 23.2.0
Requires:       python3-sortedcontainers
Requires:       python3-idna
Requires:       python3-outcome
Requires:       python3-sniffio >= 1.3.0
Requires:       python3-exceptiongroup
Provides:       python3dist(trio) = %{version}
Provides:       python-trio-0.29

%description -n python3-trio-0.29
Trio is a Python library for writing async code using modern Python features.
This is the compat package providing version 0.29.x alongside the system
python3-trio package.


%package help
Summary:        Development documents and examples for trio-0.29
Requires:       python3-trio-0.29 = %{version}-%{release}

%description help
Documentation for trio 0.29.x.


%prep
%autosetup -n trio-%{version} -p1

%build
%pyproject_build

%install
%pyproject_install

%files -n python3-trio-0.29
%license LICENSE LICENSE.MIT LICENSE.APACHE2
%{python3_sitelib}/trio/
%{python3_sitelib}/trio-%{version}*.dist-info/

%files help
%license LICENSE LICENSE.MIT LICENSE.APACHE2
%doc README.rst

%changelog
* Wed May 27 2026 Python_Bot <Python_Bot@openeuler.org> - 0.29.0-1
- Initial compat package alongside system python3-trio-0.25.1
- Use pyproject_build (no setup.py in 0.29.0)
