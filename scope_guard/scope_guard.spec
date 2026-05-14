%global debug_package %{nil}

Name:           scope_guard
Version:        1.1.0
Release:        1%{?dist}
Summary:        A public, general, simple, and fast C++11 scope guard header-only library

License:        Unlicense
URL:            https://github.com/ricab/scope_guard
Source0:        %{name}-%{version}.tar.gz

Group:          Development/Libraries
Packager:       openEuler Builder <builder@openeuler.org>

BuildArch:      noarch

%description
A public, general, simple, and fast C++11 scope guard that defends against
implicitly ignored returns and optionally enforces noexcept at compile time
(in C++17), all in a SFINAE-friendly manner.

A scope guard is an object that employs RAII to execute a provided callback
when leaving scope, be it through a fall-through, a return, or an exception.
All necessary code is provided in a single header file.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Packager:       openEuler Builder <builder@openeuler.org>
BuildArch:      noarch

%description devel
Header file for %{name}.

This package provides the scope_guard.hpp header for use in C++11 and later
projects that need RAII-based scope guard functionality.

%prep
%autosetup

%build
# Header-only library, no compilation required

%install
install -d %{buildroot}%{_includedir}
install -m 0644 scope_guard.hpp %{buildroot}%{_includedir}/scope_guard.hpp

%files devel
%license LICENSE
%doc README.md
%{_includedir}/scope_guard.hpp

%changelog
* Thu May 14 2026 openEuler Builder <builder@openeuler.org> - 1.1.0-1
- Initial package
