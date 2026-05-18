%global debug_package %{nil}

Name:           asio
Version:        1.38.0
Release:        1%{?dist}
Summary:        Asio C++ Library — cross-platform asynchronous I/O
License:        MIT
URL:            https://github.com/chriskohlhoff/asio
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
Group:          Development/Libraries
Packager:       openEuler Builder <builder@openeuler.org>

%description
Asio is a cross-platform C++ library for network and low-level I/O
programming that provides developers with a consistent asynchronous
model using a modern C++ approach. This package is header-only.

%package        devel
Summary:        Development headers for %{name}
License:        MIT
Requires:       %{name} = %{version}-%{release}

%description    devel
Header-only development files for the Asio C++ library.

%prep
%setup -q -n asio-asio-1-38-0

%build

%install
install -d %{buildroot}%{_includedir}
cp -a include/asio     %{buildroot}%{_includedir}/
cp    include/asio.hpp %{buildroot}%{_includedir}/

%files
%license LICENSE_1_0.txt
%doc README

%files devel
%{_includedir}/asio.hpp
%{_includedir}/asio/

%changelog
* Mon May 18 2026 openEuler Builder <builder@openeuler.org> - 1.38.0-1
- Initial package for asio 1.38.0
