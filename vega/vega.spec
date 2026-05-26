%global debug_package %{nil}

Name:           vega
Version:        0.23.1.20200903gitd44074135
Release:        1%{?dist}
Summary:        Decentralised trading platform for derivatives on a blockchain
License:        MIT
URL:            https://github.com/vegaprotocol/vega
Source0:        https://github.com/vegaprotocol/vega/archive/d44074135ac1685dbdca9143f41263ac9fca2853/%{name}-%{version}.tar.gz

BuildRequires:  golang >= 1.14
BuildRequires:  gcc
BuildRequires:  glibc-devel

%description
Vega is a decentralised trading platform that allows pseudo-anonymous
trading of derivatives on a blockchain. It provides governance,
a matching engine, and various API interfaces.

%package -n vegastream
Summary:        Vega streaming service

%description -n vegastream
The Vega streaming service component.

%prep
%setup -q

%build
export CGO_ENABLED=1
export GOPROXY=off
export GOFLAGS=-buildvcs=false
export GOPATH=%{_builddir}/gopath

go build -mod=vendor -ldflags "-s -w" -o bin/vega ./cmd/vega/
go build -mod=vendor -ldflags "-s -w" -o bin/vegastream ./cmd/vegastream/

%install
install -D -m 0755 bin/vega %{buildroot}%{_bindir}/vega
install -D -m 0755 bin/vegastream %{buildroot}%{_bindir}/vegastream

%files
%doc README.md
%{_bindir}/vega

%files -n vegastream
%{_bindir}/vegastream

%changelog
* Tue May 26 2026 Builder <builder@openeuler.org> - 0.23.1.20200903gitd44074135-1
- Initial package snapshot at commit d44074135
