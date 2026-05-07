Name:           python-celery
Version:        5.4.0
Release:        1%{?dist}
Summary:        Distributed Task Queue
License:        BSD-3-Clause
URL:            https://github.com/celery/celery
Source0:        python-celery-5.4.0.tar.gz
BuildArch:      noarch

%description
Celery is a simple, flexible, and reliable distributed system to
process vast amounts of messages, while providing operations with
the tools required to maintain such a system.

It's a task queue with focus on real-time processing, while also
supporting task scheduling.


%package -n python3-celery
Summary:        Distributed Task Queue
Provides:       python-celery
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-celery
Celery is a simple, flexible, and reliable distributed system to
process vast amounts of messages, while providing operations with
the tools required to maintain such a system.

It's a task queue with focus on real-time processing, while also
supporting task scheduling.


%prep
%autosetup -n python-celery-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-celery
%license LICENSE
%doc README.rst
%{python3_sitelib}/celery/
%{python3_sitelib}/celery-%{version}*.egg-info/
%{_bindir}/celery

%changelog
* Thu May 07 2026 Python_Bot <Python_Bot@openeuler.org> - 5.4.0-1
- Initial package
