Name:           python-rich-click
Version:        1.8.8
Release:        1%{?dist}
Summary:        Format click help output nicely with rich

License:        MIT
URL:            https://github.com/ewels/rich-click
Source0:        rich-click-1.8.8.tar.gz
BuildArch:      noarch

Provides:       python3-rich-click = %{version}-%{release}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-click
BuildRequires:  python3-rich
BuildRequires:  python3-typing-extensions

Requires:       python3-click >= 7
Requires:       python3-rich >= 10.7
Requires:       python3-typing-extensions >= 4

%description
Format click help output nicely with rich.

%prep
%autosetup -n rich-click-%{version}

%build
%pyproject_build

%install
%pyproject_install

%files
%license LICENSE
%doc README.md
%{_bindir}/rich-click
%{python3_sitelib}/rich_click/
%{python3_sitelib}/rich_click-%{version}*.dist-info/

%changelog
* Wed May 06 2026 Claude - 1.8.8-1
- Initial package
