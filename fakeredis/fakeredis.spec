Name:           python-fakeredis
Version:        2.34.1
Release:        1%{?dist}
Summary:        Python implementation of redis API for testing
License:        BSD-3-Clause
URL:            https://github.com/cunla/fakeredis-py
Source0:        %{pypi_source fakeredis}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-hatchling
BuildRequires:  python3-redis < 7.2
BuildRequires:  python3-sortedcontainers >= 2
BuildRequires:  python3-typing-extensions >= 4.7

%description
A Python implementation of redis server for testing purposes.


%package -n python3-fakeredis
Summary:        Python implementation of redis API for testing
Requires:       python3-redis < 7.2
Requires:       python3-sortedcontainers >= 2
Requires:       python3-typing-extensions >= 4.7
Provides:       python-fakeredis
Provides:       python3dist(fakeredis) = %{version}

%description -n python3-fakeredis
A Python implementation of redis server for testing purposes.


%package help
Summary:        Documentation for fakeredis
Requires:       python3-fakeredis = %{version}-%{release}

%description help
Documentation for fakeredis.


%prep
%autosetup -n fakeredis-%{version} -p1

%build
%pyproject_build

%install
%pyproject_install

%files -n python3-fakeredis
%license LICENSE
%{python3_sitelib}/fakeredis/
%{python3_sitelib}/fakeredis-%{version}*.dist-info/

%files help
%license LICENSE
%doc README.md

%changelog
* Wed May 27 2026 Python_Bot <Python_Bot@openeuler.org> - 2.34.1-1
- Initial package
