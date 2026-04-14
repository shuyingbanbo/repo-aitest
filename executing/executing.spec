%global srcname executing

Name:           python3-executing
Version:        2.2.1
Release:        1%{?dist}
Summary:        Get the currently executing AST node of a frame
License:        MIT
URL:            https://github.com/alexmojaki/executing
Source0:        %{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
BuildRequires:  python3-setuptools_scm

%description
Executing gets the currently executing AST node of a frame and related
introspection information.

%prep
%autosetup -n %{srcname}-%{version}

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_install

%files
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/executing/
%{python3_sitelib}/executing-%{version}*.dist-info/

%changelog
* Tue Apr 14 2026 OpenEuler Package Import <pkg@openeuler.org> - 2.2.1-1
- Initial package
