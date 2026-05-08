%global debug_package %{nil}

Name:           gitleaks
Version:        8.30.1
Release:        1%{?dist}
Summary:        A tool for detecting secrets like passwords, API keys, and tokens in git repos

License:        MIT
URL:            https://github.com/gitleaks/gitleaks
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  golang >= 1.21
BuildRequires:  make

%description
Gitleaks is a tool for detecting secrets like passwords, API keys, and tokens
in git repos, files, and whatever else you want to throw at it via stdin.
It supports scanning git history, pre-commit hooks, and CI/CD pipelines.

%prep
%setup -q

%build
export CGO_ENABLED=0
export GOPROXY=off
export GOFLAGS=-buildvcs=false

go build -mod=vendor \
    -ldflags "-s -w -X github.com/zricethezav/gitleaks/v8/version.Version=8.30.1" \
    -o gitleaks .

%install
install -D -m 755 gitleaks %{buildroot}%{_bindir}/gitleaks

%files
%license LICENSE
%doc README.md
%{_bindir}/gitleaks

%changelog
* Fri May 08 2026 OpenEuler AI Bot <ai@openeuler.org> - 8.30.1-1
- Initial package for gitleaks 8.30.1
