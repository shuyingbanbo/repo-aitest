Name:           python3-pyjwkest
Version:        1.4.4
Release:        1%{?dist}
Summary:        Python implementation of JWT, JWE, JWS and JWK
License:        Apache-2.0
URL:            https://github.com/IdentityPython/pyjwkest
Source0:        pyjwkest-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
BuildRequires:  python3-pycryptodomex
BuildRequires:  python3-requests
BuildRequires:  python3-six
BuildRequires:  python3-future

%description
Python implementation of JWT (JSON Web Token), JWE (JSON Web Encryption),
JWS (JSON Web Signature) and JWK (JSON Web Key) as defined in the IETF JOSE
working group drafts.

%prep
%autosetup -n pyjwkest-%{version}

%build
%pyproject_build

%install
%pyproject_install

%files
%license LICENSE
%doc README.rst
%{python3_sitelib}/jwkest/
%{python3_sitelib}/pyjwkest-%{version}*.dist-info/
%{_bindir}/gen_symkey.py
%{_bindir}/jwdecrypt.py
%{_bindir}/jwenc.py
%{_bindir}/jwk_create.py
%{_bindir}/jwk_export.py
%{_bindir}/jwkutil.py
%{_bindir}/peek.py

%changelog
* Mon Apr 07 2026 OpenEuler Package Import <pkg@openeuler.org> - 1.4.4-1
- Initial package
