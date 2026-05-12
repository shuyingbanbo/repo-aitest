%global debug_package %{nil}

Name:           cereal
Version:        1.3.2
Release:        1%{?dist}
Summary:        Header-only C++11 serialization library

License:        BSD-3-Clause
URL:            https://github.com/USCiLab/cereal
Source0:        %{name}-%{version}.tar.gz

Group:          Development/Libraries
Packager:       openEuler Builder <builder@openeuler.org>

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
cereal is a header-only C++11 serialization library. It takes arbitrary data
types and reversibly turns them into different representations, such as compact
binary encodings, XML, or JSON. It has no external dependencies.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Packager:       openEuler Builder <builder@openeuler.org>

%description devel
Header files and CMake integration files for %{name}.

%prep
%autosetup

%build
%cmake \
    -DJUST_INSTALL_CEREAL=ON \
    -DBUILD_DOC=OFF \
    -DBUILD_SANDBOX=OFF \
    -DCEREAL_INSTALL=ON
%cmake_build

%install
%cmake_install

%files devel
%license LICENSE
%doc README.md
%{_includedir}/cereal/
%{_libdir}/cmake/cereal/

%changelog
* Tue May 12 2026 openEuler Builder <builder@openeuler.org> - 1.3.2-1
- Initial package for cereal 1.3.2
