%global debug_package %{nil}

Name:           age
Version:        1.3.1
Release:        1%{?dist}
Summary:        A simple, modern and secure file encryption tool

License:        BSD-2-Clause
URL:            https://github.com/FiloSottile/age
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  golang >= 1.21
BuildRequires:  make

%description
age is a simple, modern and secure file encryption tool, format, and Go library.
It features small explicit keys, post-quantum support, no config options, and
UNIX-style composability.

%prep
%setup -q

%build
export CGO_ENABLED=0
export GOPROXY=off
export GOFLAGS=-buildvcs=false

go build -mod=vendor \
    -ldflags "-s -w -X main.Version=1.3.1" \
    -o age ./cmd/age

go build -mod=vendor \
    -ldflags "-s -w" \
    -o age-keygen ./cmd/age-keygen

%install
install -D -m 755 age %{buildroot}%{_bindir}/age
install -D -m 755 age-keygen %{buildroot}%{_bindir}/age-keygen

%files
%license LICENSE
%doc README.md
%{_bindir}/age
%{_bindir}/age-keygen

%changelog
* Fri May 08 2026 OpenEuler AI Bot <ai@openeuler.org> - 1.3.1-1
- Initial package for age 1.3.1
