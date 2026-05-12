%global debug_package %{nil}

Name:           expected-lite
Version:        0.10.0
Release:        1%{?dist}
Summary:        Expected objects in C++11 and later in a single-file header-only library

License:        BSL-1.0
URL:            https://github.com/martinmoene/expected-lite
Source0:        %{name}-%{version}.tar.gz

Group:          Development/Libraries
Packager:       openEuler Builder <builder@openeuler.org>

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
expected-lite is a single-file header-only library for expected objects in
C++11 and later. It provides a drop-in replacement for the C++23
std::expected, following the p0323 proposal.

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
    -DEXPECTED_LITE_OPT_BUILD_TESTS=OFF \
    -DEXPECTED_LITE_OPT_BUILD_EXAMPLES=OFF
%cmake_build

%install
%cmake_install

%files devel
%license LICENSE.txt
%doc README.md
%{_includedir}/nonstd/
%{_libdir}/cmake/expected-lite/

%changelog
* Tue May 12 2026 openEuler Builder <builder@openeuler.org> - 0.10.0-1
- Initial package for expected-lite 0.10.0
