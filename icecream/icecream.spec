%global srcname icecream

Name:           python3-icecream
Version:        2.2.0
Release:        1%{?dist}
Summary:        Never use print() to debug again
License:        MIT
URL:            https://github.com/gruns/icecream
Source0:        %{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  python3-wheel

Requires:       python3-colorama
Requires:       python3-pygments
Requires:       python3-executing
Requires:       python3-asttokens

%description
IceCream improves print debugging by showing expressions together with
values, pretty formatting, and contextual information.

%prep
%autosetup -n %{srcname}-%{version}

%build
%pyproject_build

%install
%pyproject_install

%files
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/icecream/
%{python3_sitelib}/icecream-%{version}*.dist-info/

%changelog
* Tue Apr 14 2026 OpenEuler Package Import <pkg@openeuler.org> - 2.2.0-1
- Initial package
