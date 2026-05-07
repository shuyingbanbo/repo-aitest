Name:           python-tenacity
Version:        9.1.4
Release:        1%{?dist}
Summary:        Retry code until it succeeds
License:        Apache-2.0
URL:            https://github.com/jd/tenacity
Source0:        python-tenacity-9.1.4.tar.gz
BuildArch:      noarch

%description
Tenacity is a general-purpose retrying library to simplify the task of adding
retry behavior to just about anything.


%package -n python3-tenacity
Summary:        Retry code until it succeeds
Provides:       python-tenacity
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm

%description -n python3-tenacity
Tenacity is a general-purpose retrying library to simplify the task of adding
retry behavior to just about anything.


%prep
%autosetup -n python-tenacity-%{version}

%build
SETUPTOOLS_SCM_PRETEND_VERSION=%{version} %py3_build

%install
SETUPTOOLS_SCM_PRETEND_VERSION=%{version} %py3_install

%files -n python3-tenacity
%license LICENSE
%doc README.rst
%{python3_sitelib}/tenacity/
%{python3_sitelib}/tenacity-%{version}*.egg-info/

%changelog
* Thu May 07 2026 Python_Bot <Python_Bot@openeuler.org> - 9.1.4-1
- Initial package
