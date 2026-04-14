%global srcname rich-rst

Name:           python3-rich-rst
Version:        1.3.2
Release:        1%{?dist}
Summary:        Beautiful reStructuredText renderer for Rich
License:        MIT
URL:            https://github.com/wasi-master/rich-rst
Source0:        %{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
BuildRequires:  python3-docutils
BuildRequires:  python3-rich
BuildRequires:  python3-pygments

Requires:       python3-docutils
Requires:       python3-rich
Requires:       python3-pygments

%description
rich-rst renders reStructuredText to the terminal using Rich.

%prep
%autosetup -n %{srcname}-%{version}

%build
%pyproject_build

%install
%pyproject_install

%files
%license LICENSE
%doc README.md
%{python3_sitelib}/rich_rst/
%{python3_sitelib}/rich_rst-%{version}*.dist-info/

%changelog
* Mon Apr 13 2026 OpenEuler Package Import <pkg@openeuler.org> - 1.3.2-1
- Initial package
