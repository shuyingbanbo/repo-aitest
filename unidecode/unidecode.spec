Name:           python-unidecode
Version:        1.4.0
Release:        1%{?dist}
Summary:        ASCII transliterations of Unicode text
License:        GPL-2.0-or-later
URL:            https://github.com/avian2/unidecode
Source0:        %{pypi_source unidecode}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
Unidecode takes Unicode data and attempts to represent it in ASCII characters.


%package -n python3-unidecode
Summary:        ASCII transliterations of Unicode text
Provides:       python-unidecode
Provides:       python3dist(unidecode) = %{version}

%description -n python3-unidecode
Unidecode takes Unicode data and attempts to represent it in ASCII characters.


%package help
Summary:        Documentation for unidecode
Requires:       python3-unidecode = %{version}-%{release}

%description help
Documentation for unidecode.


%prep
%autosetup -n unidecode-%{version} -p1

%build
%py3_build

%install
%py3_install

%files -n python3-unidecode
%license LICENSE
%{python3_sitelib}/unidecode/
%{python3_sitelib}/Unidecode-%{version}*.egg-info/
%{_bindir}/unidecode

%files help
%license LICENSE
%doc README.rst

%changelog
* Wed May 27 2026 Python_Bot <Python_Bot@openeuler.org> - 1.4.0-1
- Initial package
