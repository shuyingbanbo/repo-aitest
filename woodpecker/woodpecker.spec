%global debug_package %{nil}

Name:           woodpecker
Version:        0.15.0
Release:        1%{?dist}
Summary:        Woodpecker CI - a community fork of the Drone CI system
License:        Apache-2.0
URL:            https://github.com/woodpecker-ci/woodpecker
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  golang >= 1.16
BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  sqlite-devel
BuildRequires:  git

%description
Woodpecker is a community fork of the Drone CI system.
It provides a simple yet powerful CI/CD pipeline runner.
Note: this package is built without the web UI frontend.

%package agent
Summary:        Woodpecker CI agent

%description agent
The Woodpecker CI agent component that runs pipeline jobs.

%package server
Summary:        Woodpecker CI server

%description server
The Woodpecker CI server component that manages pipelines.
Note: built without pre-compiled web UI frontend.

%package cli
Summary:        Woodpecker CI CLI tool

%description cli
The Woodpecker CI command line interface.

%prep
%setup -q
# Create placeholder dist directory for go:embed to satisfy embed constraint
mkdir -p web/dist
echo '<!DOCTYPE html><html><body>Woodpecker CI</body></html>' > web/dist/index.html

%build
export CGO_ENABLED=1
export GOPROXY=off
export GOFLAGS=-buildvcs=false
export GONOSUMDB=*
LDFLAGS="-s -w -X github.com/woodpecker-ci/woodpecker/version.Version=%{version}"

go build -ldflags "${LDFLAGS}" -o woodpecker-agent ./cmd/agent/
go build -ldflags "${LDFLAGS}" -o woodpecker-server ./cmd/server/
go build -ldflags "${LDFLAGS}" -o woodpecker-cli ./cmd/cli/

%install
install -D -m 0755 woodpecker-agent %{buildroot}%{_bindir}/woodpecker-agent
install -D -m 0755 woodpecker-server %{buildroot}%{_bindir}/woodpecker-server
install -D -m 0755 woodpecker-cli %{buildroot}%{_bindir}/woodpecker

%files
%license LICENSE
%doc README.md

%files agent
%{_bindir}/woodpecker-agent

%files server
%{_bindir}/woodpecker-server

%files cli
%{_bindir}/woodpecker

%changelog
* Tue May 26 2026 Builder <builder@openeuler.org> - 0.15.0-1
- Initial package (without pre-compiled web UI)
