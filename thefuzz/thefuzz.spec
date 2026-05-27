Name:           python-thefuzz
Version:        0.22.1
Release:        1%{?dist}
Summary:        Fuzzy String Matching in Python
License:        MIT
URL:            https://github.com/seatgeek/thefuzz
Source0:        %{pypi_source thefuzz}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
A python library for doing fuzzy string matching using Levenshtein Distance.


%package -n python3-thefuzz
Summary:        Fuzzy String Matching in Python
Provides:       python-thefuzz
Provides:       python3dist(thefuzz) = %{version}

%description -n python3-thefuzz
A python library for doing fuzzy string matching using Levenshtein Distance.


%package help
Summary:        Documentation for thefuzz
Requires:       python3-thefuzz = %{version}-%{release}

%description help
Documentation for thefuzz.


%prep
%autosetup -n thefuzz-%{version} -p1

%build
%py3_build

%install
%py3_install

%files -n python3-thefuzz
%license LICENSE.txt
%{python3_sitelib}/thefuzz/
%{python3_sitelib}/thefuzz-%{version}*.egg-info/

%files help
%license LICENSE.txt
%doc README.rst

%changelog
* Wed May 27 2026 Python_Bot <Python_Bot@openeuler.org> - 0.22.1-1
- Initial package
