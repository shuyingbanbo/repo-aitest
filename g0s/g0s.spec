Name:           g0s
Version:        0.0.1
Release:        1%{?dist}
Summary:        Terminal-based server management tool built with Go
License:        MIT
URL:            https://github.com/theotruvelot/g0s
Source0:        https://github.com/theotruvelot/g0s/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}-%{version}-vendor.tar.gz
BuildRequires:  golang >= 1.21
BuildRequires:  gcc

%description
g0s (pronounced "ghost") is a powerful terminal-based server management tool
built with Go — fast, intuitive, and lightweight. It consists of three main
components: Agent, Server, and TUI (terminal user interface).

%package agent
Summary:        g0s agent component for managed servers

%description agent
Lightweight agent process running on managed servers, collecting metrics
and reporting to the g0s server.

%package server
Summary:        g0s server component for central coordination

%description server
Central coordination and data aggregation server for g0s infrastructure.

%package cli
Summary:        g0s CLI component for terminal user interface

%description cli
Terminal user interface for interacting with g0s server and managed agents.

%prep
%autosetup -n %{name}-%{version} -p1
tar xf %{SOURCE1}

%build
export CGO_ENABLED=0
export GOFLAGS=-buildvcs=false
export GOPROXY=off
mkdir -p bin
go build -mod=vendor -o bin/agent ./cmd/agent/main.go
go build -mod=vendor -o bin/server ./cmd/server/main.go
go build -mod=vendor -o bin/cli ./cmd/cli/main.go

%install
install -d %{buildroot}%{_bindir}
install -m 0755 bin/agent %{buildroot}%{_bindir}/g0s-agent
install -m 0755 bin/server %{buildroot}%{_bindir}/g0s-server
install -m 0755 bin/cli %{buildroot}%{_bindir}/g0s-cli

%files
%license LICENSE
%doc README.md

%files agent
%{_bindir}/g0s-agent

%files server
%{_bindir}/g0s-server

%files cli
%{_bindir}/g0s-cli

%changelog
* Tue May 26 2026 Go_Bot <Go_Bot@openeuler.org> - 0.0.1-1
- Initial package
