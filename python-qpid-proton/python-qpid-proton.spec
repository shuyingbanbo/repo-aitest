Name:           python-qpid-proton-0.39
Version:        0.39.0
Release:        1%{?dist}
Summary:        Python language bindings for the qpid-proton messaging library (v0.39)
License:        ASL 2.0
URL:            http://qpid.apache.org/proton/
Source0:        https://files.pythonhosted.org/packages/source/p/python-qpid-proton/python-qpid-proton-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-cffi
BuildRequires:  gcc
BuildRequires:  openssl-devel

%description
Python language bindings for the Apache Qpid Proton messaging library (version 0.39.x).
This compat package coexists with the official python3-qpid-proton package.


%package -n python3-python-qpid-proton-0.39
Summary:        Python language bindings for the qpid-proton messaging library (v0.39)
Provides:       python3-python-qpid-proton = %{version}-%{release}
Provides:       python3dist(python-qpid-proton) = %{version}
Requires:       python3-cffi

%description -n python3-python-qpid-proton-0.39
Python language bindings for the Apache Qpid Proton messaging library (version 0.39.x).
This compat package coexists with the official python3-qpid-proton package.


%package help
Summary:        Documentation for python-qpid-proton (v0.39)
Requires:       python3-python-qpid-proton-0.39
Provides:       python3-python-qpid-proton-0.39-doc

%description help
Documentation and examples for python-qpid-proton version 0.39.x.


%prep
%autosetup -n python-qpid-proton-%{version} -p1
# PyPI tarball does not include a separate LICENSE file; extract from PKG-INFO
grep -A 999 '^License:' PKG-INFO | head -1 > LICENSE || true
printf 'Apache License\nVersion 2.0\nSee http://www.apache.org/licenses/LICENSE-2.0\n' > LICENSE


%build
%define _lto_cflags %{nil}
%undefine _hardened_build
%py3_build


%install
%py3_install


%files -n python3-python-qpid-proton-0.39
%license LICENSE
%{python3_sitearch}/proton/
%{python3_sitearch}/cproton.py
%{python3_sitearch}/cproton_ffi*.so
%{python3_sitearch}/__pycache__/cproton*.pyc
%{python3_sitearch}/python_qpid_proton-%{version}*.egg-info/


%files help
%license LICENSE
%doc README.rst


%changelog
* Thu May 28 2026 Python_Bot <Python_Bot@openeuler.org> - 0.39.0-1
- Initial compat package for python-qpid-proton 0.39.0
