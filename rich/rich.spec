%global srcname rich

Name:           python3-rich
Version:        15.0.0
Release:        1%{?dist}
Summary:        Render rich text, tables, progress bars, syntax highlighting, markdown and more
License:        MIT
URL:            https://github.com/Textualize/rich
Source0:        %{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-poetry-core
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
BuildRequires:  python3-markdown-it-py
BuildRequires:  python3-pygments

%description
Rich is a Python library for rich text and beautiful formatting in the terminal,
including tables, progress bars, markdown, syntax highlighting, and tracebacks.

%prep
%autosetup -n %{srcname}-%{version}

%build
%pyproject_build

%install
%pyproject_install

%files
%license LICENSE
%doc README.md
%{python3_sitelib}/rich/
%{python3_sitelib}/rich-%{version}*.dist-info/

%changelog
* Wed Apr 15 2026 OpenEuler Package Import <pkg@openeuler.org> - 15.0.0-1
- Initial package
