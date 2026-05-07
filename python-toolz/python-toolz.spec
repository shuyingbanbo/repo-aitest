Name:           python-toolz
Version:        1.1.0
Release:        1%{?dist}
Summary:        List processing tools and functional utilities
License:        BSD-3-Clause
URL:            https://github.com/pytoolz/toolz
Source0:        python-toolz-1.1.0.tar.gz
BuildArch:      noarch

%description
A set of utility functions for iterators, functions, and dictionaries.


%package -n python3-toolz
Summary:        List processing tools and functional utilities
Provides:       python-toolz
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools-git-versioning

%description -n python3-toolz
A set of utility functions for iterators, functions, and dictionaries.


%prep
%autosetup -n python-toolz-%{version}

%build
SETUPTOOLS_GIT_VERSIONING_PRETEND_VERSION=%{version} %pyproject_build

%install
%pyproject_install

%files -n python3-toolz
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/toolz/
%{python3_sitelib}/tlz/
%{python3_sitelib}/toolz-%{version}*.dist-info/

%changelog
* Thu May 07 2026 Python_Bot <Python_Bot@openeuler.org> - 1.1.0-1
- Initial package
