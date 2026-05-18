%global debug_package %{nil}

Name:           nameof
Version:        0.10.5
Release:        1%{?dist}
Summary:        Header-only C++ library for obtaining simple readable name of type, variable, member, or enum
License:        MIT
URL:            https://github.com/Neargye/nameof
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
Group:          Development/Libraries
Packager:       openEuler Builder <builder@openeuler.org>

%description
nameof is a header-only C++ library providing compile-time reflection
for obtaining the simple readable name of a type, variable, member,
function, macro, or enum. Requires C++17 or later.

%package        devel
Summary:        Development headers for %{name}
License:        MIT
Requires:       %{name} = %{version}-%{release}

%description    devel
Header-only development files for the nameof C++ library.

%prep
%setup -q

%build

%install
install -d %{buildroot}%{_includedir}
install -p -m 644 include/nameof.hpp %{buildroot}%{_includedir}/

%files
%license LICENSE
%doc README.md

%files devel
%{_includedir}/nameof.hpp

%changelog
* Mon May 18 2026 openEuler Builder <builder@openeuler.org> - 0.10.5-1
- Initial package for nameof 0.10.5
