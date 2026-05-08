%global debug_package %{nil}

Name:           yq
Version:        4.53.2
Release:        1%{?dist}
Summary:        A lightweight and portable command-line YAML, JSON, XML and CSV processor

License:        MIT
URL:            https://github.com/mikefarah/yq
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  golang >= 1.23
BuildRequires:  make

%description
yq is a lightweight and portable command-line YAML, JSON, INI and XML processor.
It uses jq-like syntax but works with YAML files as well as JSON, XML, INI,
properties, CSV and TSV. Written in Go, it provides a dependency-free binary.

%prep
%setup -q

%build
export CGO_ENABLED=0
export GOPROXY=off
export GOFLAGS=-buildvcs=false

go build -mod=vendor \
    -ldflags "-s -w -X main.GitCommit=tarball -X main.GitDescribe=v4.53.2" \
    -o yq .

%install
install -D -m 755 yq %{buildroot}%{_bindir}/yq

%files
%license LICENSE
%doc README.md
%{_bindir}/yq

%changelog
* Fri May 08 2026 OpenEuler AI Bot <ai@openeuler.org> - 4.53.2-1
- Initial package for yq 4.53.2
