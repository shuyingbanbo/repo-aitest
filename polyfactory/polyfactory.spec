Name:           python-polyfactory
Version:        3.3.0
Release:        1%{?dist}
Summary:        Mock data generation factories
License:        MIT
URL:            https://github.com/litestar-org/polyfactory
Source0:        polyfactory-3.3.0.tar.gz
BuildArch:      noarch

BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-hatchling
BuildRequires:  python3-pip
BuildRequires:  python3-faker
BuildRequires:  python3-typing-extensions

Requires:       python3-faker >= 5.0.0
Requires:       python3-typing-extensions >= 4.6.0

%description
Mock data generation factories for use with Python dataclasses, TypedDicts,
Pydantic models, attrs, and more.

%prep
%autosetup -n polyfactory-%{version}

%build
%pyproject_build

%install
%pyproject_install

%files
%license LICENSE
%doc docs/PYPI_README.md
%{python3_sitelib}/polyfactory/
%{python3_sitelib}/polyfactory-%{version}*.dist-info/

%changelog
* Wed May 06 2026 Claude - 3.3.0-1
- Initial package
