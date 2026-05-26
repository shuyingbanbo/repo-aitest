%global debug_package %{nil}

Name:           php-parser
Version:        0.8.0~rc2.20210731git44bbff6
Release:        1%{?dist}
Summary:        PHP parser written in Go with PHP 8 support
License:        MIT
URL:            https://github.com/VKCOM/php-parser
Source0:        https://github.com/VKCOM/php-parser/archive/44bbff6073077c5c35d3bf7e3d4a3b00b85661fe/%{name}-%{version}.tar.gz

BuildRequires:  golang >= 1.13
BuildRequires:  gcc

%description
PHP Parser written in Go. This is a fork that adds PHP 8 support.
It parses PHP source code into an AST (Abstract Syntax Tree) and can
be used to write static analysis, refactoring, metrics, and code style
formatting tools.

%prep
%setup -q

%build
export CGO_ENABLED=0
export GOPROXY=off
export GOFLAGS=-buildvcs=false
export GOPATH=%{_builddir}/gopath

go build -mod=vendor -ldflags "-s -w" -o bin/php-parser ./cmd/php-parser/

%install
install -D -m 0755 bin/php-parser %{buildroot}%{_bindir}/php-parser

%files
%license LICENSE
%doc README.md
%{_bindir}/php-parser

%changelog
* Tue May 26 2026 Builder <builder@openeuler.org> - 0.8.0~rc2.20210731git44bbff6-1
- Initial package snapshot at commit 44bbff6
