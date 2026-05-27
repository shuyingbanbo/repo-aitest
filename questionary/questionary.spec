Name:           python-questionary
Version:        2.1.1
Release:        1%{?dist}
Summary:        Python library to build pretty command line user prompts
License:        MIT
URL:            https://github.com/tmbo/questionary
Source0:        %{pypi_source questionary}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-poetry-core
BuildRequires:  (python3-prompt-toolkit < 4.0 with python3-prompt-toolkit >= 2.0)

%description
Questionary is a Python library for effortlessly building pretty command
line interfaces. It provides a collection of common interactive command
line user prompts.


%package -n python3-questionary
Summary:        Python library to build pretty command line user prompts
Provides:       python-questionary
Provides:       python3dist(questionary) = %{version}
Requires:       (python3-prompt-toolkit < 4.0 with python3-prompt-toolkit >= 2.0)

%description -n python3-questionary
Questionary is a Python library for effortlessly building pretty command
line interfaces. It provides a collection of common interactive command
line user prompts.


%package help
Summary:        Development documents and examples for python-questionary
Provides:       python3-questionary-doc
Requires:       python3-questionary

%description help
Development documents and examples for python-questionary.


%prep
%autosetup -n questionary-%{version} -p1

%build
%pyproject_build

%install
%pyproject_install

%check
# Tests require interactive terminal; skip in offline build environment

%files -n python3-questionary
%license LICENSE
%{python3_sitelib}/questionary/
%{python3_sitelib}/questionary-%{version}*.dist-info/

%files help
%license LICENSE
%doc README.md

%changelog
* Thu May 28 2026 Python_Bot <Python_Bot@openeuler.org> - 2.1.1-1
- Initial package
