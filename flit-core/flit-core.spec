Name:           python-flit-core
Version:        3.12.0
Release:        1%{?dist}
Summary:        Distribution-building parts of Flit
License:        BSD-3-Clause
URL:            https://github.com/pypa/flit
Source0:        https://files.pythonhosted.org/packages/source/f/flit_core/flit_core-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pip

%description
Distribution-building parts of Flit. See flit package for more information.
Flit is a simple way to put Python packages and modules on PyPI.


%package -n python3-flit-core
Summary:        Distribution-building parts of Flit
Provides:       python-flit-core
Provides:       python3dist(flit-core) = %{version}

%description -n python3-flit-core
Distribution-building parts of Flit. See flit package for more information.
Flit is a simple way to put Python packages and modules on PyPI.


%package help
Summary:        Documentation for python-flit-core
Requires:       python3-flit-core
Provides:       python3-flit-core-doc

%description help
Documentation and examples for python-flit-core.


%prep
%autosetup -n flit_core-%{version} -p1


%build
# flit_core bootstraps itself; use --no-build-isolation since backend is bundled in source
pip3 wheel --no-build-isolation --no-deps -w wheelhouse .


%install
pip3 install --no-build-isolation --no-deps \
    --prefix=%{_prefix} --root %{buildroot} \
    wheelhouse/flit_core-%{version}*.whl


%files -n python3-flit-core
%license LICENSE
%{python3_sitelib}/flit_core/
%{python3_sitelib}/flit_core-%{version}*.dist-info/


%files help
%license LICENSE
%doc README.rst


%changelog
* Thu May 28 2026 Python_Bot <Python_Bot@openeuler.org> - 3.12.0-1
- Initial package
