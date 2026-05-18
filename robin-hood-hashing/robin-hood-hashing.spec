%global debug_package %{nil}

Name:           robin-hood-hashing
Version:        3.11.5
Release:        1%{?dist}
Summary:        Fast and memory-efficient single-header C++ hashmap
License:        MIT
URL:            https://github.com/martinus/robin-hood-hashing
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
Group:          Development/Libraries
Packager:       openEuler Builder <builder@openeuler.org>

%description
robin-hood-hashing is a single-header C++ hashmap using robin hood
open addressing with backward shift deletion. It provides very fast
lookups while keeping memory usage low. Requires C++14 or later.

%package        devel
Summary:        Development headers for %{name}
License:        MIT
Requires:       %{name} = %{version}-%{release}

%description    devel
Header-only development files for the robin-hood-hashing C++ library.

%prep
%setup -q

%build

%install
install -d %{buildroot}%{_includedir}
install -p -m 644 src/include/robin_hood.h %{buildroot}%{_includedir}/

%files
%license LICENSE
%doc README.md

%files devel
%{_includedir}/robin_hood.h

%changelog
* Mon May 18 2026 openEuler Builder <builder@openeuler.org> - 3.11.5-1
- Initial package for robin-hood-hashing 3.11.5
