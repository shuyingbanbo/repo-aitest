Name:           status-go
Version:        2.3.0
Release:        1%{?dist}
Summary:        Status bindings for go-ethereum — messaging and crypto node
License:        MPL-2.0
URL:            https://github.com/status-im/status-go
Source0:        https://github.com/status-im/status-go/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  golang >= 1.21
BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  sqlite-devel

%description
status-go provides Go bindings for go-ethereum with Status-specific extensions,
including messaging, crypto wallet, and node management functionality.
It exposes statusd (node daemon), status-cli, and bootnode binaries.

%package -n statusd
Summary:        Status node daemon

%description -n statusd
The statusd daemon runs a Status node, providing messaging and Ethereum
node functionality.

%package -n status-cli
Summary:        Status command-line interface

%description -n status-cli
Command-line interface for interacting with a Status node.

%package -n status-bootnode
Summary:        Status bootnode for peer discovery

%description -n status-bootnode
Bootnode for Status peer discovery in the p2p network.

%prep
%autosetup -n %{name}-%{version} -p1
# Fix GCC 12+ ARM64 target attribute syntax in go-sqlcipher vendor
sed -i 's/__attribute__((target("aes,crypto")))/__attribute__((target("+aes,+crypto")))/g' \
    vendor/github.com/mutecomm/go-sqlcipher/v4/aesce.c

%build
export CGO_ENABLED=1
export GOTOOLCHAIN=local
export GOFLAGS=-buildvcs=false
export GOPROXY=off
mkdir -p bin
go build -mod=vendor -o bin/statusd ./cmd/statusd
go build -mod=vendor -o bin/status-cli ./cmd/status-cli
go build -mod=vendor -o bin/bootnode ./cmd/bootnode

%install
install -d %{buildroot}%{_bindir}
install -m 0755 bin/statusd %{buildroot}%{_bindir}/statusd
install -m 0755 bin/status-cli %{buildroot}%{_bindir}/status-cli
install -m 0755 bin/bootnode %{buildroot}%{_bindir}/status-bootnode

%files
%license LICENSE.md
%doc README.md

%files -n statusd
%license LICENSE.md
%{_bindir}/statusd

%files -n status-cli
%license LICENSE.md
%{_bindir}/status-cli

%files -n status-bootnode
%license LICENSE.md
%{_bindir}/status-bootnode

%changelog
* Tue May 26 2026 Go_Bot <Go_Bot@openeuler.org> - 2.3.0-1
- Initial package
