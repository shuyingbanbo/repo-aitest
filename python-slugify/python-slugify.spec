%global srcname python-slugify

Name:           python3-python-slugify
Version:        8.0.4
Release:        1%{?dist}
Summary:        A Python slugify application that also handles Unicode
License:        MIT
URL:            https://github.com/un33k/python-slugify
Source0:        %{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  python3-wheel

%description
Python Slugify provides a slugify function and CLI for generating URL-friendly
slugs from Unicode text.

%prep
%autosetup -n %{srcname}-%{version}

%build
%pyproject_build

%install
%pyproject_install

%files
%license LICENSE
%doc README.md
%{_bindir}/slugify
%{python3_sitelib}/slugify/
%{python3_sitelib}/python_slugify-%{version}*.dist-info/

%changelog
* Tue Apr 14 2026 OpenEuler Package Import <pkg@openeuler.org> - 8.0.4-1
- Initial package
