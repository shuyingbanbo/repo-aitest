%global pypi_name beanie

Name:           python-%{pypi_name}
Version:        2.1.0
Release:        1%{?dist}
Summary:        Asynchronous Python ODM for MongoDB

License:        Apache-2.0
URL:            https://github.com/BeanieODM/beanie
Source0:        %{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-flit-core

Requires:       python3-pydantic >= 2.4
Requires:       python3-click >= 7
Requires:       python3-pymongo >= 4.11.0
Requires:       python3-typing-extensions >= 4.7
Requires:       python3-lazy-model >= 0.4.0

%description
Beanie is an asynchronous Python object-document mapper (ODM) for MongoDB.
Data models are based on Pydantic.

%package -n python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3-pydantic >= 2.4
Requires:       python3-click >= 7
Requires:       python3-pymongo >= 4.11.0
Requires:       python3-typing-extensions >= 4.7
Requires:       python3-lazy-model >= 0.4.0

%description -n python3-%{pypi_name}
Beanie is an asynchronous Python object-document mapper (ODM) for MongoDB.
Data models are based on Pydantic.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%pyproject_build

%install
%pyproject_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{_bindir}/beanie
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/

%changelog
* Tue Apr 21 2026 AI Packager <ai@openeuler.org> - 2.1.0-1
- Initial package
