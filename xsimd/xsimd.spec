%global debug_package %{nil}

Name:           xsimd
Version:        14.2.0
Release:        1%{?dist}
Summary:        C++ wrappers for SIMD intrinsics

License:        BSD-3-Clause
URL:            https://github.com/xtensor-stack/xsimd
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
Group:          Development/Libraries
Packager:       openEuler Builder <builder@openeuler.org>

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
xsimd provides a unified means for using SIMD features for library authors.
It is a header-only C++ library that offers C++ wrappers for SIMD intrinsics
and parallelized, optimized mathematical functions.

%package devel
Summary:        Development files for %{name}
BuildArch:      noarch
Group:          Development/Libraries
Packager:       openEuler Builder <builder@openeuler.org>

%description devel
Header files and CMake integration files for %{name}.

%prep
%autosetup

%build
%cmake \
    -DBUILD_TESTS=OFF \
    -DENABLE_XTL_COMPLEX=OFF \
    -DXSIMD_SKIP_INSTALL=OFF
%cmake_build

%install
%cmake_install

%files devel
%license LICENSE
%doc README.md
%{_includedir}/xsimd/
%{_datadir}/cmake/xsimd/
%{_datadir}/pkgconfig/xsimd.pc

%changelog
* Tue May 12 2026 openEuler Builder <builder@openeuler.org> - 14.2.0-1
- Initial package for xsimd 14.2.0
