# compat package: official has python3-python-dateutil-2.8.2
# force_compat mode: introducing 2.9.0.post0 alongside official as python3-python-dateutil-2.9
# Note: RPM version uses ^ for post-release: 2.9.0^post0
Name:           python-python-dateutil-2.9
Version:        2.9.0^post0
Release:        1%{?dist}
Summary:        Extensions to the standard Python datetime module (compat 2.9)
License:        BSD-2-Clause AND Apache-2.0
URL:            https://github.com/dateutil/dateutil
Source0:        %{pypi_source python-dateutil 2.9.0.post0}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm < 8.0
BuildRequires:  python3-six >= 1.5

%description
The dateutil module provides powerful extensions to the standard datetime module.
This is the compat package providing version 2.9.x alongside the system
python3-python-dateutil package.


%package -n python3-python-dateutil-2.9
Summary:        Extensions to the standard Python datetime module (compat 2.9)
Requires:       python3-six >= 1.5
Provides:       python3dist(python-dateutil) = 2.9.0^post0
Provides:       python-python-dateutil-2.9

%description -n python3-python-dateutil-2.9
The dateutil module provides powerful extensions to the standard datetime module.
This is the compat package providing version 2.9.x alongside the system
python3-python-dateutil package.


%package help
Summary:        Development documents for python-dateutil-2.9
Requires:       python3-python-dateutil-2.9 = %{version}-%{release}

%description help
Documentation for python-dateutil 2.9.x.


%prep
%autosetup -n python-dateutil-2.9.0.post0 -p1
# Create static _version.py for build
echo 'version = "2.9.0.post0"' > src/dateutil/_version.py

%build
%py3_build

%install
%py3_install

%files -n python3-python-dateutil-2.9
%license LICENSE
%{python3_sitelib}/dateutil/
%{python3_sitelib}/python_dateutil-2.9.0.post0*.egg-info/

%files help
%license LICENSE
%doc NEWS README.rst

%changelog
* Wed May 27 2026 Python_Bot <Python_Bot@openeuler.org> - 2.9.0^post0-1
- Initial compat package alongside system python3-python-dateutil-2.8.2
