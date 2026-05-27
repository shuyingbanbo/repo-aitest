Name:           python-pyright
Version:        1.1.409
Release:        1%{?dist}
Summary:        Command line wrapper for pyright type checker
License:        MIT
URL:            https://github.com/RobertCraigie/pyright-python
Source0:        %{pypi_source pyright}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-nodeenv >= 1.6.0
BuildRequires:  python3-typing-extensions >= 4.1

%description
Pyright is a full-featured, standards-based static type checker for Python.
This package provides a command line wrapper for pyright.


%package -n python3-pyright
Summary:        Command line wrapper for pyright type checker
Provides:       python-pyright
Provides:       python3dist(pyright) = %{version}
Requires:       python3-nodeenv >= 1.6.0
Requires:       python3-typing-extensions >= 4.1

%description -n python3-pyright
Pyright is a full-featured, standards-based static type checker for Python.
This package provides a command line wrapper for pyright.


%package help
Summary:        Development documents and examples for python-pyright
Provides:       python3-pyright-doc
Requires:       python3-pyright

%description help
Development documents and examples for python-pyright.


%prep
%autosetup -n pyright-%{version} -p1

%build
%py3_build

%install
%py3_install

%check
# Tests require network access to download pyright binaries; skip in offline build

%files -n python3-pyright
%license LICENSE
%{python3_sitelib}/pyright/
%{python3_sitelib}/pyright-%{version}*.egg-info/
%{_bindir}/pyright
%{_bindir}/pyright-langserver
%{_bindir}/pyright-python
%{_bindir}/pyright-python-langserver

%files help
%license LICENSE
%doc README.md

%changelog
* Thu May 28 2026 Python_Bot <Python_Bot@openeuler.org> - 1.1.409-1
- Initial package
