Name:           python-litestar-htmx
Version:        0.5.0
Release:        1%{?dist}
Summary:        HTMX integration for Litestar

License:        MIT
URL:            https://github.com/litestar-org/litestar-htmx
Source0:        litestar-htmx-0.5.0.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-hatchling
BuildRequires:  python3-pip

%description
HTMX integration package for Litestar.

%prep
%autosetup -n litestar-htmx-0.5.0

%build
%pyproject_build

%install
%pyproject_install

%files
%license LICENSE
%doc README.md
%{python3_sitelib}/litestar_htmx/
%{python3_sitelib}/litestar_htmx-0.5.0.dist-info/

%changelog
* Mon Apr 27 2026 Claude - 0.5.0-1
- Initial package
