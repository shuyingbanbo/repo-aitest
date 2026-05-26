%global debug_package %{nil}
Name:           kthena
Version:        0.2.0~rc0.20260123git236cfeaf
Release:        1%{?dist}
Summary:        Kubernetes-native LLM inference platform
License:        Apache-2.0
URL:            https://github.com/volcano-sh/kthena
Source0:        https://github.com/volcano-sh/kthena/archive/236cfeaf9e14b8d899a16f54632de7caa8de48b7/%{name}-%{version}.tar.gz

BuildRequires:  golang-1.24
BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  git

%description
Kthena is a Kubernetes-native LLM inference platform that transforms how
organizations deploy and manage Large Language Models in production. Built
with declarative model lifecycle management and intelligent request routing,
it provides high performance and enterprise-grade scalability for LLM
inference workloads.

%package controller-manager
Summary:        Kthena controller manager component

%description controller-manager
The control plane component governing the LLM inference lifecycle. It
continuously reconciles Kthena CRDs to deploy, scale, and upgrade inference
replicas across the cluster.

%package router
Summary:        Kthena router component

%description router
The data plane entry point for inference traffic. It classifies each request
by model name, custom headers, or URI patterns, then applies load-balancing
policies to dispatch requests to the right inference instance.

%package cli
Summary:        Kthena command line interface

%description cli
The Kthena CLI tool for managing LLM inference workloads.

%prep
%setup -q

%build
export PATH=/usr/lib/golang-multiversion/golang-1.24/bin:$PATH
export CGO_ENABLED=0
export GOPROXY=off
export GOFLAGS=-buildvcs=false
export GONOSUMDB=*
export GOPATH=%{_builddir}/gopath

LDFLAGS="-s -w"

go build -mod=vendor -ldflags "${LDFLAGS}" -o bin/kthena-controller-manager ./cmd/kthena-controller-manager/
go build -mod=vendor -ldflags "${LDFLAGS}" -o bin/kthena-router ./cmd/kthena-router/
go build -mod=vendor -ldflags "${LDFLAGS}" -o bin/kthena ./cli/kthena/

%install
install -D -m 0755 bin/kthena-controller-manager %{buildroot}%{_bindir}/kthena-controller-manager
install -D -m 0755 bin/kthena-router %{buildroot}%{_bindir}/kthena-router
install -D -m 0755 bin/kthena %{buildroot}%{_bindir}/kthena

%files
%license LICENSE
%doc README.md

%files controller-manager
%{_bindir}/kthena-controller-manager

%files router
%{_bindir}/kthena-router

%files cli
%{_bindir}/kthena

%changelog
* Tue May 26 2026 Builder <builder@openeuler.org> - 0.2.0~rc0.20260123git236cfeaf-1
- Initial package snapshot at commit 236cfeaf
