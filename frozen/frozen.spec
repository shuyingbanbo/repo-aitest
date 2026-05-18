%global debug_package %{nil}

Name:           frozen
Version:        1.2.0
Release:        1%{?dist}
Summary:        Header-only, constexpr-friendly C++ container library
License:        Apache-2.0
URL:            https://github.com/serge-sans-paille/frozen
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
Group:          Development/Libraries
Packager:       openEuler Builder <builder@openeuler.org>

%description
frozen provides immutable (frozen), constexpr-compatible versions of
std::set, std::map, std::unordered_set, std::unordered_map and a
0-cost initialization version of std::search. This package is
header-only and requires C++14 or later.

%package        devel
Summary:        Development headers for %{name}
License:        Apache-2.0
Requires:       %{name} = %{version}-%{release}

%description    devel
Header-only development files for the frozen C++ library.

%prep
%setup -q

%build

%install
install -d %{buildroot}%{_includedir}
cp -a include/frozen %{buildroot}%{_includedir}/

%files
%license LICENSE
%doc README.rst

%files devel
%{_includedir}/frozen/

%changelog
* Mon May 18 2026 openEuler Builder <builder@openeuler.org> - 1.2.0-1
- Initial package for frozen 1.2.0
