%global srcname cyclopts

Name:           cyclopts
Version:        4.10.2
Release:        1%{?dist}
Summary:        Intuitive, easy CLIs based on type hints
License:        Apache-2.0
URL:            https://github.com/BrianPugh/cyclopts
Source0:        %{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
BuildRequires:  python3-hatchling
BuildRequires:  python3-hatch-vcs

Requires:       python3-attrs
Requires:       python3-docstring-parser
Requires:       python3-rich
Requires:       python3-rich-rst

%description
Cyclopts is a modern command-line interface framework for Python that uses
rich type hints and docstrings to generate intuitive CLIs and help output.

%prep
%autosetup -n %{srcname}-%{version}

%build
%pyproject_build

%install
%pyproject_install

%files
%license LICENSE
%doc README.md
%{_bindir}/cyclopts
%{python3_sitelib}/cyclopts/
%{python3_sitelib}/cyclopts-%{version}*.dist-info/

%changelog
* Mon Apr 13 2026 OpenEuler Package Import <pkg@openeuler.org> - 4.10.2-1
- Initial package
