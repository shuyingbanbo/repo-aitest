%global debug_package %{nil}

Name:           benchmark
Version:        1.9.5
Release:        1%{?dist}
Summary:        Micro-benchmark support library from Google

License:        Apache-2.0
URL:            https://github.com/google/benchmark
Source0:        %{name}-%{version}.tar.gz

Group:          Development/Libraries
Packager:       openEuler Builder <builder@openeuler.org>

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
benchmark is a micro-benchmark support library from Google. It provides a
framework for writing and running C++ benchmarks, with support for
multi-threaded benchmarks, custom counters, and output in various formats.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Packager:       openEuler Builder <builder@openeuler.org>
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files, CMake integration files, and pkgconfig files for %{name}.

%prep
%autosetup

%build
%cmake \
    -DBENCHMARK_ENABLE_TESTING=OFF \
    -DBENCHMARK_ENABLE_GTEST_TESTS=OFF \
    -DBENCHMARK_INSTALL_DOCS=OFF \
    -DBENCHMARK_INSTALL_TOOLS=OFF \
    -DBENCHMARK_BUILD_32_BITS=OFF \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_CXX_FLAGS="-Wno-restrict" \
    -DHAVE_STD_REGEX=ON \
    -DCMAKE_INSTALL_LIBDIR=%{_libdir}
%cmake_build

%install
%cmake_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_libdir}/libbenchmark.so.1
%{_libdir}/libbenchmark.so.1.*
%{_libdir}/libbenchmark_main.so.1
%{_libdir}/libbenchmark_main.so.1.*
%files devel
%license LICENSE
%doc README.md
%{_includedir}/benchmark/
%{_libdir}/libbenchmark.so
%{_libdir}/libbenchmark_main.so
%{_libdir}/cmake/benchmark/
%{_libdir}/pkgconfig/benchmark.pc
%{_libdir}/pkgconfig/benchmark_main.pc

%changelog
* Tue May 13 2026 openEuler Builder <builder@openeuler.org> - 1.9.5-1
- Initial package for benchmark 1.9.5
