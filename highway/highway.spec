Name:           highway
Version:        1.4.0
Release:        1%{?dist}
Summary:        Performance-portable SIMD intrinsics library

License:        Apache-2.0 AND BSD-3-Clause
URL:            https://github.com/google/highway
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
Highway is a C++ library that provides portable SIMD/vector intrinsics.
It enables writing code that runs efficiently on multiple CPU architectures
using a single source.

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
    -DHWY_ENABLE_TESTS=OFF \
    -DHWY_ENABLE_EXAMPLES=OFF \
    -DHWY_ENABLE_CONTRIB=ON \
    -DHWY_FORCE_STATIC_LIBS=OFF

%cmake_build

%install
%cmake_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSE LICENSE-BSD3
%{_libdir}/libhwy.so.1*
%{_libdir}/libhwy_contrib.so.1*

%files devel
%doc README.md
%{_includedir}/hwy/
%{_libdir}/libhwy.so
%{_libdir}/libhwy_contrib.so
%{_libdir}/cmake/hwy/
%{_libdir}/pkgconfig/libhwy.pc
%{_libdir}/pkgconfig/libhwy_contrib.pc

%changelog
* Thu May 14 2026 openEuler Builder <builder@openeuler.org> - 1.4.0-1
- Initial package for highway 1.4.0
