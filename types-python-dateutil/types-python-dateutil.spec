# compat package: official has python3-types-python-dateutil 2.8.19.20240106
# force_compat: introducing 2.9.0.20260518 as python3-types-python-dateutil-2.9
Name:           python-types-python-dateutil-2.9
Version:        2.9.0.20260518
Release:        1%{?dist}
Summary:        Typing stubs for python-dateutil (compat 2.9)
License:        Apache-2.0
URL:            https://github.com/python/typeshed
Source0:        %{pypi_source types-python-dateutil 2.9.0.20260518}
BuildArch:      noarch

BuildRequires:  python3-devel

%description
Typing stubs for python-dateutil (compat 2.9.x).


%package -n python3-types-python-dateutil-2.9
Summary:        Typing stubs for python-dateutil (compat 2.9)
Provides:       python3dist(types-python-dateutil) = %{version}
Provides:       python-types-python-dateutil-2.9

%description -n python3-types-python-dateutil-2.9
Typing stubs for python-dateutil (compat 2.9.x).


%prep
%autosetup -n types-python-dateutil-%{version} -p1

%build
# Pure stub package - no compilation needed

%install
mkdir -p %{buildroot}%{python3_sitelib}/dateutil-stubs
cp -r dateutil-stubs/* %{buildroot}%{python3_sitelib}/dateutil-stubs/
mkdir -p %{buildroot}%{python3_sitelib}/types_python_dateutil-%{version}.dist-info
cat > %{buildroot}%{python3_sitelib}/types_python_dateutil-%{version}.dist-info/METADATA << 'METAEOF'
Metadata-Version: 2.4
Name: types-python-dateutil
Version: %{version}
Summary: Typing stubs for python-dateutil
METAEOF

%files -n python3-types-python-dateutil-2.9
%license LICENSE
%{python3_sitelib}/dateutil-stubs/
%{python3_sitelib}/types_python_dateutil-%{version}.dist-info/

%changelog
* Wed May 27 2026 Python_Bot <Python_Bot@openeuler.org> - 2.9.0.20260518-1
- Initial compat stub package
