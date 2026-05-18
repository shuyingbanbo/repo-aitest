%global debug_package %{nil}

Name:           parallel-hashmap
Version:        2.0.0
Release:        1%{?dist}
Summary:        Header-only, high-performance C++ hashmap and btree containers
License:        Apache-2.0
URL:            https://github.com/greg7mdp/parallel-hashmap
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
Group:          Development/Libraries
Packager:       openEuler Builder <builder@openeuler.org>

%description
parallel-hashmap is a header-only C++ library providing high-performance,
thread-safe parallel hashmap and btree containers compatible with the
Abseil Swiss tables design. It aims for a 10-20x lower memory overhead
on resize compared to std::unordered_map. Requires C++11 or later.

%package        devel
Summary:        Development headers for %{name}
License:        Apache-2.0
Requires:       %{name} = %{version}-%{release}

%description    devel
Header-only development files for the parallel-hashmap C++ library.

%prep
%setup -q

%build

%install
install -d %{buildroot}%{_includedir}
cp -a parallel_hashmap %{buildroot}%{_includedir}/

%files
%license LICENSE
%doc README.md

%files devel
%{_includedir}/parallel_hashmap/

%changelog
* Mon May 18 2026 openEuler Builder <builder@openeuler.org> - 2.0.0-1
- Initial package for parallel-hashmap 2.0.0
