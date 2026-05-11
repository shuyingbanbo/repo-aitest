Name:           picocli
Version:        4.7.7
Release:        1%{?dist}
Summary:        Java command line parser with ANSI colors, auto-complete, and sub-commands

License:        Apache-2.0
URL:            https://picocli.info
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
Group:          Development/Libraries
Packager:       openEuler Builder <builder@openeuler.org>

BuildRequires:  java-1.8.0-openjdk-devel
BuildRequires:  maven-local

%description
picocli is a one-file Java framework for parsing command line arguments and
generating usage help. It supports ANSI colors and styles in usage help,
auto-complete, and nested sub-commands. The library has both an annotations API
and a programmatic API, and can be included as source to avoid adding a
dependency.

%package javadoc
Summary:        Javadoc for %{name}
BuildArch:      noarch
Group:          Documentation
Packager:       openEuler Builder <builder@openeuler.org>

%description javadoc
API documentation for %{name}.

%prep
%autosetup -n %{name}-%{version}

%build
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

%files -f .mfiles
%license LICENSE
%doc README.md RELEASE-NOTES.md

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
* Mon May 11 2026 openEuler Builder <builder@openeuler.org> - 4.7.7-1
- Initial package for picocli 4.7.7
