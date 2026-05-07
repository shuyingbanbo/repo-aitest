Name:           python-structlog
Version:        25.5.0
Release:        1%{?dist}
Summary:        Structured Logging for Python
License:        MIT OR Apache-2.0
URL:            https://github.com/hynek/structlog
Source0:        python-structlog-25.5.0.tar.gz
BuildArch:      noarch

%description
structlog is the production-ready logging solution for Python.
It makes logging fast, less painful, and prettier.


%package -n python3-structlog
Summary:        Structured Logging for Python
Provides:       python-structlog
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-hatchling
BuildRequires:  python3-hatch-vcs
BuildRequires:  python3-hatch-fancy-pypi-readme

%description -n python3-structlog
structlog is the production-ready logging solution for Python.
It makes logging fast, less painful, and prettier.


%prep
%autosetup -n python-structlog-%{version}

%build
SETUPTOOLS_SCM_PRETEND_VERSION=%{version} %pyproject_build

%install
SETUPTOOLS_SCM_PRETEND_VERSION=%{version} %pyproject_install

%files -n python3-structlog
%license LICENSE-MIT LICENSE-APACHE
%doc README.md CHANGELOG.md
%{python3_sitelib}/structlog/
%{python3_sitelib}/structlog-%{version}*.dist-info/

%changelog
* Thu May 07 2026 Python_Bot <Python_Bot@openeuler.org> - 25.5.0-1
- Initial package
