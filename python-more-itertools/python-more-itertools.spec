Name:           python-more-itertools
Version:        11.0.2
Release:        1%{?dist}
Summary:        More routines for operating on Python iterables, beyond itertools
License:        MIT
URL:            https://github.com/more-itertools/more-itertools
Source0:        python-more-itertools-11.0.2.tar.gz
BuildArch:      noarch

%description
More routines for operating on Python iterables, beyond itertools.


%package -n python3-more-itertools
Summary:        More routines for operating on Python iterables, beyond itertools
Provides:       python-more-itertools
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-flit-core

%description -n python3-more-itertools
More routines for operating on Python iterables, beyond itertools.


%prep
%autosetup -n python-more-itertools-%{version}

%build
%pyproject_build

%install
%pyproject_install

%files -n python3-more-itertools
%license LICENSE
%doc README.rst
%{python3_sitelib}/more_itertools/
%{python3_sitelib}/more_itertools-%{version}*.dist-info/

%changelog
* Thu May 07 2026 Python_Bot <Python_Bot@openeuler.org> - 11.0.2-1
- Initial package
