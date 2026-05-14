Name:           simdjson
Version:        4.6.4
Release:        1%{?dist}
Summary:        Parsing gigabytes of JSON per second using SIMD instructions

License:        Apache-2.0
URL:            https://github.com/simdjson/simdjson
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
simdjson is a C++ library that uses SIMD instructions to parse JSON at
multi-gigabyte-per-second speeds. It is one of the fastest JSON parsers
available.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files, CMake integration files, and pkgconfig files for %{name}.

%prep
%autosetup

%build
%cmake \
    -DBUILD_SHARED_LIBS=ON \
    -DSIMDJSON_INSTALL=ON \
    -DSIMDJSON_BUILD_STATIC_LIB=OFF \
    -DSIMDJSON_ENABLE_THREADS=ON

%cmake_build

%install
%cmake_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSE
%{_libdir}/libsimdjson.so.33*

%files devel
%doc README.md
%{_includedir}/simdjson.h
%{_libdir}/libsimdjson.so
%{_libdir}/cmake/simdjson/
%{_libdir}/pkgconfig/simdjson.pc

%changelog
* Thu May 14 2026 openEuler Builder <builder@openeuler.org> - 4.6.4-1
- Initial package for simdjson 4.6.4
