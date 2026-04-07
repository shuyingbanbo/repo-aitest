Name:           python3-arpy
Version:        2.3.0
Release:        1%{?dist}
Summary:        Library for accessing ar archive files from Python
License:        BSD-2-Clause
URL:            https://github.com/viraptor/arpy
Source0:        arpy-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
arpy is a library for accessing ar archive files from Python.
It supports both GNU and BSD formats and exposes archived files
using the standard Python file interface. Works with Python >= 3.5.

%prep
%autosetup -n arpy-%{version}

%build
%pyproject_build

%install
%pyproject_install

%files
%license LICENSE
%doc README.md
%{python3_sitelib}/arpy.py
%{python3_sitelib}/__pycache__/arpy.cpython-*.pyc
%{python3_sitelib}/arpy-%{version}*.dist-info/

%changelog
* Fri Apr 03 2026 OpenEuler Package Import <pkg@openeuler.org> - 2.3.0-1
- Initial package
