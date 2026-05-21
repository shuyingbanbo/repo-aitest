Name:           python-schedule
Version:        1.2.2
Release:        1%{?dist}
Summary:        Job scheduling for humans
License:        MIT
URL:            https://github.com/dbader/schedule
Source0:        https://github.com/dbader/schedule/archive/v%{version}/python-schedule-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-setuptools

%description
schedule is a Python job scheduling library. Run Python functions (or any
other callable) periodically using a friendly syntax. No extra processes
needed — purely in-process scheduler with no external dependencies.


%package -n python3-schedule
Summary:        Job scheduling for humans
Provides:       python-schedule
Provides:       python3dist(schedule) = %{version}

%description -n python3-schedule
schedule is a Python job scheduling library. Run Python functions (or any
other callable) periodically using a friendly syntax. No extra processes
needed — purely in-process scheduler with no external dependencies.


%package help
Summary:        Development documents and examples for python-schedule
Provides:       python3-schedule-doc

%description help
Development documents and examples for python-schedule.


%prep
%autosetup -n python-schedule-%{version} -p1

%build
%pyproject_build

%install
%pyproject_install

%files -n python3-schedule
%license LICENSE.txt
%{python3_sitelib}/schedule/
%{python3_sitelib}/schedule-%{version}*.dist-info/

%files help
%doc README.rst

%changelog
* Thu May 21 2026 Python_Bot <Python_Bot@openeuler.org> - 1.2.2-1
- Initial package
