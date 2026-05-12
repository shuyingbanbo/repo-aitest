%global debug_package %{nil}

Name:           xtensor
Version:        0.27.1
Release:        1%{?dist}
Summary:        C++ tensors with broadcasting and lazy computing

License:        BSD-3-Clause
URL:            https://github.com/xtensor-stack/xtensor
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
Group:          Development/Libraries
Packager:       openEuler Builder <builder@openeuler.org>

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  cmake(xtl)
%description
xtensor is a C++ library for multi-dimensional arrays with broadcasting and
lazy computing. It provides an extensible expression system compatible with
NumPy, and supports SIMD acceleration via xsimd.

%package devel
Summary:        Development files for %{name}
BuildArch:      noarch
Group:          Development/Libraries
Packager:       openEuler Builder <builder@openeuler.org>
Requires:       cmake(xtl)

%description devel
Header files and CMake integration files for %{name}.

%prep
%autosetup

%build
%cmake \
    -DBUILD_TESTS=OFF \
    -DBUILD_EXAMPLES=OFF \
    -DXTENSOR_USE_XSIMD=OFF \
    -DXTENSOR_USE_TBB=OFF \
    -DXTENSOR_USE_OPENMP=OFF
%cmake_build

%install
%cmake_install

%files devel
%license LICENSE
%doc README.md
%{_includedir}/xtensor/
%{_includedir}/xtensor.hpp
%{_datadir}/cmake/xtensor/
%{_datadir}/pkgconfig/xtensor.pc
%{_datadir}/xeus-cpp/
/usr/etc/xeus-cpp/

%changelog
* Tue May 12 2026 openEuler Builder <builder@openeuler.org> - 0.27.1-1
- Initial package for xtensor 0.27.1
