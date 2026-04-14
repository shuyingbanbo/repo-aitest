%global srcname text-unidecode

Name:           python3-text-unidecode
Version:        1.3
Release:        1%{?dist}
Summary:        The most basic Text::Unidecode port
License:        Artistic-1.0
URL:            https://github.com/kmike/text-unidecode
Source0:        %{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  python3-wheel

%description
Text-Unidecode is a basic Python port of the Perl Text::Unidecode library for
ASCII transliteration of Unicode text.

%prep
%autosetup -n %{srcname}-%{version}

%build
%pyproject_build

%install
%pyproject_install

%files
%license LICENSE
%doc README.rst
%{python3_sitelib}/text_unidecode/
%{python3_sitelib}/text_unidecode-%{version}*.dist-info/

%changelog
* Tue Apr 14 2026 OpenEuler Package Import <pkg@openeuler.org> - 1.3-1
- Initial package
