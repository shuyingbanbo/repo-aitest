# compat package: official has python3-beautifulsoup4-4.12.2
# force_compat mode: introducing 4.14.3 alongside official as python3-beautifulsoup4-4.14
Name:           python-beautifulsoup4-4.14
Version:        4.14.3
Release:        1%{?dist}
Summary:        Screen-scraping library (compat version 4.14)
License:        MIT
URL:            https://www.crummy.com/software/BeautifulSoup/bs4/
Source0:        %{pypi_source beautifulsoup4}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-hatchling
BuildRequires:  python3-typing-extensions >= 4.0.0
BuildRequires:  python3-soupsieve >= 1.6.1

%description
Beautiful Soup is a Python library for pulling data out of HTML and XML files.
It works with your favorite parser to provide idiomatic ways of navigating,
searching, and modifying the parse tree.

This is the compat package providing version 4.14.x alongside the system
python3-beautifulsoup4 package.


%package -n python3-beautifulsoup4-4.14
Summary:        Screen-scraping library (compat version 4.14)
Requires:       python3-typing-extensions >= 4.0.0
Requires:       python3-soupsieve >= 1.6.1
Provides:       python3dist(beautifulsoup4) = %{version}
Provides:       python-beautifulsoup4-4.14

%description -n python3-beautifulsoup4-4.14
Beautiful Soup is a Python library for pulling data out of HTML and XML files.
It works with your favorite parser to provide idiomatic ways of navigating,
searching, and modifying the parse tree.

This is the compat package providing version 4.14.x alongside the system
python3-beautifulsoup4 package.


%package help
Summary:        Development documents and examples for beautifulsoup4-4.14
Requires:       python3-beautifulsoup4-4.14 = %{version}-%{release}

%description help
Documentation and examples for beautifulsoup4 4.14.x.


%prep
%autosetup -n beautifulsoup4-%{version} -p1

%build
%pyproject_build

%install
%pyproject_install

%files -n python3-beautifulsoup4-4.14
%license LICENSE
%{python3_sitelib}/bs4/
%{python3_sitelib}/beautifulsoup4-%{version}*.dist-info/

%files help
%license LICENSE
%doc README.md CHANGELOG

%changelog
* Wed May 27 2026 Python_Bot <Python_Bot@openeuler.org> - 4.14.3-1
- Initial compat package alongside system python3-beautifulsoup4-4.12.2
