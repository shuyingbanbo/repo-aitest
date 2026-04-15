%global srcname tabulate

Name:           python3-tabulate
Version:        0.10.0
Release:        1%{?dist}
Summary:        Pretty-print tabular data
License:        MIT
URL:            https://github.com/astanin/python-tabulate
Source0:        %{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
BuildRequires:  python3-flit
BuildRequires:  python3-flit-scm

%description
Tabulate is a Python library and command-line utility for pretty-printing
small tables and other tabular data in plain text formats.

%prep
%autosetup -n %{srcname}-%{version}

%build
%pyproject_build

%install
%pyproject_install

%files
%license LICENSE
%doc README.md
%{_bindir}/tabulate
%{python3_sitelib}/tabulate/
%{python3_sitelib}/tabulate-%{version}*.dist-info/

%changelog
* Wed Apr 15 2026 OpenEuler Package Import <pkg@openeuler.org> - 0.10.0-1
- Initial package
