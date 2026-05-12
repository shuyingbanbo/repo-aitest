Name:           redis-plus-plus
Version:        1.3.15
Release:        1%{?dist}
Summary:        C++ client for Redis based on Hiredis

License:        Apache-2.0
URL:            https://github.com/sewenew/redis-plus-plus
Source0:        %{name}-%{version}.tar.gz

Group:          Development/Libraries
Packager:       openEuler Builder <builder@openeuler.org>

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hiredis-devel

%description
redis-plus-plus is a C++ client for Redis. It is based on Hiredis and
supports most Redis commands, including cluster, sentinel, pipeline-based
batching, transactions, scripting, and pub/sub.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Packager:       openEuler Builder <builder@openeuler.org>
Requires:       %{name}%{?_isa} = %{version}
Requires:       hiredis-devel

%description devel
Header files, CMake integration files, and pkgconfig files for %{name}.

%prep
%autosetup

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DREDIS_PLUS_PLUS_BUILD_TEST=OFF \
    -DREDIS_PLUS_PLUS_USE_TLS=OFF \
    -DREDIS_PLUS_PLUS_BUILD_ASYNC=OFF \
    -DREDIS_PLUS_PLUS_BUILD_STATIC=OFF \
    -DREDIS_PLUS_PLUS_CXX_STANDARD=17
%cmake_build

%install
%cmake_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_libdir}/libredis++.so.1
%{_libdir}/libredis++.so.1.3.15

%files devel
%license LICENSE
%doc README.md
%{_includedir}/sw/
%{_libdir}/libredis++.so
%{_datadir}/cmake/redis++/
%{_libdir}/pkgconfig/redis++.pc

%changelog
* Tue May 12 2026 openEuler Builder <builder@openeuler.org> - 1.3.15-1
- Initial package for redis-plus-plus 1.3.15
