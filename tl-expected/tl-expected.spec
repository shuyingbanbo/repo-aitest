%global debug_package %{nil}

Name:           tl-expected
Version:        1.1.0
Release:        1%{?dist}
Summary:        C++23 std::expected implementation for C++11/14/17/20
License:        CC0-1.0
URL:            https://github.com/TartanLlama/expected
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
Group:          Development/Libraries
Packager:       openEuler Builder <builder@openeuler.org>

%description
tl::expected is a header-only implementation of std::expected proposed
for C++23, available for C++11, C++14, C++17, and C++20. It provides a
type-safe way to return either a value or an error without using exceptions.

%package        devel
Summary:        Development headers for %{name}
License:        CC0-1.0

%description    devel
Header-only development files for the tl::expected C++ library.

%prep
%setup -q

%build

%install
install -d %{buildroot}%{_includedir}/tl
install -p -m 644 include/tl/expected.hpp %{buildroot}%{_includedir}/tl/

%files devel
%license COPYING
%doc README.md
%{_includedir}/tl/expected.hpp

%changelog
* Tue May 19 2026 openEuler Builder <builder@openeuler.org> - 1.1.0-1
- Initial package for tl-expected 1.1.0
