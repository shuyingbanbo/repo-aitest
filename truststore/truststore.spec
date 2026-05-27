Name:           python-truststore
Version:        0.10.4
Release:        1%{?dist}
Summary:        Utilize native system trust stores in Python
License:        MIT
URL:            https://github.com/sethmlarson/truststore
Source0:        %{pypi_source truststore}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-flit-core

%description
A Python library that uses the native system certificate stores in Python.


%package -n python3-truststore
Summary:        Utilize native system trust stores in Python
Provides:       python-truststore
Provides:       python3dist(truststore) = %{version}

%description -n python3-truststore
A Python library that uses the native system certificate stores in Python.


%package help
Summary:        Documentation for truststore
Requires:       python3-truststore = %{version}-%{release}

%description help
Documentation for truststore.


%prep
%autosetup -n truststore-%{version} -p1
# Relax flit-core version constraint (we have 3.8.0, spec requires >= 3.11)
sed -i 's/flit_core >=3.11,<4/flit_core >=3.0,<4/' pyproject.toml
# Fix license format for older setuptools
sed -i 's/^license = "MIT"$/license = {text = "MIT"}/' pyproject.toml
sed -i '/^license-files = /d' pyproject.toml

%build
%pyproject_build

%install
%pyproject_install

%files -n python3-truststore
%license LICENSE
%{python3_sitelib}/truststore/
%{python3_sitelib}/truststore-%{version}*.dist-info/

%files help
%license LICENSE
%doc README.md

%changelog
* Wed May 27 2026 Python_Bot <Python_Bot@openeuler.org> - 0.10.4-1
- Initial package
