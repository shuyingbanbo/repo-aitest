Name:           python-multipart
Version:        1.3.1
Release:        1%{?dist}
Summary:        Parser for multipart/form-data

License:        MIT
URL:            https://github.com/defnull/multipart
Source0:        multipart-1.3.1.tar.gz
BuildArch:      noarch

Provides:       python3-multipart = %{version}-%{release}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-flit

%description
Parser for multipart/form-data.

%prep
%autosetup -n multipart-%{version}

%build
%pyproject_build

%install
%pyproject_install

%files
%license LICENSE
%doc README.rst CHANGELOG.rst MAINTAINERS.rst
%{python3_sitelib}/multipart.py
%{python3_sitelib}/__pycache__/multipart.cpython-*.pyc
%{python3_sitelib}/multipart-1.3.1.dist-info/

%changelog
* Wed May 06 2026 Claude - 1.3.1-1
- Initial package
