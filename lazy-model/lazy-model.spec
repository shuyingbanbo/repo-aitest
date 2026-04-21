%global pypi_name lazy-model
%global pypi_module lazy_model

Name:           python-%{pypi_name}
Version:        0.4.0
Release:        1%{?dist}
Summary:        Lazy parsing for Pydantic models

License:        Apache-2.0
URL:            https://github.com/BeanieODM/lazy_model
Source0:        %{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-poetry-core

Requires:       python3-pydantic >= 1.9.0

%description
Lazy parsing for Pydantic models. Provides a lazy interface for parsing
objects from dictionaries - fields are only validated when accessed.

%package -n python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3-pydantic >= 1.9.0

%description -n python3-%{pypi_name}
Lazy parsing for Pydantic models. Provides a lazy interface for parsing
objects from dictionaries - fields are only validated when accessed.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%pyproject_build

%install
%pyproject_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_module}/
%{python3_sitelib}/%{pypi_module}-%{version}.dist-info/

%changelog
* Tue Apr 21 2026 AI Packager <ai@openeuler.org> - 0.4.0-1
- Initial package
