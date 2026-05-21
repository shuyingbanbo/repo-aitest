Name:           python-diskcache
Version:        5.6.3
Release:        1%{?dist}
Summary:        Disk and file backed persistent cache library
License:        Apache-2.0
URL:            https://github.com/grantjenks/python-diskcache
Source0:        https://github.com/grantjenks/python-diskcache/archive/v%{version}/python-diskcache-%{version}.tar.gz
BuildArch:      noarch

%description
DiskCache is an Apache2 licensed disk and file backed cache library, written
in pure-Python, and compatible with Django. It efficiently makes gigabytes of
storage space available for caching by leveraging rock-solid database libraries
and memory-mapped files.


%package -n python3-diskcache
Summary:        Disk and file backed persistent cache library
Provides:       python-diskcache
Provides:       python3dist(diskcache) = %{version}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-diskcache
DiskCache is an Apache2 licensed disk and file backed cache library, written
in pure-Python, and compatible with Django. It efficiently makes gigabytes of
storage space available for caching by leveraging rock-solid database libraries
and memory-mapped files.


%package help
Summary:        Development documents and examples for python-diskcache
Provides:       python3-diskcache-doc

%description help
Development documents and examples for python-diskcache.


%prep
%autosetup -n python-diskcache-%{version} -p1

%build
%py3_build

%install
%py3_install

%files -n python3-diskcache
%license LICENSE
%{python3_sitelib}/diskcache/
%{python3_sitelib}/diskcache-%{version}*.egg-info/

%files help
%doc README.rst

%changelog
* Thu May 21 2026 Python_Bot <Python_Bot@openeuler.org> - 5.6.3-1
- Initial package
