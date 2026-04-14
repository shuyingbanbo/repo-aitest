%global srcname loguru

Name:           python3-loguru
Version:        0.7.3
Release:        1%{?dist}
Summary:        Python logging made simple
License:        MIT
URL:            https://github.com/Delgan/loguru
Source0:        %{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
BuildRequires:  python3-flit

%description
Loguru is a Python logging library focused on making logging simple while
providing a pre-configured logger and convenient APIs for common logging tasks.

%prep
%autosetup -n %{srcname}-%{version}

%build
%pyproject_build

%install
%pyproject_install

%files
%license LICENSE
%doc README.md
%{python3_sitelib}/loguru/
%{python3_sitelib}/loguru-%{version}*.dist-info/

%changelog
* Tue Apr 14 2026 OpenEuler Package Import <pkg@openeuler.org> - 0.7.3-1
- Initial package
