%global debug_package %{nil}
%global __requires_exclude_from ^%{_datadir}/woodpecker/.*

Name:           woodpecker
Version:        0.15.0
Release:        1%{?dist}
Summary:        Woodpecker CI - a community fork of the Drone CI system
License:        Apache-2.0
URL:            https://github.com/woodpecker-ci/woodpecker
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  golang >= 1.16
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  sqlite-devel

%description
Woodpecker is a community fork of the Drone CI system.
It is a simple CI engine with great extensibility.

%package server
Summary:        Woodpecker CI server

%description server
The Woodpecker CI server component.

%package agent
Summary:        Woodpecker CI agent

%description agent
The Woodpecker CI agent component that runs pipeline steps.

%package cli
Summary:        Woodpecker CI command-line client

%description cli
Command-line client for interacting with a Woodpecker CI server.

%prep
%autosetup -n %{name}-%{version}

%build
# Create placeholder web dist so go:embed dist/* is satisfied without a frontend build
mkdir -p web/dist
touch web/dist/.keep

export GOFLAGS="-buildvcs=false -mod=vendor"
export GONOSUMCHECK=*
export GONOSUMDB=*
export VERSION="%{version}"
LDFLAGS="-s -w -extldflags -static -X github.com/woodpecker-ci/woodpecker/version.Version=${VERSION}"

# Build agent (CGO_ENABLED=0)
CGO_ENABLED=0 go build -ldflags "${LDFLAGS}" \
    -o woodpecker-agent github.com/woodpecker-ci/woodpecker/cmd/agent

# Build cli (CGO_ENABLED=0)
CGO_ENABLED=0 go build -ldflags "${LDFLAGS}" \
    -o woodpecker-cli github.com/woodpecker-ci/woodpecker/cmd/cli

# Build server (CGO_ENABLED=1, needs sqlite)
CGO_ENABLED=1 go build -ldflags "-s -w -X github.com/woodpecker-ci/woodpecker/version.Version=${VERSION}" \
    -o woodpecker-server github.com/woodpecker-ci/woodpecker/cmd/server

%install
install -Dm0755 woodpecker-server %{buildroot}%{_bindir}/woodpecker-server
install -Dm0755 woodpecker-agent  %{buildroot}%{_bindir}/woodpecker-agent
install -Dm0755 woodpecker-cli    %{buildroot}%{_bindir}/woodpecker-cli

%files server
%license LICENSE
%{_bindir}/woodpecker-server

%files agent
%license LICENSE
%{_bindir}/woodpecker-agent

%files cli
%license LICENSE
%doc README.md
%{_bindir}/woodpecker-cli

%changelog
* Fri May 22 2026 OpenEuler Packager <packager@openeuler.org> - 0.15.0-1
- Initial package
