Name:           python-types-cachetools
Version:        7.0.0.20260518
Release:        1%{?dist}
Summary:        Typing stubs for cachetools
License:        Apache-2.0
URL:            https://github.com/python/typeshed
Source0:        %{pypi_source types-cachetools 7.0.0.20260518}
BuildArch:      noarch

BuildRequires:  python3-devel

%description
Typing stubs for cachetools.


%package -n python3-types-cachetools
Summary:        Typing stubs for cachetools
Provides:       python-types-cachetools
Provides:       python3dist(types-cachetools) = %{version}

%description -n python3-types-cachetools
Typing stubs for cachetools.


%prep
%autosetup -n types-cachetools-%{version} -p1

%build
# Pure stub package

%install
mkdir -p %{buildroot}%{python3_sitelib}/cachetools-stubs
cp -r cachetools-stubs/* %{buildroot}%{python3_sitelib}/cachetools-stubs/
mkdir -p %{buildroot}%{python3_sitelib}/types_cachetools-%{version}.dist-info
cat > %{buildroot}%{python3_sitelib}/types_cachetools-%{version}.dist-info/METADATA << 'METAEOF'
Metadata-Version: 2.4
Name: types-cachetools
Version: %{version}
Summary: Typing stubs for cachetools
METAEOF

%files -n python3-types-cachetools
%license LICENSE
%{python3_sitelib}/cachetools-stubs/
%{python3_sitelib}/types_cachetools-%{version}.dist-info/

%changelog
* Wed May 27 2026 Python_Bot <Python_Bot@openeuler.org> - 7.0.0.20260518-1
- Initial package
